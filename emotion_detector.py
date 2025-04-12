from deepface import DeepFace
from tkinter import filedialog, Tk
import cv2
import json

# Load config
with open("config.json") as f:
    config = json.load(f)

def detect_emotion():
    if not config.get("emotion_enabled", True):
        print("Emotion detection is disabled in config.")
        return

    root = Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename()

    if not image_path:
        print("No image selected")
        return

    # Analyze emotion
    result = DeepFace.analyze(img_path=image_path, actions=['emotion'])

    # Show results
    print("Predicted Emotion:", result[0]['dominant_emotion'])
    img = cv2.imread(image_path)
    cv2.imshow(f"Emotion: {result[0]['dominant_emotion']}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_emotion()
