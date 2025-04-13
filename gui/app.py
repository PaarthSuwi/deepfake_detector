import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from predict import predict_image

class DeepfakeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deepfake Detector")
        self.root.geometry("400x500")

        self.label = tk.Label(root, text="Upload an Image", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.canvas = tk.Label(root)
        self.canvas.pack()

        self.button = tk.Button(root, text="Browse Image", command=self.load_image)
        self.button.pack(pady=10)

        self.result = tk.Label(root, text="", font=("Helvetica", 12))
        self.result.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((250, 250))
            photo = ImageTk.PhotoImage(img)
            self.canvas.configure(image=photo)
            self.canvas.image = photo

            is_fake, confidence = predict_image(file_path)
            result_text = f"DEEPFAKE DETECTED!\nConfidence: {confidence:.2f}" if is_fake else f"REAL IMAGE\nConfidence: {confidence:.2f}"
            self.result.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DeepfakeApp(root)
    root.mainloop()
