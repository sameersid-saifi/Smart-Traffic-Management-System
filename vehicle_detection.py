import os
import cv2
from ultralytics import YOLO

# Load YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Define vehicle-related classes from COCO
vehicle_labels = ['car', 'bus', 'motorbike', 'truck', 'bicycle']

# Resize and center image in 960x540 canvas while keeping aspect ratio
def resize_keep_aspect(img, target_size=(960, 540)):
    h, w = img.shape[:2]
    scale = min(target_size[0] / w, target_size[1] / h)
    new_w, new_h = int(w * scale), int(h * scale)
    resized = cv2.resize(img, (new_w, new_h))
    canvas = cv2.copyMakeBorder(
        resized,
        top=(target_size[1] - new_h) // 2,
        bottom=(target_size[1] - new_h + 1) // 2,
        left=(target_size[0] - new_w) // 2,
        right=(target_size[0] - new_w + 1) // 2,
        borderType=cv2.BORDER_CONSTANT,
        value=(0, 0, 0)  # black padding
    )
    return canvas

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def detect_and_show(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ Failed to load {image_path}")
        return None

    results = model(img)

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            if label in vehicle_labels:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                conf = box.conf[0].item()
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    return img

def main():
    input_dir = os.path.join(os.getcwd(), "test_images")
    output_dir = os.path.join(os.getcwd(), "output_images")
    ensure_dir(output_dir)

    image_files = sorted([f for f in os.listdir(input_dir)
                          if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

    if not image_files:
        print("❌ No images found in test_images/")
        return

    idx = 0
    while 0 <= idx < len(image_files):
        filename = image_files[idx]
        print(f"🖼️  Showing: {filename} [{idx+1}/{len(image_files)}]")

        img_path = os.path.join(input_dir, filename)
        img = detect_and_show(img_path)

        if img is not None:
            display_img = resize_keep_aspect(img)
            cv2.imshow("Vehicle Detection", display_img)

            key = cv2.waitKey(0)

            if key == 27 or key == ord('q'):  # ESC or q to quit
                break
            idx += 1  # default forward

            # Save output
            output_path = os.path.join(output_dir, f"output_{filename}")
            cv2.imwrite(output_path, img)

            cv2.destroyAllWindows()

    print("✅ Finished.")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
