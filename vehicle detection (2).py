import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Vehicle classes to filter
vehicle_labels = ['car', 'bus', 'truck', 'motorbike', 'bicycle']

# Open video feed (0 for webcam, or provide path to video file)
cap = cv2.VideoCapture('videos/traffic footage.mp4')  # Replace with your video path

if not cap.isOpened():
    print("Error: Cannot open video feed.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video or can't receive frame.")
        break

    # Run detection on the frame
    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            if label in vehicle_labels:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                conf = box.conf[0].item()
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Resize frame to standard size before showing
    resized_frame = cv2.resize(frame, (960, 540))
    cv2.imshow('Vehicle Detection', resized_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
