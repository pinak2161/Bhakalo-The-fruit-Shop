from PIL import Image,ImageTk
import tkinter as tk
import os
from tkinter import ttk, messagebox,PhotoImage,Label
import requests
#this is my project
class Bhakalo:
    def __init__(self):
        #Initialize the Tkinter Root Window
        self.root = tk.Tk()
        self.screen_width = 1900
        self.screen_height= 1000
        self.root.title("Bhakalo Fruit Shop")

        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.configure(bg = "#192f44")
        self.original_label_text = "Welcome to Bhakalo"
        #Setup the UI components
        self.setup_ui()
        self.table_window = None
        self.table_label = None
    def setup_ui(self):

        #Create the background frame
        self.background_frame = tk.Frame(self.root, bg = "#0A2472",width=self.screen_width,height=self.screen_height)
        self.background_frame.pack()

        #Create left frame for navigation and buttons
        self.left_frame = tk.Frame(self.background_frame, bg = "#ff9147",width=self.screen_width // 7,height=self.screen_height)
        self.left_frame.pack(side=tk.LEFT)

        #Set up button Styling
        style = ttk.Style()
        style.configure("Rounded.TButton", borderwidth=0, relief="flat",background="#BCD2E8", padding = 10, font=("Calibri",12))
        style.map("Rounded.TButton",foreground=[('pressed','black'),('active','white')])

        #Create the fruits button
        self.button_label = ttk.Button(self.left_frame,text="My Store", style="Rounded.TButton",command=self.fruit_tab)
        self.button_label.pack()
        self.button_label.place(x=75,y=350,anchor='nw')

        #Create the Account button
        self.button_label = ttk.Button(self.left_frame,text="My Account", style="Rounded.TButton",command=self.account_tab)
        self.button_label.pack()
        self.button_label.place(x=75,y=420,anchor='nw')

        #Create the sale button
        self.button_label = ttk.Button(self.left_frame,text="My cart", style="Rounded.TButton",command=self.cart_tab)
        self.button_label.pack()
        self.button_label.place(x=75,y=490,anchor='nw')

        #Create the OurBlogs button
        self.button_label = ttk.Button(self.left_frame,text="Our Blogs", style="Rounded.TButton",command=self.ourblogs_tab)
        self.button_label.pack()
        self.button_label.place(x=75,y=560,anchor='nw')
       
        #Load and Display an Image
        script_directory = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_directory,"../assets/user.jpg")
        img = ImageTk.PhotoImage(Image.open(img_path))
        original_image = Image.open(img_path)
        resized_image = original_image.resize((150, 175))  
        img = ImageTk.PhotoImage(resized_image)
        self.label = tk.Label(self.left_frame, image=img,background="#00072D")
        self.label.image_types = img
        self.label.pack()
        self.label.place(x=50, y=130, anchor="nw")

        # Welcome user
        welcome_label = tk.Label(self.left_frame, text="Welcome User", background="#00072D", fg="#BCD2E8", font=("Monotype", 24, "bold"))
        welcome_label.pack()
        welcome_label.place(x=20, y=70, anchor="nw")

        #Setup the right frame for dynamic content
        rgba_color = (222,55,48,255)
        tk_color = "#{:02x}{:02x}{:02x}".format(*rgba_color[:3])
        self.right_frame = tk.Frame(self.background_frame,bg="#BCD2E8",width=(self.screen_width - self.screen_width // 6),height=self.screen_height)
        self.right_frame.pack(side=tk.RIGHT)

        #Create a "Back" button
        self.back_button = ttk.Button(self.left_frame,text="Back",style="Rounded.TButton",command=self.reset_ui)
        self.back_button.pack()
        self.back_button.place(x=75,y=630,anchor="nw")

        #Track whether Font Library is open and additional widgets
        self.fruit_tab_opened = False
        self.secondtab_opened = False
        self.thirdtab_opened = False
        self.fourthtab_opened = False
        self.fifthtab_opened = False
        self.account_tab_opened = False
        self.cart_tab_opened = False
        self.ourblogs_tab_opened = False
        self.additional_widgets = []

    # Load and Display an Image in the right frame
        script_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_directory, "../assets/bg1.jpg")

        # Use PIL to open the image and convert it to Tkinter PhotoImage
        original_image = Image.open(image_path)
        resized_image = original_image.resize((self.screen_width - self.screen_width // 6, self.screen_height), Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(resized_image)

        # Create the label with the background image
        self.bg_label = tk.Label(self.right_frame, image=bg_img)
        self.bg_label.image = bg_img  # Keep a reference to the image to prevent it from being garbage collected
        self.bg_label.place(x=0, y=0, anchor="nw")

        # Create a label for welcome text on top of the image
        tk_color = "#FFA101"
        welcome_label = tk.Label(self.right_frame, text=self.original_label_text, font=("Calibri", 50, "bold"), fg=tk_color)
        welcome_label.place(relx=0.5, rely=0.5, anchor="center")
    

        
    
    def fruit_tab(self):
        #Show Font Library tab
        if self.fruit_tab_opened:
            pass
        else:
            #Destroy existing widgets
            for widget in self.additional_widgets:
                widget.destroy()
            self.additional_widgets = []

            #Set up front library tab
            rgba_color = (222,55,48,255)
            tk_color = "#{:02x}{:02x}{:02x}".format(*rgba_color[:3])

            
            #Create and pack widgets for label
            self.heading_label = tk.Label(self.right_frame,text="Fruits",font=("Calibri ",20,"bold"),fg=tk_color)
            self.heading_label.pack()
            self.heading_label.place(x=50,y=50,anchor="nw")

            self.input_label = ttk.Entry(self.right_frame, width=60, font=("Calibri", 12))
            self.input_label.insert(0,"Enter the fruit name...")
            self.input_label.pack()
            self.input_label.place(x=50,y=100,anchor="nw")

            self.button_nextpage = ttk.Button(self.right_frame,text ="2>", style="Rounded.TButton",command=self.secondtab)
            self.button_nextpage.pack()
            self.button_nextpage.place(x=950,y=625,anchor='nw')         

            self.fruit_tab_opened = True

            #Create buttons for different fonts
            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/APPLE.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image1 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image1)
            self.label1 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label1.image_types = img
            self.label1.pack()
            self.label1.place(x=100, y=150, anchor="nw")

            self.button_label1 = ttk.Button(self.right_frame,text ="Apple", style="Rounded.TButton",command=self.appleClicked)
            self.button_label1.pack()
            self.button_label1.place(x=100,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/BANANA.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image2 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image2)
            self.label2 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label2.image_types = img
            self.label2.pack()
            self.label2.place(x=425, y=150, anchor="nw")

            self.button_label2 = ttk.Button(self.right_frame,text ="Banana", style="Rounded.TButton",command=self.bananaClicked)
            self.button_label2.pack()
            self.button_label2.place(x=425,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Cherry.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image3 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image3)
            self.label3 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label3.image_types = img
            self.label3.pack()
            self.label3.place(x=750, y=150, anchor="nw")

            self.button_label3 = ttk.Button(self.right_frame,text="Cherry", style="Rounded.TButton",command=self.cherryClicked)
            self.button_label3.pack()
            self.button_label3.place(x=750,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Dragon Fruit.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image4 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image4)
            self.label4 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label4.image_types = img
            self.label4.pack()
            self.label4.place(x=100, y=400, anchor="nw")

            self.button_label4 = ttk.Button(self.right_frame,text="Dragon Fruit", style="Rounded.TButton",command=self.dragonfruitClicked)
            self.button_label4.pack()
            self.button_label4.place(x=100,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Gooseberry.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image4 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image4)
            self.label5 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label5.image_types = img
            self.label5.pack()
            self.label5.place(x=425, y=400, anchor="nw")

            self.button_label5 = ttk.Button(self.right_frame,text='Gooseberry', style="Rounded.TButton",command=self.gooseberryClicked)
            self.button_label5.pack()
            self.button_label5.place(x=425,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Jackfruit.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image4 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image4)
            self.label6 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label6.image_types = img
            self.label6.pack()
            self.label6.place(x=750, y=400, anchor="nw")

            self.button_label6 = ttk.Button(self.right_frame,text="Jack Fruit", style="Rounded.TButton",command=self.jackfruitClicked)
            self.button_label6.pack()
            self.button_label6.place(x=750,y=600,anchor='nw')

    def secondtab(self):
        #Show Font Library tab
        if self.secondtab_opened:
            messagebox.showinfo("Already opened","Second tab is already opened!")
        else:
            #Destroy existing widgets
            for widget in self.additional_widgets:
                widget.destroy()
            self.additional_widgets = []

            #Set up front library tab
            rgba_color = (222,55,48,255)
            tk_color = "#{:02x}{:02x}{:02x}".format(*rgba_color[:3])

            
            #Create and pack widgets for label
            self.heading_label = tk.Label(self.right_frame,text="Fruits",font=("Calibri ",20,"bold"),fg=tk_color)
            self.heading_label.pack()
            self.heading_label.place(x=50,y=50,anchor="nw")

            self.input_label = ttk.Entry(self.right_frame, width=60, font=("Calibri", 12))
            self.input_label.insert(0,"Enter the fruit name...")
            self.input_label.pack()
            self.input_label.place(x=50,y=100,anchor="nw")  

            self.button_nextpage = ttk.Button(self.right_frame,text ="3>", style="Rounded.TButton",command=self.thirdtab)
            self.button_nextpage.pack()
            self.button_nextpage.place(x=950,y=625,anchor='nw')         

            self.secondtab_opened = True

            #Create buttons for different fonts
            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Lemon.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image7 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image7)
            self.label7 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label7.image_types = img
            self.label7.pack()
            self.label7.place(x=100, y=150, anchor="nw")

            self.button_label7 = ttk.Button(self.right_frame,text ="Lemon", style="Rounded.TButton",command=self.lemonClicked)
            self.button_label7.pack()
            self.button_label7.place(x=100,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Mango.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image8 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image8)
            self.label8 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label8.image_types = img
            self.label8.pack()
            self.label8.place(x=425, y=150, anchor="nw")

            self.button_label8 = ttk.Button(self.right_frame,text ="Mango", style="Rounded.TButton",command=self.mangoClicked)
            self.button_label8.pack()
            self.button_label8.place(x=425,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Orange.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image9 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image9)
            self.label9 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label9.image_types = img
            self.label9.pack()
            self.label9.place(x=750, y=150, anchor="nw")

            self.button_label9 = ttk.Button(self.right_frame,text="Orange", style="Rounded.TButton",command=self.orangeClicked)
            self.button_label9.pack()
            self.button_label9.place(x=750,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Pineapple.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image10 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image10)
            self.label10 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label10.image_types = img
            self.label10.pack()
            self.label10.place(x=100, y=400, anchor="nw")

            self.button_label10 = ttk.Button(self.right_frame,text="Pineapple", style="Rounded.TButton",command=self.pineappleClicked)
            self.button_label10.pack()
            self.button_label10.place(x=100,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Strawberry.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image11 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image11)
            self.label11 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label11.image_types = img
            self.label11.pack()
            self.label11.place(x=425, y=400, anchor="nw")

            self.button_label11 = ttk.Button(self.right_frame,text='Strawberry', style="Rounded.TButton",command=self.strawberryClicked)
            self.button_label11.pack()
            self.button_label11.place(x=425,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Watermelon.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image12 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image12)
            self.label12 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label12.image_types = img
            self.label12.pack()
            self.label12.place(x=750, y=400, anchor="nw")

            self.button_label12 = ttk.Button(self.right_frame,text="Watermelon", style="Rounded.TButton",command=self.watermelonClicked)
            self.button_label12.pack()
            self.button_label12.place(x=750,y=600,anchor='nw')

    def thirdtab(self):
        #Show Font Library tab
        if self.thirdtab_opened:
            messagebox.showinfo("Already opened","Third tab is already opened!")
        else:
            #Destroy existing widgets
            for widget in self.additional_widgets:
                widget.destroy()
            self.additional_widgets = []

            #Set up front library tab
            rgba_color = (222,55,48,255)
            tk_color = "#{:02x}{:02x}{:02x}".format(*rgba_color[:3])

            
            #Create and pack widgets for label
            self.heading_label = tk.Label(self.right_frame,text="Fruits",font=("Calibri ",20,"bold"),fg=tk_color)
            self.heading_label.pack()
            self.heading_label.place(x=50,y=50,anchor="nw")

            self.input_label = ttk.Entry(self.right_frame, width=60, font=("Calibri", 12))
            self.input_label.insert(0,"Enter the fruit name...")
            self.input_label.pack()
            self.input_label.place(x=50,y=100,anchor="nw")  

            self.button_nextpage = ttk.Button(self.right_frame,text ="4>", style="Rounded.TButton",command=self.fourthtab)
            self.button_nextpage.pack()
            self.button_nextpage.place(x=950,y=625,anchor='nw')         

            self.thirdtab_opened = True

            #Create buttons for different fonts
            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Quince.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image13 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image13)
            self.label13 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label13.image_types = img
            self.label13.pack()
            self.label13.place(x=100, y=150, anchor="nw")

            self.button_label13 = ttk.Button(self.right_frame,text ="Quince", style="Rounded.TButton",command=self.quinceClicked)
            self.button_label13.pack()
            self.button_label13.place(x=100,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Tomato.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image14 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image14)
            self.label14 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label14.image_types = img
            self.label14.pack()
            self.label14.place(x=425, y=150, anchor="nw")

            self.button_label14 = ttk.Button(self.right_frame,text ="Tomato", style="Rounded.TButton",command=self.tomatoClicked)
            self.button_label14.pack()
            self.button_label14.place(x=425,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Zucchini.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image15 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image15)
            self.label15 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label15.image_types = img
            self.label15.pack()
            self.label15.place(x=750, y=150, anchor="nw")

            self.button_label15 = ttk.Button(self.right_frame,text="Zucchini", style="Rounded.TButton",command=self.zucchiniClicked)
            self.button_label15.pack()
            self.button_label15.place(x=750,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Custardapple.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image16 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image16)
            self.label16 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label16.image_types = img
            self.label16.pack()
            self.label16.place(x=100, y=400, anchor="nw")

            self.button_label16 = ttk.Button(self.right_frame,text="Custardapple", style="Rounded.TButton",command=self.custardappleClicked)
            self.button_label16.pack()
            self.button_label16.place(x=100,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Kiwi.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image17 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image17)
            self.label17 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label17.image_types = img
            self.label17.pack()
            self.label17.place(x=425, y=400, anchor="nw")

            self.button_label17 = ttk.Button(self.right_frame,text='Kiwi', style="Rounded.TButton",command=self.kiwiClicked)
            self.button_label17.pack()
            self.button_label17.place(x=425,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Pomegranate.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image18 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image18)
            self.label18 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label18.image_types = img
            self.label18.pack()
            self.label18.place(x=750, y=400, anchor="nw")

            self.button_label18 = ttk.Button(self.right_frame,text="Pomegranate", style="Rounded.TButton",command=self.pomogranateClicked)
            self.button_label18.pack()
            self.button_label18.place(x=750,y=600,anchor='nw')

    def fourthtab(self):
        #Show Font Library tab
        if self.fourthtab_opened:
            messagebox.showinfo("Already opened","Fourth tab is already opened!")
        else:
            #Destroy existing widgets
            for widget in self.additional_widgets:
                widget.destroy()
            self.additional_widgets = []

            #Set up front library tab
            rgba_color = (222,55,48,255)
            tk_color = "#{:02x}{:02x}{:02x}".format(*rgba_color[:3])

            
            #Create and pack widgets for label
            self.heading_label = tk.Label(self.right_frame,text="Fruits",font=("Calibri ",20,"bold"),fg=tk_color)
            self.heading_label.pack()
            self.heading_label.place(x=50,y=50,anchor="nw")

            self.input_label = ttk.Entry(self.right_frame, width=60, font=("Calibri", 12))
            self.input_label.insert(0,"Enter the fruit name...")
            self.input_label.pack()
            self.input_label.place(x=50,y=100,anchor="nw")  

            self.button_nextpage = ttk.Button(self.right_frame,text ="5>", style="Rounded.TButton",command=self.fifthtab)
            self.button_nextpage.pack()
            self.button_nextpage.place(x=950,y=625,anchor='nw')         

            self.fourthtab_opened = True

            #Create buttons for different fonts
            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Blackberry.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image19 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image19)
            self.label19 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label19.image_types = img
            self.label19.pack()
            self.label19.place(x=100, y=150, anchor="nw")

            self.button_label19 = ttk.Button(self.right_frame,text ="Blackberry", style="Rounded.TButton",command=self.blackberryClicked)
            self.button_label19.pack()
            self.button_label19.place(x=100,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Grapes.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image20 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image20)
            self.label20 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label20.image_types = img
            self.label20.pack()
            self.label20.place(x=425, y=150, anchor="nw")

            self.button_label20 = ttk.Button(self.right_frame,text ="Grapes", style="Rounded.TButton",command=self.grapesClicked)
            self.button_label20.pack()
            self.button_label20.place(x=425,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Pear.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image21 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image21)
            self.label21 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label21.image_types = img
            self.label21.pack()
            self.label21.place(x=750, y=150, anchor="nw")

            self.button_label21 = ttk.Button(self.right_frame,text="Pear", style="Rounded.TButton",command=self.pearClicked)
            self.button_label21.pack()
            self.button_label21.place(x=750,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Avacado.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image22 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image22)
            self.label22 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label22.image_types = img
            self.label22.pack()
            self.label22.place(x=100, y=400, anchor="nw")

            self.button_label22 = ttk.Button(self.right_frame,text="Avacado", style="Rounded.TButton",command=self.avacadoClicked)
            self.button_label22.pack()
            self.button_label22.place(x=100,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Lichi.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image23 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image23)
            self.label23 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label23.image_types = img
            self.label23.pack()
            self.label23.place(x=425, y=400, anchor="nw")

            self.button_label23 = ttk.Button(self.right_frame,text='Lichi', style="Rounded.TButton",command=self.lichiClicked)
            self.button_label23.pack()
            self.button_label23.place(x=425,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Blueberry.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image24 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image24)
            self.label24 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label24.image_types = img
            self.label24.pack()
            self.label24.place(x=750, y=400, anchor="nw")

            self.button_label24 = ttk.Button(self.right_frame,text="Blueberry", style="Rounded.TButton",command=self.blueberryClicked)
            self.button_label24.pack()
            self.button_label24.place(x=750,y=600,anchor='nw')

    def fifthtab(self):
        #Show Font Library tab
        if self.fifthtab_opened:
            messagebox.showinfo("Already opened","Fifth tab is already opened!")
        else:
            #Destroy existing widgets
            for widget in self.additional_widgets:
                widget.destroy()
            self.additional_widgets = []

            #Set up front library tab
            rgba_color = (222,55,48,255)
            tk_color = "#{:02x}{:02x}{:02x}".format(*rgba_color[:3])

            
            #Create and pack widgets for label
            self.heading_label = tk.Label(self.right_frame,text="Fruits",font=("Calibri ",20,"bold"),fg=tk_color)
            self.heading_label.pack()
            self.heading_label.place(x=50,y=50,anchor="nw")

            self.input_label = ttk.Entry(self.right_frame, width=60, font=("Calibri", 12))
            self.input_label.insert(0,"Enter the fruit name...")
            self.input_label.pack()
            self.input_label.place(x=50,y=100,anchor="nw")  

            self.button_nextpage = ttk.Button(self.right_frame,text =" Back", style="Rounded.TButton",command=self.cart_tab)
            self.button_nextpage.pack()
            self.button_nextpage.place(x=950,y=625,anchor='nw')         

            self.fifthtab_opened = True

            #Create buttons for different fonts
            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Muskmelon.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image25 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image25)
            self.label25 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label25.image_types = img
            self.label25.pack()
            self.label25.place(x=100, y=150, anchor="nw")

            self.button_label25 = ttk.Button(self.right_frame,text ="Muskmelon", style="Rounded.TButton",command=self.muskmelonClicked)
            self.button_label25.pack()
            self.button_label25.place(x=100,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Papaya.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image26 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image26)
            self.label26 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label26.image_types = img
            self.label26.pack()
            self.label26.place(x=425, y=150, anchor="nw")

            self.button_label26 = ttk.Button(self.right_frame,text ="Papaya", style="Rounded.TButton",command=self.papayaClicked)
            self.button_label26.pack()
            self.button_label26.place(x=425,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Peach.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image27 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image27)
            self.label27 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label27.image_types = img
            self.label27.pack()
            self.label27.place(x=750, y=150, anchor="nw")

            self.button_label27 = ttk.Button(self.right_frame,text="Peach", style="Rounded.TButton",command=self.peachClicked)
            self.button_label27.pack()
            self.button_label27.place(x=750,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Gauva.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image28 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image28)
            self.label28 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label28.image_types = img
            self.label28.pack()
            self.label28.place(x=100, y=400, anchor="nw")

            self.button_label28 = ttk.Button(self.right_frame,text="Gauva", style="Rounded.TButton",command=self.guavaClicked)
            self.button_label28.pack()
            self.button_label28.place(x=100,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Grapefruit.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image29 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image29)
            self.label29 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label29.image_types = img
            self.label29.pack()
            self.label29.place(x=425, y=400, anchor="nw")

            self.button_label29 = ttk.Button(self.right_frame,text='Grapefruit', style="Rounded.TButton",command=self.grapefruitClicked)
            self.button_label29.pack()
            self.button_label29.place(x=425,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/Raspberry.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            resized_image30 = original_image.resize((225, 175))  
            img = ImageTk.PhotoImage(resized_image30)
            self.label30 = tk.Label(self.right_frame, image=img, background="#00072D")
            self.label30.image_types = img
            self.label30.pack()
            self.label30.place(x=750, y=400, anchor="nw")

            self.button_label30 = ttk.Button(self.right_frame,text="Raspberry", style="Rounded.TButton",command=self.raspberryClicked)
            self.button_label30.pack()
            self.button_label30.place(x=750,y=600,anchor='nw')

    def account_tab(self):
        #Show Font Library tab
        if self.account_tab_opened:
            messagebox.showinfo("Already opened","My Account page is already opened!")
        else:
            #Destroy existing widgets
            for widget in self.additional_widgets:
                widget.destroy()
            self.additional_widgets = []
        self.account_tab_opened =True

    def cart_tab(self):
        #Show Font Library tab
        if self.cart_tab_opened:
            messagebox.showinfo("Already opened","My cart page is already opened!")
        else:
            #Destroy existing widgets
            for widget in self.additional_widgets:
                widget.destroy()
            self.additional_widgets = []
        self.cart_tab_opened = True

    def ourblogs_tab(self):
        #Show Font Library tab
        if self.ourblogs_tab_opened:
            messagebox.showinfo("Already opened","Our blogs are already opened!")
        else:
            #Destroy existing widgets
            for widget in self.additional_widgets:
                widget.destroy()
            self.additional_widgets = []    
        self.ourblogs_tab_opened =  True
        
    def get_nutrition_info(self, food_name):
        api_key = 'p5y9oPvsHagFwbduywWIYw==8eg8cKkiv8LupO2g'  # Replace with your actual Calorieninjas API key

        try:
            response = requests.get(
                f'https://api.calorieninjas.com/v1/nutrition?query={food_name}', headers={'X-Api-Key': api_key})
            if response.status_code == requests.codes.ok:
                data = response.json()
                print(f"API Response for {food_name}:\n{data}")  # Print the entire response
                if 'items' in data and data['items']:
                    item = data['items'][0]
                    nutrients = [
                        {'title': 'Calories', 'amount': item['calories'], 'unit': 'cal'},
                        {'title': 'Fat', 'amount': item['fat_total_g'], 'unit': 'g'},
                        {'title': 'Saturated Fat', 'amount': item['fat_saturated_g'], 'unit': 'g'},
                        {'title': 'Protein', 'amount': item['protein_g'], 'unit': 'g'},
                        {'title': 'Sodium', 'amount': item['sodium_mg'], 'unit': 'mg'},
                        {'title': 'Potassium', 'amount': item['potassium_mg'], 'unit': 'mg'},
                        {'title': 'Cholesterol', 'amount': item['cholesterol_mg'], 'unit': 'mg'},
                        {'title': 'Carbohydrates', 'amount': item['carbohydrates_total_g'], 'unit': 'g'},
                        {'title': 'Fiber', 'amount': item['fiber_g'], 'unit': 'g'},
                        {'title': 'Sugar', 'amount': item['sugar_g'], 'unit': 'g'},
                    ]

                    return nutrients
        except requests.RequestException as e:
            print(f"Error fetching data from Calorieninjas API: {e}")

        return None

    def create_table_window(self, nutrients):
        # Create a new Toplevel window for the table
        self.table_window = tk.Toplevel(self.root)
        self.table_window.title("Nutrition Information")

        # Create and pack a Label for the nutritional information
        self.table_label = tk.Label(self.table_window, text="Nutrition Information", font=("Calibri", 16, "bold"))
        self.table_label.pack()

        # Create and pack Labels for each nutrient
        for nutrient in nutrients:
            nutrient_label = tk.Label(self.table_window, text=f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}")
            nutrient_label.pack()

    def appleClicked(self):
        food_name = 'Apple'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    
    def bananaClicked(self):
        food_name = 'Banana'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    
        
    def cherryClicked(self):
        food_name = 'cherry'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    

    def dragonfruitClicked(self):
        food_name = 'dragonfruit'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def gooseberryClicked(self):
        food_name = 'gooseberry'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def jackfruitClicked(self):
        food_name = 'jackfruit'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def lemonClicked(self):
        food_name = 'lemon'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def mangoClicked(self):
        food_name = 'mango'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def orangeClicked(self):
        food_name = 'orange'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def pineappleClicked(self):
        food_name = 'pineapple'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def strawberryClicked(self):
        food_name = 'strawberry'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def watermelonClicked(self):
        food_name = 'watermelon'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def grapesClicked(self):
        food_name = 'grapes'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def blackberryClicked(self):
        food_name = 'blackberry'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def custardappleClicked(self):
        food_name = 'custardapple'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def muskmelonClicked(self):
        food_name = 'muskmelon'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def avacadoClicked(self):
        food_name = 'avacado'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def pearClicked(self):
        food_name = 'cherry'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def peachClicked(self):
        food_name = 'peach'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def lichiClicked(self):
        food_name = 'lichi'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def blueberryClicked(self):
        food_name = 'blueberry'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def kiwiClicked(self):
        food_name = 'kiwi'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def papayaClicked(self):
        food_name = 'papaya'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def pomegranateClicked(self):
        food_name = 'pomegranate'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def quinceClicked(self):
        food_name = 'quince'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def raspberryClicked(self):
        food_name = 'raspberry'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def tomatoClicked(self):
        food_name = 'tomato'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def guavaClicked(self):
        food_name = 'guava'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def zucchiniClicked(self):
        food_name = 'zucchini'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")

    def grapefruitClicked(self):
        food_name = 'grapefruit'
        nutrients = self.get_nutrition_info(food_name)

        if nutrients:
            result_text = "\n".join([f"{nutrient['title']}: {nutrient['amount']} {nutrient['unit']}" for nutrient in nutrients])

            # Check if the table window is already open
            if self.table_window:
                # Destroy the existing table window
                self.table_window.destroy()

            # Create a new table window
            self.create_table_window(nutrients)

        else:
            messagebox.showerror("Error", f"Failed to retrieve nutrition information for {food_name}")
      
    def reset_ui(self):
        #Reset UI when going back
        self.fruit_tab_opened = False
        self.secondtab_opened = False
        self.thirdtab_opened = False
        self.fourthtab_opened = False
        self.fifthtab_opened = False

        for widget in self.additional_widgets:
            widget.destroy()
        self.additional_widgets = []
        self.heading_label.destroy()
        self.input_label.destroy()
        self.button_label1.destroy()
        self.button_label2.destroy()
        self.button_label3.destroy()
        self.button_label4.destroy()
        self.button_label5.destroy()
        self.button_label6.destroy()
        self.button_label7.destroy()
        self.button_label8.destroy()
        self.button_label9.destroy()
        self.button_label10.destroy()
        self.button_label11.destroy()
        self.button_label12.destroy()
        self.button_label13.destroy()
        self.button_label14.destroy()
        self.button_label15.destroy()
        self.button_label16.destroy()
        self.button_label17.destroy()
        self.button_label18.destroy()
        self.button_label19.destroy()
        self.button_label20.destroy()
        self.button_label21.destroy()
        self.button_label22.destroy()
        self.button_label23.destroy()
        self.button_label24.destroy()
        self.button_label25.destroy()
        self.button_label26.destroy()
        self.button_label27.destroy()
        self.button_label28.destroy()
        self.button_label29.destroy()
        self.button_label30.destroy()

        self.right_label.config(text = self.original_label_text)


    def run(self):
        #Run the Tkinter main loop
        self.root.mainloop()

  