import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class FruitShop:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fruit Shop")

        self.cart = {}
        self.product_prices = {"Apple": 2.99, "Banana": 1.99, "Orange": 3.99}

        # Create and display fruit widgets
        self.create_fruit_widgets()

        # Create and display cart image
        cart_image_path = "assets\\Images\\cart.jpg"  # Replace with your actual image path
        self.cart_image = Image.open(cart_image_path)
        self.cart_image = ImageTk.PhotoImage(self.cart_image)
        self.cart_button = tk.Button(self.root, image=self.cart_image, command=self.show_cart)
        self.cart_button.image = self.cart_image  # Keep a reference to avoid garbage collection
        self.cart_button.pack(pady=10)

    def create_fruit_widgets(self):
        for fruit, price in self.product_prices.items():
            # Load and resize fruit image
            img_path = "assets\\Images\\APPLE.jpg"  # Replace with your actual image path
            original_image = Image.open(img_path)
            resized_image = original_image.resize((100, 100))
            fruit_image = ImageTk.PhotoImage(resized_image)

            fruit_label = tk.Label(self.root, image=fruit_image)
            fruit_label.image = fruit_image  # Keep a reference to avoid garbage collection
            fruit_label.pack()

            # Display fruit name and price in a button
            fruit_button = ttk.Button(self.root, text=f"{fruit} - ${price:.2f}", command=lambda f=fruit, p=price: self.add_to_cart(f, p))
            fruit_button.pack(pady=5)

    def add_to_cart(self, fruit, price):
        quantity = self.cart.get(fruit, 0) + 1
        self.cart[fruit] = quantity
        messagebox.showinfo("Added to Cart", f"{fruit} added to the cart!")

    def show_cart(self):
        if not self.cart:
            messagebox.showinfo("Cart", "Cart is empty.")
            return

        cart_content = ""
        total_price = 0

        for fruit, quantity in self.cart.items():
            price = self.product_prices.get(fruit, 0)
            total_price += price * quantity
            cart_content += f"{fruit} - Quantity: {quantity} - Price: ${price * quantity:.2f}\n"

        cart_content += f"\nTotal Bill: ${total_price:.2f}"

        messagebox.showinfo("Cart", cart_content)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    fruit_shop = FruitShop()
    fruit_shop.run()
