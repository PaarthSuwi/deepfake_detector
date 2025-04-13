# deepfake_detector

# 🧠 Deepfake Detector with GUI 🎭

This project is a lightweight **Deepfake Detection** tool that allows users to upload an image and instantly determine whether it’s a real image or a deepfake. Built with **TensorFlow** and wrapped in a **Tkinter GUI**, this tool provides a user-friendly interface for quick verification.

## 🚀 Features
- 🖼 Upload any image (JPEG, PNG, etc.)
- 🤖 Classifies image as REAL or DEEPFAKE using a trained model
- 📊 Displays prediction confidence score
- 🧩 Simple Tkinter GUI for usability
- 🔍 Logs predictions in a clean visual format

## 🖥 GUI Preview
![App Screenshot](demo_screenshot.png)

## 🗂 Project Structure
deepfake_detector/
├── model/
│   └── deepfake_model.h5      # Pre-trained Keras model
├── utils/
│   └── preprocessing.py       # Image processing utilities
├── gui/
│   └── app.py                 # Tkinter GUI logic
└── predict.py                 # Model inference logic


## 🔧 Requirements
- Python 3.8+
- TensorFlow
- OpenCV
- Pillow
- Tkinter (comes pre-installed with Python)

Install dependencies:
```bash
pip install -r requirements.txt

Run the app
python gui/app.py
```
📂 Model

You need a trained .h5 model placed inside the model/ folder. You can use a custom CNN or pretrained architecture like XceptionNet trained on the Deepfake Detection Challenge dataset.

    Note: The current setup assumes binary classification output (1 = deepfake, 0 = real).

🛡️ Disclaimer

This project is a simplified academic tool and should not be used as a standalone forensic solution. Deepfake detection is a rapidly evolving field — always validate with multiple sources in real-world applications.
👨‍💻 Author

Paarth Suwi
Inspired by the intersection of ethics, AI, and human truth ✨



