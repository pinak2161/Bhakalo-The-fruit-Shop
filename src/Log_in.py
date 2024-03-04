from tkinter import *
from tkinter import messagebox
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, set_appearance_mode, set_default_color_theme
from PIL import Image, ImageTk
from firebase_admin import credentials, auth, initialize_app
import os
import subprocess
import tkinter as tk

cred = credentials.Certificate("setup\\bhakalo-d2b35-firebase-adminsdk-ahxcm-9ef0ccf015.json")
initialize_app(cred)


from tkinter import Tk, Canvas, Label, NW
from PIL import Image, ImageTk
import os

window = Tk()
window.title("NUTRI FOOD")

script_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_directory, "../assets/Images/bg.jpg")

original_image = Image.open(image_path)


resized_image = original_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.ANTIALIAS)
bg_img = ImageTk.PhotoImage(resized_image)


canvas = Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight(), bg='white')
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=bg_img)


Label(window, text='                   Bhakalo - The Fruit Shop                ', font=('alice', 48, 'bold'), fg='#F60639').place(x=100, y=10)

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

def create_signin_widgets(frame_or_username):
    # Destroy existing widgets in the frame
    if isinstance(frame_or_username, tk.Frame):
        for widget in frame_or_username.winfo_children():
            widget.destroy()

        Label(frame_or_username, text='Sign in', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold')).place(x=130, y=5)

        email_entry = create_entry(frame_or_username, "Username", 80)
        password_entry = create_entry(frame_or_username, "Password", 150)

        Button(frame_or_username, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,
               command=lambda: signin(email_entry, password_entry)).place(x=35, y=230)

        Label(frame_or_username, text='Don\'t have an account?', fg='black', bg='white',
              font=('Microsoft YaHei UI Light', 9)).place(x=60, y=280)

        Button(frame_or_username, width=12, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
               command=lambda: create_signup_widgets(frame_or_username)).place(x=200, y=280)
    else:
        # Handle the case where a username is passed instead of a frame
        # You might want to implement a different behavior for this case
        pass



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
