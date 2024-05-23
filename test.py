import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


path = './imgs'
pathOut = '/editedImgs'

class MyApp:
    def __init__(self, root):
        self.root = root
        self.current_index = 0
        self.image_paths = []

        # Create an entry widget for folder path
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        # Create a button to submit the entry
        self.button = tk.Button(root, text="Load Images", command=self.load_images)
        self.button.pack(pady=10)

        # Create a canvas to display images
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack(pady=10)

        # Create a button to show the next image
        self.next_button = tk.Button(root, text="Next Image", command=self.show_next_image)
        self.next_button.pack(pady=10)

        # Create a label to display the result
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def load_images(self):
        folder_path = path
        if not os.path.isdir(folder_path):
            messagebox.showerror("Error", "Invalid folder path. Please enter a valid path.")
            return

        try:
            self.image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            if not self.image_paths:
                self.result_label.config(text="No images found in the folder.")
                return

            self.current_index = 0
            self.show_next_image()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def show_next_image(self):
        if not self.image_paths:
            return

        if self.current_index >= len(self.image_paths):
            self.result_label.config(text="No more images to display.")
            return

        image_path = self.image_paths[self.current_index]
        try:
            image = Image.open(image_path)
            #image = image.resize((400, 400), Image.ANTIALIAS)  # Resize the image to fit the canvas
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

            self.result_label.config(text=f"Displaying image {self.current_index + 1} of {len(self.image_paths)}")
            self.current_index += 1
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the image: {e}")

# Create the main window
root = tk.Tk()
root.title("Image Viewer")

# Create an instance of the application class
app = MyApp(root)

# Run the application
root.mainloop()