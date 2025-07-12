# 🌶️ Capsicum Grading and Sorting System using Deep Learning and Raspberry Pi

---

## 📌 Overview

This project automates the **grading and sorting of capsicum (bell peppers)** using image classification techniques and real-time computer vision on a **Raspberry Pi**. The system is capable of detecting whether a capsicum is **fresh** or **stale** using a deep learning model (MobileNet or YOLO-based), and accordingly **activates a conveyor mechanism** to sort it to the left or right basket.

This solution replaces traditional **manual sorting methods** in agricultural and food industries with an efficient, fast, and low-cost embedded system.

---

## 🎯 Purpose and Motivation

In agricultural industries, especially in developing countries like India, **grading and sorting of vegetables** is largely a **manual process**. This method is:

- Time-consuming
- Labor-intensive
- Prone to human error and fatigue

The **primary motivation** behind this project is to provide an **automated, low-cost, and scalable solution** for vegetable grading using **machine vision**, **deep learning**, and **embedded hardware** (Raspberry Pi). This allows industries and farmers to:

- Improve productivity
- Reduce labor costs
- Ensure consistent quality
- Enable scalable post-harvest processing

---

## 🚀 Applications

- 🧑‍🌾 **Smart Agriculture**: Automates grading in agricultural produce sorting centers.
- 🏭 **Food Processing Units**: Integrated with production lines to sort quality capsicum.
- 📦 **Supply Chain Optimization**: Ensures quality at dispatch.
- 🎓 **Educational Demonstration**: Great project for learning embedded AI systems and real-world computer vision.

---

## 🔧 System Components

### 💻 Software Stack

- Python
- PyTorch + torchvision
- OpenCV
- YOLOv5 (for object detection)
- PIL (Python Imaging Library)
- Raspberry Pi GPIO (for hardware control)
- Google Colab (for training)
- ROS (optional, for robotics integration)

### 🔩 Hardware Components

- Raspberry Pi 4
- DC Motors + Conveyor Belt Mechanism
- Motor Driver Module (L298N)
- USB Camera
- Gears, Shaft, Acrylic frame
- Power Supply (12V Adapter)

---

## 🧠 AI Model

The system uses a **MobileNetV1** or **YOLOv5** model trained on a custom dataset containing images of:

- `Fresh Capsicum`
- `Stale Capsicum`

### Dataset:
- Images captured under real conditions and augmented
- Annotated using YOLO format
- Dataset split into training and validation sets

### Training:
- Image size: 224x224 (for MobileNet)
- Framework: PyTorch
- Accuracy achieved: ~80%

---

## 🖼️ System Workflow

1. **Capsicum placed on rotating roller** — rotates for 360° visibility.
2. **Camera captures image**
3. **Image passed to AI model**
4. **Model classifies** image as "Fresh" or "Stale"
5. **Raspberry Pi triggers** the appropriate GPIO:
   - Fresh → Conveyor Right
   - Stale → Conveyor Left
6. **Capsicum sorted** into respective baskets.


🔮 Future Enhancements
Use object detection (YOLO) for detecting multiple capsicums simultaneously

Add size and weight grading using sensors

Export model to TensorRT for faster inference

Web dashboard or touch UI for manual override

Multi-class grading: Add rotten, half-rotten, etc.


---

## 📂 Repository Structure

```bash
.
├── capsicum_model.pth          # Trained PyTorch model
├── capsicum.yaml               # YOLO dataset config
├── detect_and_sort.py          # Real-time detection & motor control code
├── train.py                    # Model training script
├── data/
│   ├── images/
│   │   ├── fresh/
│   │   └── stale/
│   └── labels/
├── README.md                   # Project documentation
```

<img width="624" height="335" alt="result2" src="https://github.com/user-attachments/assets/1bbadb8d-2fe2-4ed4-a553-870ebcd5f23f" />

<img width="662" height="301" alt="result" src="https://github.com/user-attachments/assets/0ac50515-183e-44b5-8da9-1a30b03c56e3" />

<img width="643" height="394" alt="code" src="https://github.com/user-attachments/assets/8bfa5c6d-d98a-4457-8b02-fb00268ba0a5" />

<img width="638" height="332" alt="cad" src="https://github.com/user-attachments/assets/d9d6c3e2-f60b-41af-8c84-4e88b3cfc488" />

<img width="584" height="768" alt="prototype" src="https://github.com/user-attachments/assets/2f64295b-2290-45bc-a40e-aae07e84b9ca" />
