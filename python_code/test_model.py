import cv2
from ultralytics import YOLO

model = YOLO("C:/Users/greathtj/Sync/My Downloads/colab_research_google_com/test_v8m/weights/best.pt")
# model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        # =========
        results = model(frame)
        frame = results[0].plot()
        # =========
        cv2.imshow("model_test", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()