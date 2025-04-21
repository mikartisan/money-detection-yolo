## 💵 Philippine Money Security Features Detection
This Python script utilizes the Ultralytics YOLO model in conjunction with OpenCV and CvZone to detect various security features on Philippine peso bills.

## 🧰 Features

- Detects multiple security elements such as:
  - Concealed Value
  - Security Thread
  - See-through Mark
  - Serial Number
  - Value
  - Watermark

- Visualizes detections with bounding boxes and labels.

## 🛠 Requirements

- Python 3.7 or higher
- OpenCV
- CvZone
- Ultralytics YOLO
  
Install the required packages using pip:

```bash
pip install opencv-python cvzone ultralytics
```
## 📂 Usage
 1. Place your target image in the image/ directory.
 2. Ensure your YOLO model weights (money.pt) are located in the weights/ directory.
 3. Run the script:
```bash
pythin main.py
```



