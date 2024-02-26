from PIL import Image,ImageTk
import tkinter as tk
import os
from tkinter import ttk, messagebox,PhotoImage,Label
import requests
import webbrowser
class Bhakalo:
    def __init__(self):
        #Initialize the Tkinter Root Window
        self.root = tk.Tk()
        self.screen_width = 1900
        self.screen_height= 1000
        self.root.title("Bhakalo Fruit Shop")

        self.cart = {}
        self.fruitprices = {
            "Apple": 220, "Banana": 40, "Cherry": 600, "Dragon Fruit": 300, "Gooseberry": 220, "Jack Fruit": 170,
            "Lemon": 85, "Mango": 100, "Orange": 70, "Pineapple": 60, "Strawberry": 400, "Watermelon": 90, "Quince": 525,
            "Tomato": 40, "Zucchini": 120, "Custardapple": 140, "Kiwi": 300, "Pomegranate": 110, "Blackberry": 1500,
            "Grapes": 80, "Pear": 180, "Avocado": 250, "Lychee": 275, "Blueberry": 750, "Muskmelon": 52, "Papaya": 90,
            "Peach": 630, "Guava": 115, "Grapefruit": 129, "Raspberry": 150
        }
        
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.configure(bg = "#192f44")
        self.original_label_text = "Welcome to Bhakalo"
        #Setup the UI components
        self.setup_ui()
        self.table_window = None
        self.table_label = None
        self.label7 = None
        self.fruit_tab()


        
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
            self.button_nextpage.place(x=1000,y=675,anchor='nw')         

            self.fruit_tab_opened = True

            #Create buttons for differnt fruits

            #Apple
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
            self.label1.bind("<Button-1>", self.appleClicked)

            self.button_label1 = ttk.Button(self.right_frame, text="Apple - ₹220/kg", style="Rounded.TButton", command=lambda f="Apple", p=220: self.cart_tab(f, p))
            self.button_label1.pack()
            self.button_label1.place(x=105, y=340, anchor='nw')


            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image1 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image1)
            self.l1 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l1.image_types = img
            self.l1.pack()
            self.l1.place(x=275, y=340, anchor="nw")
            self.l1.bind("<Button-1>", self.show_cart)

            #Banana
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
            self.label2.bind("<Button-1>", self.bananaClicked)

            self.button_label2 = ttk.Button(self.right_frame,text ="Banana 40₹/dozen", style="Rounded.TButton",command=lambda f="Banana", p=40: self.cart_tab(f, p))
            self.button_label2.pack()
            self.button_label2.place(x=425,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image2 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image2)
            self.l2 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l2.image_types = img
            self.l2.pack()
            self.l2.place(x=600, y=340, anchor="nw")
            
            #cherry
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
            self.label3.bind("<Button-1>", self.cherryClicked)

            self.button_label3 = ttk.Button(self.right_frame,text="Cherry 600₹/kg", style="Rounded.TButton",command=lambda f="Cherry", p=600: self.cart_tab(f, p))
            self.button_label3.pack()
            self.button_label3.place(x=750,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image3 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image3)
            self.l3 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l3.image_types = img
            self.l3.pack()
            self.l3.place(x=925, y=340, anchor="nw")

            #Dragon Fruit
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
            self.label4.bind("<Button-1>", self.dragonfruitClicked)

            self.button_label4 = ttk.Button(self.right_frame,text="Dragon Fruit 300₹/kg", style="Rounded.TButton",command=lambda f="Dragon Fruit", p=300: self.cart_tab(f, p))
            self.button_label4.pack()
            self.button_label4.place(x=100,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image4 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image4)
            self.l4 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l4.image_types = img
            self.l4.pack()
            self.l4.place(x=275, y=600, anchor="nw")
            

            #Gooseberry
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
            self.label5.bind("<Button-1>", self.gooseberryClicked)

            self.button_label5 = ttk.Button(self.right_frame,text='Gooseberry 220₹/kg', style="Rounded.TButton",command=lambda f="Gooseberry", p=220: self.cart_tab(f, p))
            self.button_label5.pack()
            self.button_label5.place(x=425,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image5 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image5)
            self.l5 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l5.image_types = img
            self.l5.pack()
            self.l5.place(x=600, y=600, anchor="nw")


            #Jackfruit
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
            self.label6.bind("<Button-1>", self.jackfruitClicked)

            self.button_label6 = ttk.Button(self.right_frame,text="Jackfruit 170₹/kg", style="Rounded.TButton",command=lambda f="Jackfruit", p=170: self.cart_tab(f, p))
            self.button_label6.pack()
            self.button_label6.place(x=750,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image6 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image6)
            self.l6 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l6.image_types = img
            self.l6.pack()
            self.l6.place(x=925, y=600, anchor="nw")
            
    def reset_first_tab(self):
            self.firsttab_opened = False
            if self.label1 is not None:
                self.label1.config(image='')
                self.label1.image = None
            if self.label2 is not None:
                self.label2.config(image='')
                self.label2.image = None
            if self.label3 is not None:
                self.label3.config(image='')
                self.label3.image = None
            if self.label4 is not None:
                self.label4.config(image='')
                self.label4.image = None
            if self.label5 is not None:
                self.label5.config(image='')
                self.label5.image = None    
            if self.label6 is not None:
                self.label6.config(image='')
                self.label6.image = None
#cart image clear
            if self.l1 is not None:
                self.l1.config(image='')
                self.l1.image = None

            self.button_label1.destroy()
            self.button_label2.destroy()
            self.button_label3.destroy()
            self.button_label4.destroy()
            self.button_label5.destroy()
            self.button_label6.destroy()    

    def secondtab(self):
        #Show Font Library tab
        self.reset_first_tab()
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
            self.button_nextpage.place(x=1000,y=675,anchor='nw')         

            self.secondtab_opened = True

            #Create buttons for different fruits
            #Lemon
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
            self.label7.bind("<Button-1>", self.lemonClicked)
        
            self.button_label7 = ttk.Button(self.right_frame,text ="Lemon 85₹/kg", style="Rounded.TButton",command=lambda f="Lemon", p=85: self.cart_tab(f, p))
            self.button_label7.pack()
            self.button_label7.place(x=100,y=340,anchor='nw')


            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image7 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image7)
            self.l7 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l7.image_types = img
            self.l7.pack()
            self.l7.place(x=275, y=340, anchor="nw")



            #Mango
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
            self.label8.bind("<Button-1>", self.mangoClicked)

            self.button_label8 = ttk.Button(self.right_frame,text ="Mango 100₹/kg", style="Rounded.TButton",command=lambda f="Mango", p=100: self.cart_tab(f, p))
            self.button_label8.pack()
            self.button_label8.place(x=425,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image8 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image8)
            self.l8 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l8.image_types = img
            self.l8.pack()
            self.l8.place(x=600, y=340, anchor="nw")


            #Orange
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
            self.label9.bind("<Button-1>", self.orangeClicked)

            self.button_label9 = ttk.Button(self.right_frame,text="Orange 70₹/kg", style="Rounded.TButton",command=lambda f="Orange", p=70: self.cart_tab(f, p))
            self.button_label9.pack()
            self.button_label9.place(x=750,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image9 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image9)
            self.l9 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l9.image_types = img
            self.l9.pack()
            self.l9.place(x=925, y=340, anchor="nw")

            #pineapple
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
            self.label10.bind("<Button-1>", self.pineappleClicked)

            self.button_label10 = ttk.Button(self.right_frame,text="Pineapple 60₹/kg", style="Rounded.TButton",command=lambda f="Pineapple", p=60: self.cart_tab(f, p))
            self.button_label10.pack()
            self.button_label10.place(x=100,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image10 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image10)
            self.l10 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l10.image_types = img
            self.l10.pack()
            self.l10.place(x=275, y=600, anchor="nw")

            #Strawberry
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
            self.label11.bind("<Button-1>", self.strawberryClicked)

            self.button_label11 = ttk.Button(self.right_frame,text='Strawberry 400₹/kg', style="Rounded.TButton",command=lambda f="Strawberry", p=400: self.cart_tab(f, p))
            self.button_label11.pack()
            self.button_label11.place(x=425,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image11 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image11)
            self.l11 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l11.image_types = img
            self.l11.pack()
            self.l11.place(x=600, y=600, anchor="nw")


            #Watermelon
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
            self.label12.bind("<Button-1>", self.watermelonClicked)

            self.button_label12 = ttk.Button(self.right_frame,text="Watermelon 90₹/kg", style="Rounded.TButton",command=lambda f="Watermelon", p=90: self.cart_tab(f, p))
            self.button_label12.pack()
            self.button_label12.place(x=750,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image12 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image12)
            self.l12 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l12.image_types = img
            self.l12.pack()
            self.l12.place(x=925, y=600, anchor="nw")
            
    def reset_secondtab(self):
        self.reset_first_tab()
        self.secondtab_opened = False
        if self.label7 is not None:
            self.label7.config(image='')
            self.label7.image = None
        if self.label8 is not None:
            self.label8.config(image='')
            self.label8.image = None
        if self.label9 is not None:
            self.label9.config(image='')
            self.label9.image = None
        if self.label10 is not None:
            self.label10.config(image='')
            self.label10.image = None 
        if self.label11 is not None:
            self.label11.config(image='')
            self.label11.image = None
        if self.label12 is not None:
            self.label12.config(image='')
            self.label12.image = None
        self.button_label7.destroy()
        self.button_label8.destroy()
        self.button_label9.destroy()
        self.button_label10.destroy()
        self.button_label11.destroy()    
        self.button_label12.destroy()

    def thirdtab(self):
        self.reset_secondtab()
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
            self.button_nextpage.place(x=1000,y=675,anchor='nw')         

            self.thirdtab_opened = True

            #Create buttons for different fruits
            #Quince
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
            self.label13.bind("<Button-1>", self.quinceClicked)

            self.button_label13 = ttk.Button(self.right_frame,text ="Quince 525₹/kg", style="Rounded.TButton",command=lambda f="Quince", p=525: self.cart_tab(f, p))
            self.button_label13.pack()
            self.button_label13.place(x=100,y=340,anchor='nw')
            
            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image13 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image13)
            self.l13 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l13.image_types = img
            self.l13.pack()
            self.l13.place(x=275, y=340, anchor="nw")

             #Tomato   
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
            self.label14.bind("<Button-1>", self.tomatoClicked)

            self.button_label14 = ttk.Button(self.right_frame,text ="Tomato 40₹/kg", style="Rounded.TButton",command=lambda f="Tomato", p=40: self.cart_tab(f, p))
            self.button_label14.pack()
            self.button_label14.place(x=425,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image14 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image14)
            self.l14 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l14.image_types = img
            self.l14.pack()
            self.l14.place(x=600, y=340, anchor="nw")

            #Zucchini
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
            self.label15.bind("<Button-1>", self.zucchiniClicked)

            self.button_label15 = ttk.Button(self.right_frame,text="Zucchini 120₹/kg", style="Rounded.TButton",command=lambda f="Zucchini", p=120: self.cart_tab(f, p))
            self.button_label15.pack()
            self.button_label15.place(x=750,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image15 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image15)
            self.l15 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l15.image_types = img
            self.l15.pack()
            self.l15.place(x=925, y=340, anchor="nw")


            #Custardapple
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
            self.label16.bind("<Button-1>", self.custardappleClicked)

            self.button_label16 = ttk.Button(self.right_frame,text="Custardapple 140₹/kg", style="Rounded.TButton",command=lambda f="Custardapple", p=140: self.cart_tab(f, p))
            self.button_label16.pack()
            self.button_label16.place(x=100,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image16 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image16)
            self.l16 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l16.image_types = img
            self.l16.pack()
            self.l16.place(x=275, y=600, anchor="nw")

            #   Kiwi
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
            self.label17.bind("<Button-1>", self.kiwiClicked)

            self.button_label17 = ttk.Button(self.right_frame,text='Kiwi 300₹/kg', style="Rounded.TButton",command=lambda f="Kiwi", p=300: self.cart_tab(f, p))
            self.button_label17.pack()
            self.button_label17.place(x=425,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image17 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image17)
            self.l17 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l17.image_types = img
            self.l17.pack()
            self.l17.place(x=600, y=600, anchor="nw")

            #Pomegranate
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
            self.label18.bind("<Button-1>", self.pomegranateClicked)


            self.button_label18 = ttk.Button(self.right_frame,text="Pomegranate 110₹/kg", style="Rounded.TButton",command=lambda f="Pomegranate", p=110: self.cart_tab(f, p))
            self.button_label18.pack()
            self.button_label18.place(x=750,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image18 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image18)
            self.l18 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l18.image_types = img
            self.l18.pack()
            self.l18.place(x=925, y=600, anchor="nw")
    #this is method for 4> to remove first 3 tabs
    def reset_thirdtab(self):
        self.thirdtab_opened = False
        self.reset_first_tab()
        
        self.reset_secondtab()
        if self.label13 is not None:
            self.label13.config(image='')
            self.label13.image = None  
        if self.label14 is not None:
            self.label14.config(image='')
            self.label14.image = None
        if self.label15 is not None:
            self.label15.config(image='')
            self.label15.image = None
        if self.label16 is not None:
            self.label16.config(image='')
            self.label16.image = None
        if self.label17 is not None:
            self.label17.config(image='')
            self.label17.image = None
        if self.label18 is not None:
            self.label18.config(image='')
            self.label18.image = None                         
        self.button_label13.destroy()
        self.button_label14.destroy()
        self.button_label15.destroy()
        self.button_label16.destroy()
        self.button_label17.destroy()
        self.button_label18.destroy()


    def fourthtab(self):
        self.reset_thirdtab()
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
            self.button_nextpage.place(x=1000,y=675,anchor='nw')         

            self.fourthtab_opened = True
           
            #Create buttons for different fruits

            #Blackberry
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
            self.label19.bind("<Button-1>", self.blackberryClicked)

            self.button_label19 = ttk.Button(self.right_frame,text ="Blackberry 1500₹/kg", style="Rounded.TButton",command=lambda f="Blackberry", p=1500: self.cart_tab(f, p))
            self.button_label19.pack()
            self.button_label19.place(x=100,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image19 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image19)
            self.l19 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l19.image_types = img
            self.l19.pack()
            self.l19.place(x=275, y=340, anchor="nw")



            #Grapes
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
            self.label20.bind("<Button-1>", self.grapesClicked)

            self.button_label20 = ttk.Button(self.right_frame,text ="Grapes 80₹/kg", style="Rounded.TButton",command=lambda f="Grapes", p=80: self.cart_tab(f, p))
            self.button_label20.pack()
            self.button_label20.place(x=425,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image20 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image20)
            self.l20 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l20.image_types = img
            self.l20.pack()
            self.l20.place(x=600, y=340, anchor="nw")


            #Pear
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
            self.label21.bind("<Button-1>", self.pearClicked)

            self.button_label21 = ttk.Button(self.right_frame,text="Pear 180₹/kg", style="Rounded.TButton",command=lambda f="Pear", p=180: self.cart_tab(f, p))
            self.button_label21.pack()
            self.button_label21.place(x=750,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image21 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image21)
            self.l21 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l21.image_types = img
            self.l21.pack()
            self.l21.place(x=925, y=340, anchor="nw")

            #Avacado
            
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
            self.label22.bind("<Button-1>", self.avacadoClicked)

            self.button_label22 = ttk.Button(self.right_frame,text="Avacado 250₹/kg", style="Rounded.TButton",command=lambda f="Avacado", p=250: self.cart_tab(f, p))
            self.button_label22.pack()
            self.button_label22.place(x=100,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image22 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image22)
            self.l22 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l22.image_types = img
            self.l22.pack()
            self.l22.place(x=275, y=600, anchor="nw")


            # Lichi
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
            self.label23.bind("<Button-1>", self.lichiClicked)

            self.button_label23 = ttk.Button(self.right_frame,text='Lichi 275₹/kg', style="Rounded.TButton",command=lambda f="Lichi", p=275: self.cart_tab(f, p))
            self.button_label23.pack()
            self.button_label23.place(x=425,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image23 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image23)
            self.l23 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l23.image_types = img
            self.l23.pack()
            self.l23.place(x=600, y=600, anchor="nw")



            #Blueberry
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
            self.label24.bind("<Button-1>", self.blueberryClicked)

            self.button_label24 = ttk.Button(self.right_frame,text="Blueberry 750₹/kg", style="Rounded.TButton",command=lambda f="Blueberry", p=750: self.cart_tab(f, p))
            self.button_label24.pack()
            self.button_label24.place(x=750,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image24 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image24)
            self.l24 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l24.image_types = img
            self.l24.pack()
            self.l24.place(x=925, y=600, anchor="nw")
    #this is method for 4> to remove last 4 tabs
    def reset_fourthtab(self):
        self.fourthtab_opened = False
        self.reset_first_tab()
        self.reset_secondtab()
        self.reset_thirdtab()
        if self.label19 is not None:
            self.label19.config(image='')
            self.label19.image = None
        if self.label20 is not None:
                    self.label20.config(image='')
                    self.label20.image = None           
        if self.label21 is not None:
                    self.label21.config(image='')
                    self.label21.image = None
        if self.label22 is not None:
                    self.label22.config(image='')
                    self.label22.image = None
        if self.label23 is not None:
                    self.label23.config(image='')
                    self.label23.image = None
        if self.label24 is not None:
                    self.label24.config(image='')
                    self.label24.image = None
        self.button_label19.destroy()
        self.button_label20.destroy()
        self.button_label21.destroy()
        self.button_label22.destroy()
        self.button_label23.destroy()
        self.button_label24.destroy()            


    
    def fifthtab(self):
        self.reset_fourthtab()
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

            
            self.button_nextpage = ttk.Button(self.right_frame,text =" Start Over", style="Rounded.TButton",command=self.fruit_tab)
            self.button_nextpage.pack()
            self.button_nextpage.place(x=1000,y=675,anchor='nw')         

            self.fifthtab_opened = True

            #Create buttons for different fonts
            #Muskmelon
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
            self.label25.bind("<Button-1>", self.muskmelonClicked)

            self.button_label25 = ttk.Button(self.right_frame,text ="Muskmelon 52₹/kg", style="Rounded.TButton",command=lambda f="Muskmelon", p=52: self.cart_tab(f, p))
            self.button_label25.pack()
            self.button_label25.place(x=100,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image25 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image25)
            self.l25 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l25.image_types = img
            self.l25.pack()
            self.l25.place(x=275, y=340, anchor="nw")


            #Papaya
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
            self.label26.bind("<Button-1>", self.papayaClicked)

            self.button_label26 = ttk.Button(self.right_frame,text ="Papaya 90₹/kg", style="Rounded.TButton",command=lambda f="Papaya", p=90: self.cart_tab(f, p))
            self.button_label26.pack()
            self.button_label26.place(x=425,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image26 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image26)
            self.l26 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l26.image_types = img
            self.l26.pack()
            self.l26.place(x=600, y=340, anchor="nw")


            #Peach
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
            self.label27.bind("<Button-1>", self.peachClicked)

            self.button_label27 = ttk.Button(self.right_frame,text="Peach 630₹/kg", style="Rounded.TButton",command=lambda f="Peach", p=630: self.cart_tab(f, p))
            self.button_label27.pack()
            self.button_label27.place(x=750,y=340,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image27 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image27)
            self.l27 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l27.image_types = img
            self.l27.pack()
            self.l27.place(x=925, y=340, anchor="nw")


            #Gauva
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
            self.label28.bind("<Button-1>", self.guavaClicked)

            self.button_label28 = ttk.Button(self.right_frame,text="Gauva 115₹/kg", style="Rounded.TButton",command=lambda f="Gauva", p=115: self.cart_tab(f, p))
            self.button_label28.pack()
            self.button_label28.place(x=100,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image28 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image28)
            self.l28 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l28.image_types = img
            self.l28.pack()
            self.l28.place(x=275, y=600, anchor="nw")


            #Grapefruit
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
            self.label29.bind("<Button-1>", self.grapefruitClicked)

            self.button_label29 = ttk.Button(self.right_frame,text='Grapefruit 129₹/kg', style="Rounded.TButton",command=lambda f="Grapefruit", p=129: self.cart_tab(f, p))
            self.button_label29.pack()
            self.button_label29.place(x=425,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image29 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image29)
            self.l29 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l29.image_types = img
            self.l29.pack()
            self.l29.place(x=600, y=600, anchor="nw")


            #Raspberry
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
            self.label.bind("<Button-1>", self.raspberryClicked)

            self.button_label30 = ttk.Button(self.right_frame,text="Raspberry 150₹/kg", style="Rounded.TButton",command=lambda f="Raspberry", p=150: self.cart_tab(f, p))
            self.button_label30.pack()
            self.button_label30.place(x=750,y=600,anchor='nw')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(script_directory,"../assets/Images/cart.jpg")
            img = ImageTk.PhotoImage(Image.open(img_path))
            original_image = Image.open(img_path)
            image30 = original_image.resize((40, 40))  
            img = ImageTk.PhotoImage(image30)
            self.l30 = tk.Label(self.right_frame, image=img, background="#fffce9")
            self.l30.image_types = img
            self.l30.pack()
            self.l30.place(x=925, y=600, anchor="nw") 
   
    def reset_fifthtab(self):
        self.fifthtab_opened = False
        self.reset_first_tab()
        self.reset_secondtab()
        self.reset_thirdtab()
        self.reset_fourthtab()
        
        if self.label25 is not None:
                        self.label25.config(image='')
                        self.label25.image = None
        if self.label26 is not None:
                        self.label26.config(image='')
                        self.label26.image = None                       
        if self.label27 is not None:
                        self.label27.config(image='')
                        self.label27.image = None        
        if self.label28 is not None:
                        self.label28.config(image='')
                        self.label28.image = None
        if self.label29 is not None:
                        self.label29.config(image='')
                        self.label29.image = None
        if self.label30 is not None:
                        self.label30.config(image='')
                        self.label30.image = None
        self.button_label25.destroy()
        self.button_label26.destroy()
        self.button_label27.destroy()
        self.button_label28.destroy()
        self.button_label29.destroy()
        self.button_label30.destroy()                






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
        self.button_label = ttk.Button(self.left_frame,text="My cart", style="Rounded.TButton",command=self.show_cart)
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
        self.back_button = ttk.Button(self.left_frame,text="Back",style="Rounded.TButton",command=self.reset_fifthtab)
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
        self.bt1 = ttk.Button(self.right_frame,text ="Your Information", style="Rounded.TButton")
        self.bt1.pack()
        self.bt1.place(x=150,y=100,anchor='nw')

        self.bt2 = ttk.Button(self.right_frame,text ="Your Orders", style="Rounded.TButton")
        self.bt2.pack()
        self.bt2.place(x=600,y=100,anchor='nw')

        self.bt3 = ttk.Button(self.right_frame,text ="Buy Again ", style="Rounded.TButton")
        self.bt3.pack()
        self.bt3.place(x=150,y=200,anchor='nw')

        self.bt4 = ttk.Button(self.right_frame,text ="Your Rewards", style="Rounded.TButton")
        self.bt4.pack()
        self.bt4.place(x=600,y=200,anchor='nw')

        self.bt5 = ttk.Button(self.right_frame,text ="See all", style="Rounded.TButton")
        self.bt5.pack()
        self.bt5.place(x=150,y=300,anchor='nw')
        self.reset_ui()
    def destroy_myAccount(self,event=None):
        self.bt1.destroy()
        self.bt2.destroy()
        self.bt3.destroy()
        self.bt4.destroy()
            
    def cart_tab(self,food_name,price):
        quantity = self.cart.get(food_name, 0) + 1
        self.cart[food_name] = quantity
        messagebox.showinfo("Added to Cart", f"{food_name} added to the cart!")

    def show_cart(self):
        if not self.cart:
            messagebox.showinfo("Cart", "Cart is empty.")
            return

        cart_content = ""
        total_price = 0

        for food_name, quantity in self.cart.items():
            price = self.fruitprices.get(food_name, 0)
            total_price += price * quantity
            cart_content += f"{food_name} - Quantity: {quantity} - Price: ₹{price * quantity:.2f}/kg\n"

        cart_content += f"\nTotal Bill: ₹{total_price:.2f}"

        messagebox.showinfo("Cart", cart_content)    
    def ourblogs_tab(self):
          
        # Replace "https://www.example.com/ourblogs" with your actual link
        link = "https://www.fruit-forest.com/blog"
        
        # Open the link in the default web browser
        webbrowser.open(link)
        
        
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

    def appleClicked(self,event=None):
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

    
    def bananaClicked(self,event=None):
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

    
        
    def cherryClicked(self,event=None):
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

    

    def dragonfruitClicked(self,event=None):
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

    def gooseberryClicked(self,event=None):
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

    def jackfruitClicked(self,event=None):
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

    def lemonClicked(self,event=None):
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

    def mangoClicked(self,event=None):
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

    def orangeClicked(self,event=None):
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

    def pineappleClicked(self,event=None):
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

    def strawberryClicked(self,event=None):
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

    def watermelonClicked(self,event=None):
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

    def grapesClicked(self,event=None):
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

    def blackberryClicked(self,event=None):
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

    def custardappleClicked(self,event=None):
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

    def muskmelonClicked(self,event=None):
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

    def avacadoClicked(self,event=None):
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

    def pearClicked(self,event=None):
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

    def peachClicked(self,event=None):
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

    def lichiClicked(self,event=None):
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

    def blueberryClicked(self,event=None):
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

    def kiwiClicked(self,event=None):
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
 

    def papayaClicked(self,event=None):
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

    def pomegranateClicked(self,event=None):
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

    def quinceClicked(self,event=None):
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

    def raspberryClicked(self,event=None):
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

    def tomatoClicked(self,event=None):
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

    def guavaClicked(self,event=None):
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

    def zucchiniClicked(self,event=None):
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

    def grapefruitClicked(self,event=None):
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
        self.reset_images()
        self.reset_buttons()
        self.reset_labels()
        self.reset_fifthtab()
        for widget in self.additional_widgets:
            widget.destroy()
        self.additional_widgets = []
        self.heading_label.destroy()
        self.input_label.destroy()

        # Reset the entire UI by calling individual reset methods
        self.fruit_tab_opened = False
        self.secondtab_opened = False
        self.thirdtab_opened = False
        self.fourthtab_opened = False
        self.fifthtab_opened = False
        
    def run(self):
        #Run the Tkinter main loop
        self.root.mainloop()

  