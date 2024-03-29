from tkinter import *
from tkinter import messagebox
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, set_appearance_mode, set_default_color_theme
from PIL import Image, ImageTk
from firebase_admin import credentials, auth, initialize_app
import os
import subprocess
import tkinter as tk

# Initialize Firebase Admin SDK (replace 'path/to/credentials.json' with the actual path)
cred = credentials.Certificate("setup\\bhakalo-d2b35-firebase-adminsdk-ahxcm-9ef0ccf015.json")
initialize_app(cred)

# Create the main application window
from tkinter import Tk, Canvas, Label, NW
from PIL import Image, ImageTk
import os

window = Tk()
window.title("NUTRI FOOD")

script_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_directory, "../assets/bg.jpg")

# Use PIL to open the image and convert it to Tkinter PhotoImage
original_image = Image.open(image_path)

# Resize the image to match the window size
resized_image = original_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.ANTIALIAS)
bg_img = ImageTk.PhotoImage(resized_image)

# Create a Canvas to hold the background image
canvas = Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight(), bg='white')
canvas.pack()

# Display the stretched background image
canvas.create_image(0, 0, anchor="nw", image=bg_img)

# Display the label directly on the root window
Label(window, text='                        Bhakalo - The Fruit Shop                        ', font=('Bodoni', 56, 'bold'), fg='#F60639',bg='#ffe068').place(relx=0.5, rely=0.05, anchor="center")

# Center the window on the screen
window.update_idletasks()
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
x_position = (window.winfo_screenwidth() - window_width) // 2
y_position = (window.winfo_screenheight() - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

def signup(email_entry, password_entry, confirm_password_entry):
    username = email_entry.get()
    password = password_entry.get()
    conform_password = confirm_password_entry.get()

    if password == conform_password:
        try:
            user = auth.create_user(email=username, password=password)
            messagebox.showinfo('Signup', 'Successfully signed up')
            create_signin_widgets(username)
        except auth.EmailAlreadyExistsError:
            messagebox.showinfo('Invalid', 'Email already exists')
        except ValueError as e:
            messagebox.showinfo('Invalid', f'Error: {e}')
    else:
        messagebox.showinfo('Invalid', 'Both passwords should match')

def signin(email_entry, password_entry):
    username = email_entry.get()
    password = password_entry.get()

    try:
        user = auth.get_user_by_email(username)
        # Validate password here
        # If password is correct, proceed
        messagebox.showinfo('Signin', 'Successfully signed in')

        # Hide the login window
        window.withdraw()

        # Run main.py using subprocess
        subprocess.run(["python", "src\\main.py"], check=True)

        # Callback function to be called after main.py completes
        def on_main_complete():
            # Destroy the login window when main.py completes
            window.destroy()

        # Call the callback function after main.py completes
        on_main_complete()

    except auth.UserNotFoundError:
        messagebox.showinfo('Invalid', 'User not found')
    except Exception as e:
        messagebox.showinfo('Invalid', f'Error: {e}')
        messagebox.showinfo('Invalid', f'Error: {e}')
    except subprocess.CalledProcessError as e:
        messagebox.showinfo('Error', f'An error occurred while running main.py: {e}')
    except Exception as e:
        messagebox.showinfo('Error', f'An unexpected error occurred: {e}')


def create_widgets(username=None, show_signup=False):
    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=600, y=140)

    if username:
        Label(frame, text=f'Welcome back, {username}!', fg='black', bg='white',
              font=('Microsoft YaHei UI Light', 12)).place(x=50, y=60)
    else:
        if show_signup:
            create_signup_widgets(frame)
        else:
            create_signin_widgets(frame)

    window.lift()

def create_signup_widgets(frame):
    # Destroy existing widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold')).place(
        x=130, y=5)

    email_entry = create_entry(frame, "Username", 80)
    password_entry = create_entry(frame, "Password", 150)
    confirm_password_entry = create_entry(frame, "Confirm password", 220)

    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0,
           command=lambda: signup(email_entry, password_entry, confirm_password_entry)).place(x=35, y=280)

    Label(frame, text='Already have an account:', fg='black', bg='white',
          font=('Microsoft YaHei UI Light', 9)).place(x=50, y=340)

    Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8',
           command=lambda: create_signin_widgets(frame)).place(x=200, y=340)

def create_signin_widgets(frame):
    # Destroy existing widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text='Sign in', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold')).place(x=130, y=5)

    email_entry = create_entry(frame, "Username", 80)
    password_entry = create_entry(frame, "Password", 150)

    Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,
           command=lambda: signin(email_entry, password_entry)).place(x=35, y=230)

    Label(frame, text='Don\'t have an account?', fg='black', bg='white',
          font=('Microsoft YaHei UI Light', 9)).place(x=60, y=280)

    Button(frame, width=12, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
           command=lambda: create_signup_widgets(frame)).place(x=200, y=280)


def create_entry(frame, placeholder, y_position):
    entry = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    entry.place(x=30, y=y_position)
    entry.insert(0, placeholder)

    def on_enter(e):
        entry.delete(0, 'end')

    def on_leave(e):
        if entry.get() == '':
            entry.insert(0, placeholder)

    entry.bind("<FocusIn>", on_enter)
    entry.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=y_position + 27)

    return entry

# Main window
create_widgets()
window.mainloop()
