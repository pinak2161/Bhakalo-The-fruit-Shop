import tkinter as tk

def create_popup():
    popup = tk.Toplevel(root)
    popup.title("Pop-up Window")
    
    # Set the position of the pop-up window
    popup.geometry("+20+100")  # Replace 100 with the desired X and Y coordinates

    # Add widgets to the pop-up window
    label = tk.Label(popup, text="This is a pop-up window!")
    label.pack(padx=20, pady=20)

# Create the main Tkinter window
root = tk.Tk()
root.title("Main Window")

# Create a button that triggers the pop-up window
popup_button = tk.Button(root, text="Open Pop-up", command=create_popup)
popup_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
