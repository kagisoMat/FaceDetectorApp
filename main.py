import cv2
import json
import os
from datetime import datetime

# Load config
with open("config.json") as f:
    config = json.load(f)

SAVE_PATH = config.get("save_folder", "snapshots")
os.makedirs(SAVE_PATH, exist_ok=True)

def detect_faces():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    video = cv2.VideoCapture(0)

    while True:
        success, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Fancy Face Detector 😎 (Press s to save, q to quit)', frame)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('s'):
            filename = f"{SAVE_PATH}/face_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Snapshot saved to {filename}")

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_faces()
