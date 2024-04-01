from ultralytics import YOLO
import cv2
import cvzone
import math
import time

image_path = "image/fifty_pesos.jpg"

model = YOLO("weights/money.pt")
classNames = ['concealed_value', 'optically_variable_ink', 'security_thread', 'see_through_mark', 'serial_number', 'value', 'value_invisible_watermark', 'watermark']

img = cv2.imread(image_path)
results = model(img)

for r in results:
    boxes = r.boxes
    for box in boxes:
        # Bounding Box
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        w, h = x2 - x1, y2 - y1

        # Draw a rectangle
        cvzone.cornerRect(img, (x1, y1, w, h), l=20, rt=2, colorR=(255, 0, 255))
        # Confidence
        conf = math.ceil((box.conf[0] * 100)) / 100
        # Class Name
        cls = int(box.cls[0])
        # Display Class name and Confidence
        cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1) + 8, max(35, y1) - 15), scale=1, thickness=1)

# img = cv2.resize(img, (0, 0), None, 0.7, 0.6)
cv2.imshow("Money Security Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
