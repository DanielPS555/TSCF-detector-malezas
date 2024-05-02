from ultralytics import YOLO

# Build a YOLOv9c model from scratch
model = YOLO('yolov9c.pt')

# Display model information (optional)
model.info()

# Train using GPU with reduced batch size and reduced number of workers
results = model.train(data='All.v2.yolov9/data.yaml', epochs=100, imgsz=640, workers=0, device='cuda')
