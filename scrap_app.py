import streamlit as st
import cv2
import glob
import numpy as np
import time
import json
from tensorflow.keras.models import load_model
import zipfile
import os


ZIP_PATH = "Garbage image dataset.zip"
EXTRACT_PATH = "dataset"

if not os.path.exists(EXTRACT_PATH):
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_PATH)
    st.success("Dataset extracted successfully!")

DATASET_PATH = os.path.join(EXTRACT_PATH, "TrashType_Image_Dataset")


MODEL_PATH = "scrap_model.h5"
model = load_model(MODEL_PATH)


class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
object_counts = {cls: 0 for cls in class_names}

image_paths = glob.glob(DATASET_PATH + "/*/*.jpg") + glob.glob(DATASET_PATH + "/*/*.png")
image_paths.sort()
num_total_images = len(image_paths)
st.sidebar.write(f"Total images found: {num_total_images}")

if num_total_images == 0:
    st.error("No images found in dataset! Check your DATASET_PATH.")
    st.stop()


st.title(" Real-Time Scrap Classification Simulator")
st.sidebar.header("Simulation Settings")

num_images = st.sidebar.slider("Number of images to simulate", min_value=1, max_value=min(50, num_total_images), value=20)
frame_delay = st.sidebar.slider("Frame delay (ms)", min_value=50, max_value=1000, value=200)

frame_placeholder = st.empty()


for img_path in image_paths[:num_images]:
    img = cv2.imread(img_path)
    if img is None:
        continue

    img_resized = cv2.resize(img, (128, 128)) / 255.0
    img_input = np.expand_dims(img_resized, axis=0)

    start_time = time.time()
    predictions = model.predict(img_input)
    latency = (time.time() - start_time) * 1000

    pred_index = np.argmax(predictions)
    label = class_names[pred_index]
    object_counts[label] += 1

    h, w, _ = img.shape
    pick_point = (w // 2, h // 2)
    cv2.circle(img, pick_point, 10, (0, 255, 0), -1)

    cv2.putText(img, f"Type: {label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(img, f"Latency: {latency:.1f} ms", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.putText(img, f"Counts: {object_counts}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    ros_message = {
        "label": label,
        "confidence": float(predictions[0][pred_index]),
        "pick_point": {"x": int(pick_point[0]), "y": int(pick_point[1])},
        "timestamp": time.strftime("%H:%M:%S")
    }
    st.sidebar.json(ros_message)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(img_rgb, channels="RGB")

    time.sleep(frame_delay / 1000)
