# 😷 Face Mask Detection System

A Real-Time Face Mask Detection System built using Python, OpenCV, TensorFlow, Keras, and Deep Learning.

The application uses a webcam to detect human faces and classify whether a person is wearing a face mask or not in real time.

---

## 🚀 Features

✅ Real-Time Face Detection

✅ Face Mask Classification

✅ Webcam Integration

✅ Deep Learning Based Prediction

✅ OpenCV Haar Cascade Face Detection

✅ TensorFlow & Keras Model

✅ Live Bounding Box Visualization

✅ Real-Time Prediction Labels

---

## 🛠 Technologies Used

### Programming Language

- Python

### Computer Vision

- OpenCV

### Deep Learning

- TensorFlow
- Keras

### Numerical Computing

- NumPy

---

## 📂 Project Structure

```text
Face-Mask-Detection-System/
│
├── face_mask_model.keras
├── main.py
├── requirements.txt
├── README.md
│
└── dataset/
```

---

## 📸 Working

The system performs the following steps:

1. Accesses webcam feed.
2. Detects faces using Haar Cascade Classifier.
3. Extracts and preprocesses detected faces.
4. Sends face image to trained CNN model.
5. Predicts:
   - Mask 😷
   - No Mask ❌
6. Displays prediction with colored bounding boxes.

---

## 🤖 Model Information

The face mask classification model was trained using TensorFlow and Keras.

### Classes

| Label | Meaning |
|---------|---------|
| 0 | Mask |
| 1 | No Mask |

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Face-Mask-Detection-System.git
```

### Navigate to Project

```bash
cd Face-Mask-Detection-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
python main.py
```

---

## 📦 Required Libraries

```bash
pip install tensorflow
pip install opencv-python
pip install numpy
```

---

## 📊 Output

### Mask Detected

- Green Bounding Box
- Label: Mask

### No Mask Detected

- Red Bounding Box
- Label: No Mask

---

## 🔮 Future Improvements

- Face Recognition Integration
- Mobile Deployment
- Multi-Person Detection
- Improved CNN Architecture
- Cloud Deployment

---

## 👨‍💻 Developer

Saif Ahmad

GitHub:
https://github.com/Saif-Ahmad11

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

---

## 📜 License

This project is licensed under the MIT License.
