import tkinter as tk
from tkinter import messagebox
import subprocess

def run_detector():
    subprocess.run(["python", "main.py"])

def show_about():
    messagebox.showinfo("About", "This is a Fancy Face Detector using Python and OpenCV!")

app = tk.Tk()
app.title("Fancy Face Detector App")
app.geometry("300x200")

title = tk.Label(app, text="😊 Face Detector 😊", font=("Arial", 18))
title.pack(pady=10)

start_btn = tk.Button(app, text="Start Detecting", command=run_detector)
start_btn.pack(pady=5)

about_btn = tk.Button(app, text="About", command=show_about)
about_btn.pack(pady=5)

exit_btn = tk.Button(app, text="Exit", command=app.quit)
exit_btn.pack(pady=5)

app.mainloop()
