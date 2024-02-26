import tkinter as tk
from PIL import Image, ImageTk

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        self.brand_preview = tk.Label(root)
        self.brand_preview.pack()

        # Load and display the default image
        self.load_image("assets\\Images\\Pear.jpg")

        # Button to delete the image
        self.delete_button = tk.Button(root, text="Delete Image", command=self.clear_label_image)
        self.delete_button.pack()

    def load_image(self, path):
        original_image = Image.open(path)
        resized_image = original_image.resize((300, 200))
        self.tk_image = ImageTk.PhotoImage(resized_image)

        # Display the image in the label
        self.brand_preview.config(image=self.tk_image)
        self.brand_preview.image = self.tk_image

    def clear_label_image(self):
        # Remove the image from the label
        self.brand_preview.config(image='')
        self.brand_preview.image = None

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
