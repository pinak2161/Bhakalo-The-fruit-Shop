
import tkinter as tk
from PIL import Image, ImageTk
import os
class MyApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        # Load the image
        script_directory = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_directory, "../assets/Images/APPLE.jpg")

        original_image = Image.open(img_path)
        resized_image = original_image.resize((200, 150))
        self.img = ImageTk.PhotoImage(resized_image)

        # Create a label and display the image
        self.image_label = tk.Label(self.root, image=self.img)
        self.image_label.pack()

        # Bind the function to the label click event
        self.image_label.bind("<Button-1>", self.image_clicked)

    def image_clicked(self, event):
        print("Image clicked!")
        # Call the method or perform actions you want here

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
