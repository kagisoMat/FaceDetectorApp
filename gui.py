import tkinter as tk
import subprocess

def run_webcam():
    subprocess.run(["python", "main.py"])

def run_image_detector():
    subprocess.run(["python", "image_detector.py"])

def run_emotion_detector():
    subprocess.run(["python", "emotion_detector.py"])

app = tk.Tk()
app.title("Face Detection Toolkit")
app.geometry("350x300")

tk.Label(app, text="😎 Fancy Face Detector Toolkit", font=("Arial", 16)).pack(pady=10)

tk.Button(app, text="1️⃣ Detect Faces (Webcam)", command=run_webcam).pack(pady=5)
tk.Button(app, text="2️⃣ Detect Faces (Image)", command=run_image_detector).pack(pady=5)
tk.Button(app, text="3️⃣ Detect Emotion (Image)", command=run_emotion_detector).pack(pady=5)
tk.Button(app, text="❌ Exit", command=app.quit).pack(pady=15)

app.mainloop()
