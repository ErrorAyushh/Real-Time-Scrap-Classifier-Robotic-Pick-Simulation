 ## Real-Time Scrap Classifier & Robotic Pick Simulation  

This project demonstrates a **real-time waste classification system** using **MobileNetV2** for image classification and a **robotic pick simulation** to visualize automated waste sorting.  
The goal is to classify different types of scrap (metal, plastic, paper, etc.) and simulate how a robotic arm could pick and place items accordingly.  

---

## 🔹 1. Approach  

### Dataset Preparation  
- Used the **Garbage Image Dataset (TrashType_Image_Dataset)** (~2500+ images).  
- Organized images into categories (plastic, metal, paper, glass, etc.).  
- Applied preprocessing steps such as resizing, normalization, and augmentation.  

### Model Training (MobileNetV2)  
- Implemented **MobileNetV2**, a lightweight CNN optimized for image classification.  
- Fine-tuned on the dataset with transfer learning.  
- **Achieved 84% classification accuracy** on the validation set.  

### Real-Time Classification  
- Integrated with a live webcam feed.  
- Each detected item is classified instantly and displayed with labels.  

### Robotic Pick Simulation  
- Simulated how a robotic arm could automatically pick and place classified items into respective bins.  
- Acts as a **proof-of-concept** for smart waste management systems.  

---

## 🔹 2. Libraries Used  

- **TensorFlow / Keras** – Model building & training  
- **OpenCV** – Image capture & real-time video processing  
- **NumPy** – Numerical computations  
- **Matplotlib / Seaborn** – Visualization of results  
- **OS / Zipfile / Shutil** – Dataset handling  

---

3. How to Run

Clone the repository:

git clone https://github.com/your-username/scrap-classifier.git
cd scrap-classifier


Install dependencies:

pip install -r requirements.txt


Prepare dataset:

Place your dataset folder (TrashType_Image_Dataset) inside the data/ directory.

Train the model (optional):

python train.py


Run real-time classifier:

python app.py

🔹 4. Challenges Faced

Dataset Imbalance – Some classes had fewer images, which impacted accuracy. Used augmentation to address this.

Real-Time Constraints – Ensuring the classifier ran smoothly without heavy GPU requirements. MobileNet helped here.

Robotic Simulation – Designing a realistic robotic arm pick-up simulation using only OpenCV was challenging.

Accuracy Trade-off – Balancing between speed (real-time performance) and accuracy. Final model achieved 84% accuracy.

🔹 5. Demo

🎥 Video Demo: [Demo Link or upload video file]
Or you can create a quick GIF demo showing:

Image input

Classification result

Simulated robotic pick action
