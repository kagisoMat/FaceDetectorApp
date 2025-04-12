import cv2
from tkinter import filedialog
from tkinter import Tk

def detect_faces_in_image(file_path):
    image = cv2.imread(file_path)
    if image is None:
        print("Error loading image.")
        return

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Optional: You can let the user select the file here if not testing
    detect_faces_in_image("test_image.jpg")  # Replace with your image path
