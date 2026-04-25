# Install YOLOv8
!pip install ultralytics

from ultralytics import YOLO

# Load pretrained YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Train model
model.train(
    data="/content/waste_detection/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16
)

# Validate model
metrics = model.val()

# Run prediction on test set
model.predict(
    source="/content/waste_detection/images/test",
    save=True,
    conf=0.25
)

# Download important files
from google.colab import files

files.download("/content/runs/detect/train/weights/best.pt")
files.download("/content/runs/detect/train/results.png")
files.download("/content/runs/detect/train/confusion_matrix.png")