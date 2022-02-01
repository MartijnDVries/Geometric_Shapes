import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import math


class Screens(tk.Toplevel):
    
    def __init__(self):
        """Create a toplevel window with a grid configuration""" 
        super().__init__()
        self.geometry("800x650+279+0")
        col_count = 65
        row_count = 80
        for col in range(col_count):
            self.grid_columnconfigure(col, minsize=10)
        for row in range(row_count):
            self.grid_rowconfigure(row, minsize=10)
            
    def destroy_screen(self, page):
        """destroy the toplevel window and go back to the main screen"""
        self.destroy()
        App(page)
        
        
class Scroll():
            
    def scroll_forward(page,btn_1=0,btn_2=0,btn_3=0,btn_4=0,btn_5=0,btn_6=0,btn_7=0,btn_8=0,btn_9=0,btn_10=0,next_btn=0, prev_btn=0):
        """Scroll to the next page in main menu"""
        if page == 1:
            btn_1.destroy()
            btn_2.destroy()
            btn_3.destroy()
            btn_4.destroy()
            next_btn.destroy()
            App(page=2)
        if page == 2:
            btn_5.destroy()
            btn_6.destroy()
            btn_7.destroy()
            btn_8.destroy()
            next_btn.destroy()
            prev_btn.destroy()
            App(page=3)

    def scroll_backward(page,btn_1=0,btn_2=0,btn_3=0,btn_4=0,btn_5=0,btn_6=0,btn_7=0,btn_8=0,btn_9=0,btn_10=0,next_btn=0, prev_btn=0):
        """Scroll to previous page in main menu"""
        if page == 2:
            btn_5.destroy()
            btn_6.destroy()
            btn_7.destroy()
            btn_8.destroy()
            next_btn.destroy()
            App(page=1)
        if page== 3:
            btn_9.destroy()
            btn_10.destroy()
            App(page=2)

        
class App(tk.Tk):
    
    def __init__(self, page):
        """Create the main window dependent on given page"""
        super().__init__()
        self.overrideredirect(True)
        self.withdraw()
        
        #check if window already exists
        global pages_root
        try:
            value = tk.Toplevel.winfo_exists(pages_root)
            if value == 0:
                pages_root = tk.Toplevel()
            if value == 1:
                pass
        except NameError:
            pages_root =  tk.Toplevel()
            pages_root.geometry("1158x650+100+0")
            
        #Setup grid (50x50)
        col_counter = 23
        row_counter = 15
        for col in range(col_counter):
            pages_root.grid_columnconfigure(col, minsize=50)
        for row in range(row_counter):
            pages_root.grid_rowconfigure(row, minsize=50)

        path = r"C:\Geometric-Shapes\images"

        #Load images from path
        global img
        img = ImageTk.PhotoImage(Image.open(\
        path+r"\square_button.png"))
        global img2
        img2 = ImageTk.PhotoImage(Image.open(\
        path+"\cirkel_button2.png"))
        global img3
        img3 = ImageTk.PhotoImage(Image.open(\
        path+r"\triangle_button.png"))
        global img4
        img4 = ImageTk.PhotoImage(Image.open(\
        path+"\pythagoras_triangle_button.png"))
        global img5
        img5 = ImageTk.PhotoImage(Image.open(\
        path+"\kite_button.png"))
        global img6
        img6 = ImageTk.PhotoImage(Image.open(\
        path+"\cube_button.png"))
        global img7
        img7 = ImageTk.PhotoImage(Image.open(\
        path+"\cilinder_button.png"))
        global img8
        img8 = ImageTk.PhotoImage(Image.open(\
        path+"\pyramid_button.png"))
        global img9
        img9 = ImageTk.PhotoImage(Image.open(\
        path+"\parallel_button.png"))
        global img10
        img10 = ImageTk.PhotoImage(Image.open(\
        path+r"\trapezoid_button.png"))
        global next_image
        next_image = ImageTk.PhotoImage(Image.open(\
        path+r"\arrow_forward.png"))
        global previous_image
        previous_image = ImageTk.PhotoImage(Image.open(\
        path+r"\arrow_previous.png"))
        

        #Load images in buttons & other specifics of the button
        if page == 1:
            btn_1 =  tk.Button(pages_root, image=img, relief="raised",
                width=196, height=200, command=lambda:App.square_screen())
            btn_2 = tk.Button(pages_root, image=img2, relief="raised", 
                width=196, height=200, command=lambda:App.cirkel_screen())
            btn_3 = tk.Button(pages_root, image=img3, relief="raised", 
                width=196, height=200, command=lambda:App.triangle_screen())
            btn_4 = tk.Button(pages_root, image=img4, relief="raised",
                width=196, height=200, command=lambda:App.pyth_triangle_screen())
            btn_5 =0
            btn_6 =0
            btn_7 =0
            btn_8 =0
            btn_9 =0
            btn_10 =0
            prev_btn=0
            next_btn = tk.Button(pages_root, image=next_image, borderwidth=0, 
                command=lambda:Scroll.scroll_forward(1,btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_10,next_btn,prev_btn))
                
        elif page ==2:
            btn_5 =  tk.Button(pages_root, image = img5, relief = "raised",
                width=196, height=200, command=lambda:App.kite_screen())
            btn_6 = tk.Button(pages_root, image =  img6, relief = "raised",
                width=196, height=200, command=lambda:App.cube_screen())
            btn_7 = tk.Button(pages_root, image =  img7, relief = "raised", 
                width=196, height=200, command=lambda:App.cilinder_screen())
            btn_8 = tk.Button(pages_root, image =  img8, relief = "raised",
                width=196, height=200, command=lambda:App.pyramid_screen())
            btn_1 =0
            btn_2 =0
            btn_3 =0
            btn_4 =0
            btn_9 =0
            btn_10 =0
            next_btn = tk.Button(pages_root, image=next_image, borderwidth=0, 
                command=lambda:Scroll.scroll_forward(2,btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_10,next_btn,prev_btn))
            prev_btn = tk.Button(pages_root, image=previous_image, borderwidth=0, 
                command=lambda:Scroll.scroll_backward(2,btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_10,next_btn,prev_btn))
                
        elif page ==3:
            btn_9 =  tk.Button(pages_root, image=img9, relief="raised", width=196,
                height=200, command=lambda:App.parallel_screen())
            btn_10 = tk.Button(pages_root, image=img10, relief="raised", width=196,
                height=200, command=lambda:App.trapezoid_screen())
            btn_1 =0
            btn_2 =0
            btn_3 =0
            btn_4 =0
            btn_5 =0
            btn_6 =0
            btn_7 =0
            btn_8 =0
            next_btn =0
            prev_btn = tk.Button(pages_root, image=previous_image, borderwidth=0, 
                command=lambda:Scroll.scroll_backward(3,btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_10,next_btn,prev_btn))
                

        #place buttons in grid
        if page ==1:
            btn_1.grid(row=5, column=2, columnspan=4, rowspan=4)
            btn_2.grid(row=5, column=7, columnspan=4, rowspan=4)
            btn_3.grid(row=5, column=12, columnspan=4, rowspan=4)
            btn_4.grid(row=5, column=17, columnspan=4, rowspan=4)
            next_btn.grid(row=10, column=20, columnspan=3, rowspan=3)
            
        if page ==2:
            btn_5.grid(row=5, column=2, columnspan=4, rowspan=4)
            btn_6.grid(row=5, column=7, columnspan=4, rowspan=4)
            btn_7.grid(row=5, column=12, columnspan=4, rowspan=4)
            btn_8.grid(row=5, column=17, columnspan=4, rowspan=4)
            next_btn.grid(row=10, column=20, columnspan=3, rowspan=3)
            prev_btn.grid(row=10, column=0, columnspan=3, rowspan=3)
            
        if page ==3:
            btn_9.grid(row=5, column=2, columnspan=4, rowspan=4)
            btn_10.grid(row=5, column=7, columnspan=4, rowspan=4)
            prev_btn.grid(row=10, column=0, columnspan=3, rowspan=3)
            

    def cirkel_screen():
        """opens the screen to input cirkel values"""
            #Destroy old window
        global pages_root
        pages_root.destroy()
            #Create new specific window
        cirkel_root = Screens()
            #load cirkel image from path
        path = r"C:\Geometric-Shapes\images"
        global big_cirkel
        big_cirkel = ImageTk.PhotoImage(Image.open(path+"\cirkel_s_blanc.png"))
        
            #Create widgets
        back_button = tk.Button(cirkel_root, width=6, text="Back", 
            relief="raised", command=lambda:cirkel_root.destroy_screen(page=1))
        diameter_l= tk.Label(cirkel_root,width=14, height=1, text="Diameter:", 
            font=("Arial",16), relief="raised")
        diameter = tk.StringVar()
        diameter_entry= tk.Entry(cirkel_root, width=6, textvariable=diameter)
        area_l = tk.Label(cirkel_root,width=14, height=1, text="Area:", 
            font=("Arial",16), relief="raised")
        area_entry = tk.Label(cirkel_root, width=6, relief="sunken", bg="white")
        circumference_l = tk.Label(cirkel_root,width=14, height=1,
            text="Circumference:", font=("Arial",16), relief="raised")
        circumference_entry =  tk.Label(cirkel_root, width=6, relief="sunken",
            bg="white")
        cirkel_canvas = tk.Canvas(cirkel_root, height=530, width=530)
        image = cirkel_canvas.create_image(0,0,anchor='nw', image=big_cirkel)
      
            #Create mousehover events definitions      
        def on_enter_dia(e):
            global line_c
            line_c = cirkel_canvas.create_line(38,259,489,259, width=5, 
                fill="yellow")
        
        def on_leave_dia(e):
            global line_c
            cirkel_canvas.after(0, cirkel_canvas.delete, line_c)
            
        def on_enter_ar(e):
            global fill_ar
            fill_ar = cirkel_canvas.create_oval(37,32,489,490, fill="yellow")
        
        def on_leave_ar(e):
            global fill_ar
            cirkel_canvas.after(0, cirkel_canvas.delete, fill_ar)
        
        def on_enter_cir(e):
            global cir_c
            cir_c = cirkel_canvas.create_oval(35,30,491,492, outline="yellow",
                width=7)
                
        def on_leave_cir(e):
            global cir_c
            cirkel_canvas.after(0, cirkel_canvas.delete, cir_c)
            
            #Bind events to widgets
        diameter_l.bind("<Enter>", on_enter_dia)
        diameter_l.bind("<Leave>", on_leave_dia)
        area_l.bind("<Enter>", on_enter_ar)
        area_l.bind("<Leave>", on_leave_ar)
        circumference_l.bind("<Enter>", on_enter_cir)
        circumference_l.bind("<Leave>", on_leave_cir)
        
            #Place wigets in grid
        back_button.grid(row = 1, column=3, columnspan=6)
        cirkel_canvas.grid(row=2, column=3, columnspan=53, rowspan=53)
        diameter_l.grid(row=11, column=57, rowspan=1, columnspan=1)
        diameter_entry.grid(row=11, column=58)
        area_l.grid(row=45, column=57, rowspan=1, columnspan=1)
        area_entry.grid(row=45, column=58)
        circumference_l.grid(row=49, column=57, rowspan=1, columnspan=1)
        circumference_entry.grid(row=49, column=58)
        
        def assign_1(*args):
            """get the number input from entry and output calculated answers"""
            try:
                dia = float(diameter.get())
                circ =(str(math.pi*float(dia)))
                area = (1/4)*math.pi*float(dia**2)
            except ValueError:
                area = str(0)
                circ = str(0)
            circumference_entry.config(text=(App.check_lastchar(str(circ))))
            area_entry.config(text=(App.check_lastchar(str(area))))

        diameter.trace('w', assign_1)
        
    def square_screen():
        """Opens screen to input square values (and calculate answers)"""
            #Destroy old window
        global pages_root
        pages_root.destroy()
            #Create new specific window
        square_root = Screens()

            #Create widgets
        square_canvas = tk.Canvas(square_root, height=530, width=530, bg="white")
        back_button = tk.Button(square_root, width=6, text="Back", 
            relief="raised", command=lambda:square_root.destroy_screen(page=1))
        perimeter_l = tk.Label(square_root, height=1, width=14, relief="raised",
            text="Perimeter", font=("Arial",16))
        perimeter_entry = tk.Label(square_root, width=6, relief="sunken", 
            bg="white")
        area_l = tk.Label(square_root, height=1, width=14, relief="raised",
            text="Area", font=("Arial",16))
        area_entry = tk.Label(square_root, width=6, relief="sunken", 
            bg="white")
        height_l = tk.Label(square_root, height=1, width=14, relief="raised",
            text="Height", font=("Arial",16))
        height = tk.StringVar()
        height_entry = tk.Entry(square_root, width=6, textvariable=height)
        width_l = tk.Label(square_root, height=1, width=14, relief="raised",
            text="Width", font=("Arial",16))
        width = tk.StringVar()
        width_entry = tk.Entry(square_root, width=6, textvariable=width)
        
            #create mouse hover events
        def on_enter_he(e):
            global h
            h = square_canvas.create_line(35, 28, 35, 493, fill="yellow", width=7)
        def on_leave_he(e):
            global h
            square_canvas.after(0, square_canvas.delete, h)
        def on_enter_wi(e):
            global w
            w =  square_canvas.create_line(33,490, 493,490,
                fill="yellow", width=7)
        def on_leave_wi(e):
            global w
            square_canvas.after(0, square_canvas.delete, w)
        def on_enter_ar(e):
            global ar
            global squareline1
            global squareline1_2
            global squareline2
            global squareline2_2
            global square_corner1_1
            ar = square_canvas.create_polygon(38,33, 488,32, 488,488, 38,488, 
                fill="yellow")
            squareline1 = square_canvas.create_line(25,248,45,248, width=5)
            squareline1_2 = square_canvas.create_line(25,268,45,268, width=5)
            squareline2 =  square_canvas.create_line(248,480, 248,500, width=5)
            squareline2_2 =  square_canvas.create_line(268,480, 268,500, width=5)
            square_corner1_1 = square_canvas.create_rectangle(37,470, 57,490, width=2)
        def on_leave_ar(e):
            global ar
            global squareline1
            global squareline1_2
            global squareline2
            global squareline2_2
            global square_corner1_1
            square_canvas.after(0, square_canvas.delete, ar)
            square_canvas.after(0, square_canvas.delete, squareline1)
            square_canvas.after(0, square_canvas.delete, squareline1_2)
            square_canvas.after(0, square_canvas.delete, squareline2)
            square_canvas.after(0, square_canvas.delete, squareline2_2)
            square_canvas.after(0, square_canvas.delete, square_corner1_1)
        def on_enter_per(e):
            global per
            global squareline1
            global squareline1_2
            global squareline2
            global squareline2_2
            global square_corner1_1
            per = square_canvas.create_polygon(35,30, 490,30, 490,490, 35,490, 
                outline="yellow", width=7, fill="white")
            squareline1 = square_canvas.create_line(25,248,45,248, width=5)
            squareline1_2 = square_canvas.create_line(25,268,45,268, width=5)
            squareline2 =  square_canvas.create_line(248,480, 248,500, width=5)
            squareline2_2 =  square_canvas.create_line(268,480, 268,500, width=5)
            square_corner1_1 = square_canvas.create_line(39,470, 57,470, width=2)
            square_corner1_2 = square_canvas.create_line(57,470, 57,488, width=2)
        def on_leave_per(e):
            global per
            global squareline1
            global squareline1_2
            global squareline2
            global squareline2_2
            global square_corner1_1
            square_canvas.after(0, square_canvas.delete, per)
            square_canvas.after(0, square_canvas.delete, ar)
            square_canvas.after(0, square_canvas.delete, squareline1)
            square_canvas.after(0, square_canvas.delete, squareline1_2)
            square_canvas.after(0, square_canvas.delete, squareline2)
            square_canvas.after(0, square_canvas.delete, squareline2_2)
            square_canvas.after(0, square_canvas.delete, square_corner1_1)
            
        height_l.bind("<Enter>", on_enter_he)
        height_l.bind("<Leave>", on_leave_he)
        width_l.bind("<Enter>", on_enter_wi)
        width_l.bind("<Leave>", on_leave_wi)
        area_l.bind("<Enter>", on_enter_ar)
        area_l.bind("<Leave>", on_leave_ar)
        perimeter_l.bind("<Enter>", on_enter_per)
        perimeter_l.bind("<Leave>", on_leave_per)
        
            #Place wigets in grid
        back_button.grid(row = 1, column=3, columnspan=6)
        square_canvas.grid(row=2, column=3, columnspan=53, rowspan=53)
        rect = square_canvas.create_polygon(35,30, 490,30, 490,490, 35,490,
            outline="black", fill="white", width=5)
        squareline1 = square_canvas.create_line(25,248,45,248, width=5)
        squareline1_2 = square_canvas.create_line(25,268,45,268, width=5)
        squareline2 =  square_canvas.create_line(248,480, 248,500, width=5)
        squareline2_2 =  square_canvas.create_line(268,480, 268,500, width=5)
        square_corner1_1 = square_canvas.create_rectangle(37,470, 57,490, width=2)
        height_l.grid(row=9, column=57, rowspan=1, columnspan=1)
        height_entry.grid(row=9, column=58)
        width_l.grid(row=13, column=57, rowspan=1, columnspan=1)
        width_entry.grid(row=13, column=58)
        area_l.grid(row=45, column=57, rowspan=1, columnspan=1)
        area_entry.grid(row=45, column=58)
        perimeter_l.grid(row=49, column=57, rowspan=1, columnspan=1)
        perimeter_entry.grid(row=49, column=58)
    
        def assign_2(*args):
            """get the number input from entry and output calculated answers"""
            try:
                he = float(height.get())
                wi = float(width.get())
                area = he*wi
                perimeter = (2*he)+(2*wi)
            except ValueError:
                area = str(0)
                perimeter = str(0)
            perimeter_entry.config(text=(App.check_lastchar(str(perimeter))))
            area_entry.config(text=(App.check_lastchar(str(area))))

        height.trace('w', assign_2)
        width.trace('w', assign_2)
        
    def triangle_screen():
        """Opens screen to input square values (and calculate answers)"""

            #Destroy menu window
        global pages_root
        pages_root.destroy()
        
            #Create new specific window
        triangle_root = Screens()

            #Create widgets
        triangle_canvas = tk.Canvas(triangle_root, height=530, width=530, 
            bg="white")
        back_button = tk.Button(triangle_root, width=6, text="Back", 
            relief="raised", command=lambda:triangle_root.destroy_screen(page=1))
        area_l = tk.Label(triangle_root, height=1, width=14, relief="raised",
            text="Area", font=("Arial",16))
        area_entry = tk.Label(triangle_root, width=6, relief="sunken", 
            bg="white")
        height_l = tk.Label(triangle_root, height=1, width=14, relief="raised",
            text="Height", font=("Arial",16))
        height = tk.StringVar()
        height_entry = tk.Entry(triangle_root, width=6, textvariable=height)
        width_l = tk.Label(triangle_root, height=1, width=14, relief="raised",
            text="Width", font=("Arial",16))
        width = tk.StringVar()
        width_entry = tk.Entry(triangle_root, width=6, textvariable=width)
        
            #create mouse hover events
        def on_enter_he(e):
            global h
            global corner_tria1
            global corner_tria2
            h = triangle_canvas.create_line(263,34, 263,488, fill="yellow",
                width=7)
            corner_tria1 = triangle_canvas.create_line(267,468, 287,468,
                fill="yellow", width=2)
            corner_tria2 = triangle_canvas.create_line(287,468, 287,488,
                fill="yellow", width=2)
        def on_leave_he(e):
            global h
            global corner_tria1
            global corner_tria2
            triangle_canvas.after(0, triangle_canvas.delete, h)
            triangle_canvas.after(0, triangle_canvas.delete, corner_tria1)
            triangle_canvas.after(0, triangle_canvas.delete, corner_tria2)
            
        def on_enter_wi(e):
            global w
            w =  triangle_canvas.create_line(33,490, 493,490,
                fill="yellow", width=7)
        def on_leave_wi(e):
            global w
            triangle_canvas.after(0, triangle_canvas.delete, w)
        def on_enter_ar(e):
            global ar 
            global tria1
            global tria2
            global tria3
            global tria4
            ar = triangle_canvas.create_polygon(263,40, 487,488, 38,488, 
                fill="yellow")
            tria1 = triangle_canvas.create_line(149,234, 173,246, width=5)
            tria2 = triangle_canvas.create_line(139,254, 163,266, width=5)
            tria3 = triangle_canvas.create_line(362,266, 386,254, width=5)
            tria4 = triangle_canvas.create_line(354,246, 378,234, width=5)
        def on_leave_ar(e):
            global ar
            global tria1
            global tria2
            global tria3
            global tria4
            triangle_canvas.after(0, triangle_canvas.delete, ar)
            triangle_canvas.after(0, triangle_canvas.delete, tria1)
            triangle_canvas.after(0, triangle_canvas.delete, tria2)
            triangle_canvas.after(0, triangle_canvas.delete, tria3)
            triangle_canvas.after(0, triangle_canvas.delete, tria4)
            
        height_l.bind("<Enter>", on_enter_he)
        height_l.bind("<Leave>", on_leave_he)
        width_l.bind("<Enter>", on_enter_wi)
        width_l.bind("<Leave>", on_leave_wi)
        area_l.bind("<Enter>", on_enter_ar)
        area_l.bind("<Leave>", on_leave_ar)

            #Place wigets in grid
        back_button.grid(row = 1, column=3, columnspan=6)
        triangle_canvas.grid(row=2, column=3, columnspan=53, rowspan=53)
        tria = triangle_canvas.create_polygon(490,490, 35,490, 263,35,
            outline="black", fill="white", width=5)
        trialine1 = triangle_canvas.create_line(149,234, 173,246, width=5)
        trialine2 = triangle_canvas.create_line(139,254, 163,266, width=5)
        trialine3 = triangle_canvas.create_line(362,266, 386,254, width=5)
        trialine4 = triangle_canvas.create_line(354,246, 378,234, width=5)
        height_l.grid(row=9, column=57, rowspan=1, columnspan=1)
        height_entry.grid(row=9, column=58)
        width_l.grid(row=13, column=57, rowspan=1, columnspan=1)
        width_entry.grid(row=13, column=58)
        area_l.grid(row=45, column=57, rowspan=1, columnspan=1)
        area_entry.grid(row=45, column=58)
        
        def assign_3(*args):
            """get the number input from entry and output calculated answers"""
            try:
                he = float(height.get())
                wi = float(width.get())
                area = float(0.5)*he*wi
            except ValueError:
                area = str(0)
                perimeter = str(0)
            area_entry.config(text=str(App.check_lastchar(str(area))))

        height.trace('w', assign_3)
        width.trace('w', assign_3)
        triangle_root.mainloop()
        
    def pyth_triangle_screen():
        """Opens screen to input pythagoran triangle values 
            (and calculate answers)"""
            #Destroy menu window
        global pages_root
        pages_root.destroy()
        
            #Create new specific window
        global pyth_triangle_root
        pyth_triangle_root = Screens()

            #Create widgets
        pyth_triangle_canvas = tk.Canvas(pyth_triangle_root, height=530, width=530, 
            bg="white")
        back_button = tk.Button(pyth_triangle_root, width=6, text="Back", 
            relief="raised", command=lambda:pyth_triangle_root.destroy_screen(page=1))
        A_l = tk.Label(pyth_triangle_root, height=1, width=6, relief="raised",
            text="A", font=("Arial",16))
        A_l2 = tk.Label(pyth_triangle_root, height=1, width=6, relief="raised",
            text="A", font=("Arial",16))
        A_output = tk.Label(pyth_triangle_root, width=6, relief="sunken", 
            bg="white")
        A = tk.StringVar()
        A_entry =  tk.Entry(pyth_triangle_root, width=6, textvariable=A)
        
        B_l = tk.Label(pyth_triangle_root, height=1, width=6, relief="raised",
            text="B", font=("Arial",16))
        B_l2 = tk.Label(pyth_triangle_root, height=1, width=6, relief="raised",
            text="B", font=("Arial",16))
        B_output = tk.Label(pyth_triangle_root, width=6, relief="sunken", 
            bg="white")
        B = tk.StringVar()
        B_entry = tk.Entry(pyth_triangle_root, width=6, textvariable=B)
        
        C_l = tk.Label(pyth_triangle_root, height=1, width=6, relief="raised",
            text="C", font=("Arial",16))
        C_l2 = tk.Label(pyth_triangle_root, height=1, width=6, relief="raised",
            text="C", font=("Arial",16))
        C_output = tk.Label(pyth_triangle_root, width=6, relief="sunken", 
            bg="white")
        C = tk.StringVar()
        C_entry = tk.Entry(pyth_triangle_root, width=6, textvariable=C)
        
        input_l =  tk.Label(pyth_triangle_root, height=1, width=14,
            relief="raised", text="Input:", font=("Arial",16))
        output_l =  tk.Label(pyth_triangle_root, height=1, width=14,
            relief="raised", text="Output", font=("Arial",16))
        
            #create mouse hover events
        def on_enter_A(e):
            global a
            a = pyth_triangle_canvas.create_line(35, 33, 35, 495, fill="yellow",
                width=7)
        def on_leave_A(e):
            global a
            pyth_triangle_canvas.after(0, pyth_triangle_canvas.delete, a)
        def on_enter_B(e):
            global b
            b =  pyth_triangle_canvas.create_line(33, 492, 494, 492,
                fill="yellow", width=7)
        def on_leave_B(e):
            global b
            pyth_triangle_canvas.after(0, pyth_triangle_canvas.delete, b)
        def on_enter_C(e):
            global c
            c = pyth_triangle_canvas.create_line(33,33,492,495, fill="yellow",
                width=7)
        def on_leave_C(e):
            global c
            pyth_triangle_canvas.after(0, pyth_triangle_canvas.delete, c)
            
        A_l.bind("<Enter>", on_enter_A)
        A_l.bind("<Leave>", on_leave_A)
        B_l.bind("<Enter>", on_enter_B)
        B_l.bind("<Leave>", on_leave_B)
        C_l.bind("<Enter>", on_enter_C)
        C_l.bind("<Leave>", on_leave_C)
        
        A_l2.bind("<Enter>", on_enter_A)
        A_l2.bind("<Leave>", on_leave_A)
        B_l2.bind("<Enter>", on_enter_B)
        B_l2.bind("<Leave>", on_leave_B)
        C_l2.bind("<Enter>", on_enter_C)
        C_l2.bind("<Leave>", on_leave_C)

            #Place wigets in grid
        back_button.grid(row = 1, column=3, columnspan=6, rowspan=4)
        pyth_triangle_canvas.grid(row=2, column=3, columnspan=53, rowspan=53)
        tria = pyth_triangle_canvas.create_polygon(491,492,35,492,35,35,
            outline="black", fill="white", width=5)
        ptria_corn1 = pyth_triangle_canvas.create_line(38,472, 58,472, 
            fill="black", width=2)
        ptria_corn1 = pyth_triangle_canvas.create_line(58,472, 58,492,
            fill="black", width=2)
        input_l.grid(row=10, column=57, rowspan=1, columnspan=1)
        output_l.grid(row=35, column=57, rowspan=1, columnspan=1)
        A_l.grid(row=13, column=57, rowspan=1, columnspan=1)
        A_entry.grid(row=13, column=58)
        B_l.grid(row=17, column=57, rowspan=1, columnspan=1)
        B_entry.grid(row=17, column=58)
        C_l.grid(row=21, column=57, rowspan=1, columnspan=1)
        C_entry.grid(row=21, column=58)
        
        A_l2.grid(row=38, column=57, rowspan=1, columnspan=1)
        A_output.grid(row=38, column=58)
        B_l2.grid(row=42, column=57, rowspan=1, columnspan=1)
        B_output.grid(row=42, column=58)
        C_l2.grid(row=46, column=57, rowspan=1, columnspan=1)
        C_output.grid(row=46, column=58)
        
        
        def assign_4(*args):
            """get the number input from entry and output calculated answers"""
            if C.get() != '' and A.get() > C.get() or C.get() !=''and B.get() > C.get():
                last_entry = pyth_triangle_root.focus_get()
                last_entry.delete(0, 'end')
                messagebox.showwarning("Warning", "Sides can't be bigger than hypotenuse")
            elif A.get() !='' and B.get() !='' and C.get() !='':
                last_entry = pyth_triangle_root.focus_get()
                last_entry.delete(0, 'end')
                messagebox.showwarning("Warning!", "Can't calculate with 3 values")
            else:
                if A.get() =='':
                    try:
                        bb = float(B.get())
                        cc = float(C.get())
                        Aa = math.sqrt((float(cc)**2)-(float(bb)**2))
                    except ValueError:
                        cc = C.get()
                        bb = B.get()
                        Aa = str(0.0)
                    A_output.config(text=(App.check_lastchar(str(Aa))))
                    B_output.config(text=(bb))
                    C_output.config(text=(cc))
                if B.get()=='':
                    try:
                        aa = float(A.get())
                        cc = float(C.get())
                        Bb = math.sqrt((float(cc)**2)-(float(aa)**2))
                    except ValueError:
                        aa =  A.get()
                        cc =  C.get()
                        Bb =  str(0.0)
                    B_output.config(text=(App.check_lastchar(str(Bb))))
                    A_output.config(text=(aa))
                    C_output.config(text=(cc))
                if C.get()=='':
                    try:
                        aa = float(A.get())
                        bb = float(B.get())
                        Cc = math.sqrt((float(aa)**2)+(float(bb)**2))
                    except ValueError:
                        aa = A.get()
                        bb = B.get()
                        Cc = str(0.0)
                    C_output.config(text=(App.check_lastchar(str(Cc))))
                    A_output.config(text=(aa))
                    B_output.config(text=(bb))
            
        A.trace('w', assign_4)
        B.trace('w', assign_4)
        C.trace('w',assign_4)
        

    def kite_screen():
        """Opens screen to input square values (and calculate answers)"""
            #destroy menu window
        global pages_root
        pages_root.destroy()
        
            #Create new specific window
        kite_root = Screens()

            #Create widgets
        kite_canvas = tk.Canvas(kite_root, height=530, width=530, bg="white")
        back_button = tk.Button(kite_root, width=6, text="Back", 
            relief="raised", command=lambda:kite_root.destroy_screen(page=2))
                #input
        height_l = tk.Label(kite_root, height=1, width=14, relief="raised",
            text="Height 1", font=("Arial",16))
        height_up = tk.StringVar()
        height_entry_up = tk.Entry(kite_root, width=6, textvariable=height_up)
        height_l2 = tk.Label(kite_root, height=1, width=14, relief="raised",
            text="Height 2", font=("Arial",16))
        height_down = tk.StringVar()
        height_entry_down = tk.Entry(kite_root, width=6, textvariable=height_down)
        width_l = tk.Label(kite_root, height=1, width=14, relief="raised",
            text="Width", font=("Arial",16))
        width = tk.StringVar()
        width_entry = tk.Entry(kite_root, width=6, textvariable=width)
                #output
        area_l = tk.Label(kite_root, height=1, width=14, relief="raised",
            text="Area", font=("Arial",16))
        area_output = tk.Label(kite_root, width=6, relief="sunken", 
            bg="white")

            #create mouse hover events
        def on_enter_hdown(e):
            global hup
            global whup
            global kite_cornerdown1
            global kite_cornerdown2
            hup = kite_canvas.create_line(265,200, 265,502, fill="yellow",
                width=7)
            whup= kite_canvas.create_line(110,200,420,200, width=5)
            kite_cornerdown1 = kite_canvas.create_line(243,223, 243,200,
                fill="black", width=2)
            kite_cornerdown2 = kite_canvas.create_line(242,223, 262,223,
                fill="black", width=2)
        def on_leave_hdown(e):
            global hup
            global whup
            global kite_cornerup1
            global kite_cornerup2
            kite_canvas.after(0, kite_canvas.delete, hup)
            kite_canvas.after(0, kite_canvas.delete, whup)
            kite_canvas.after(0, kite_canvas.delete, kite_cornerdown1)
            kite_canvas.after(0, kite_canvas.delete, kite_cornerdown2)
        def on_enter_hup(e):
            global hdown
            global wdown
            global kite_cornerup1
            global kite_cornerup2
            hdown =  kite_canvas.create_line(265,30, 265, 200,
                fill="yellow", width=7)
            wdown = kite_canvas.create_line(110,200,420,200, width=5)
            kite_cornerup1 = kite_canvas.create_line(243,180, 243,200,
                fill="black", width=2)
            kite_cornerup2 = kite_canvas.create_line(242,180, 262,180,
                fill="black", width=2)
        def on_leave_hup(e):
            global hdown
            global wdown
            global kite_cornerup1
            global kite_cornerup2
            kite_canvas.after(0, kite_canvas.delete, hdown)
            kite_canvas.after(0, kite_canvas.delete, wdown)
            kite_canvas.after(0, kite_canvas.delete, kite_cornerup1)
            kite_canvas.after(0, kite_canvas.delete, kite_cornerup2)
        def on_enter_wi(e):
            global wi
            wi = kite_canvas.create_line(110,200,420,200, fill="yellow",
                width=7)
        def on_leave_wi(e):
            global wi
            kite_canvas.after(0, kite_canvas.delete, wi)
        def on_enter_are(e):
            global are
            are = kite_canvas.create_polygon(265,497,112,200,265,33,418,200, 
                fill="yellow")
        def on_leave_are(e):
            global are
            kite_canvas.after(0, kite_canvas.delete, are)
        
        height_l.bind("<Enter>", on_enter_hup)
        height_l.bind("<Leave>", on_leave_hup)
        height_l2.bind("<Enter>", on_enter_hdown)
        height_l2.bind("<Leave>", on_leave_hdown)
        width_l.bind("<Enter>", on_enter_wi)
        width_l.bind("<Leave>", on_leave_wi)
        area_l.bind("<Enter>", on_enter_are)
        area_l.bind("<Leave>", on_leave_are)
        
            #Place widgets in grid
        back_button.grid(row = 1, column=3, columnspan=6)
        kite_canvas.grid(row=2, column=3, columnspan=53, rowspan=53)
        kite_draw = kite_canvas.create_polygon(265,500,110,200,265,30,420,200,
            outline="black", fill="white", width=5)
        height_l.grid(row=9, column=57, rowspan=1, columnspan=1)
        height_entry_up.grid(row=9, column=58)
        height_l2.grid(row=13, column=57, rowspan=1, columnspan=1)
        height_entry_down.grid(row=13, column=58)
        width_l.grid(row=17, column=57, rowspan=1, columnspan=1)
        width_entry.grid(row=17, column=58)
        area_l.grid(row=45, column=57, rowspan=1, columnspan=1)
        area_output.grid(row=45, column=58)
        
            #collect input values and calculate answers + output
        def assign_5(*args):
            try:
                he_up = float(height_up.get())
                he_do =  float(height_down.get())
                wi_2 = float(width.get())
                area = (float(0.5)*he_up*wi_2)+(float(0.5)*he_do*wi_2)
            except ValueError:
                he_up = str(0)
                he_do= str(0)
                wi_2 = str(0)
                area = str(0.0)
            area_output.config(text=(App.check_lastchar(str(area))))
            
            #trace the input values and assign them to method
        height_up.trace('w', assign_5)
        height_down.trace('w', assign_5)
        width.trace('w', assign_5)

        
    def cube_screen():
        """Opens screen to input square values (and calculate answers)"""
            #destroy menu window
        global pages_root
        pages_root.destroy()
        
            #Create new specific window
        cube_root = Screens()

            #Create widgets
        cube_canvas = tk.Canvas(cube_root, height=530, width=530, bg="white")
        back_button = tk.Button(cube_root, width=6, text="Back", 
            relief="raised", command=lambda:cube_root.destroy_screen(page=2))
                #input
        side_l = tk.Label(cube_root, height=1, width=14, relief="raised",
            text="Side", font=("Arial",16))
        side = tk.StringVar()
        side_entry = tk.Entry(cube_root, width=6, textvariable=side)
                #output
        volume_l = tk.Label(cube_root, height=1, width=14, relief="raised",
            text="Volume", font=("Arial",16))
        volume_output = tk.Label(cube_root, width=6, relief="sunken", 
            bg="white")
            
            #Create mouse hover events
        def on_enter_side(e):
            global side_line
            side_line = cube_canvas.create_line(50,230, 300,230, fill="yellow",
                width=7)
        def on_leave_side(e):
            global side_line
            cube_canvas.after(0, cube_canvas.delete, side_line)
        def on_enter_cubearea(e):
            global cube_area
            global cube_area2
            global cube_area3
            cube_area = cube_canvas.create_polygon(53,478,53,232,298,232,298,478,
                fill="yellow")
            cube_area2 = cube_canvas.create_polygon(53,228, 171,92, 415,92, 299,228,
                fill="yellow")
            cube_area3 = cube_canvas.create_polygon(303,230, 418,95, 418,339, 302,475,
                fill="yellow")
        def on_leave_area(e):
            global cube_area
            global cube_area2
            global cube_area3
            cube_canvas.after(0, cube_canvas.delete, cube_area)
            cube_canvas.after(0, cube_canvas.delete, cube_area2)
            cube_canvas.after(0, cube_canvas.delete, cube_area3)
            
        side_l.bind("<Enter>", on_enter_side)
        side_l.bind("<Leave>", on_leave_side)
        volume_l.bind("<Enter>", on_enter_cubearea)
        volume_l.bind("<Leave>", on_leave_area)
            
            
            #Place widgets in grid
        back_button.grid(row = 1, column=3, columnspan=6)
        cube_canvas.grid(row=2, column=3, columnspan=53, rowspan=53)
        cube_draw = cube_canvas.create_polygon(50,480,50,230,300,230,300,480,
            outline="black", fill="white", width=5)
        #cube_2draw = cube_canvas.create_polygon(170,90, 170,340, 420,340, 420,90,
            #outline="black", fill="white", width=5)
        cube_3draw = cube_canvas.create_polygon(50,230, 170,90, 420,90, 300,230,
            outline="black", fill="white", width=5)
        cube_4draw = cube_canvas.create_polygon(300,230, 420,90, 420,340, 300,480,
            outline="black", fill="white", width=5)
        line1 = cube_canvas.create_line(42,337, 58,337, width=5)
        line2 = cube_canvas.create_line(42,353, 58,353, width=5)
        line3 = cube_canvas.create_line(101,155, 119,165, width=5)
        line4 = cube_canvas.create_line(95, 165, 113,175, width=5)
        line5 = cube_canvas.create_line(167,222, 167,238, width=5)
        line6 = cube_canvas.create_line(183,222, 183,238, width=5)
        side_l.grid(row=9, column=57, rowspan=1, columnspan=1)
        side_entry.grid(row=9, column=58)
        volume_l.grid(row=45, column=57, rowspan=1, columnspan=1)
        volume_output.grid(row=45, column=58)
        
        def assign_6(*args):
            """Collect inputvalues en calculate answers"""
            try:
                si_de = float(side.get())
                vo_lume = float(si_de**3)
            except ValueError:
                si_de= str(0.0)
                vo_lume = str(0.0)
            volume_output.config(text=(App.check_lastchar(str(vo_lume))))
            
            #Trace inputvalue
        side.trace('w', assign_6)
        
    def cilinder_screen():
        """Opens screen to input square values (and calculate answers)"""
            #destroy menu window
        global pages_root
        pages_root.destroy()
        
            #Create new specific window
        cilinder_root = Screens()
        
            #Create widgets
        cilinder_canvas = tk.Canvas(cilinder_root, height=530, width=530,
            bg="white")
        back_button = tk.Button(cilinder_root, width=6, text="Back", 
            relief="raised", command=lambda:cilinder_root.destroy_screen(page=2))
            
                #input
        diameter_l = tk.Label(cilinder_root, height=1, width=14, relief="raised",
            text="Diameter", font=("Arial",16))
        diameter = tk.StringVar()
        diameter_entry = tk.Entry(cilinder_root, width=6, textvariable=diameter)
        height_l = tk.Label(cilinder_root, height=1, width=14, relief="raised",
            text="Height", font=("Arial",16))
        height_cilinder =  tk.StringVar()
        height_entry = tk.Entry(cilinder_root, width=6,     
            textvariable=height_cilinder)
            
                #output
        volume_l = tk.Label(cilinder_root, height=1, width=14, relief="raised",
            text="Volume", font=("Arial",16))
        volume_output = tk.Label(cilinder_root, width=6, relief="sunken", 
            bg="white")
            
            #Create mouse hover events
        def on_enter_diacilinder(e):
            global dia_line
            dia_line = cilinder_canvas.create_line(153,265, 373,265, width=7, 
                fill="yellow")
        def on_leave_diacilinder(e):
            global dia_line
            cilinder_canvas.after(0, cilinder_canvas.delete, dia_line)
        def on_enter_height(e):
            global height_cil
            height_cil = cilinder_canvas.create_line(150,75, 150,455, fill="yellow", 
                width=7)
        def on_leave_height(e):
            global height_cil
            cilinder_canvas.after(0, cilinder_canvas.delete, height_cil)
        def on_enter_cilvol(e):
            global cilvol
            global cilvol2
            global cilvol3
            cilvol = cilinder_canvas.create_rectangle(153,75, 372,455,
                outline="yellow", fill="yellow")
            cilvol2 =  cilinder_canvas.create_oval(150,430, 375,480,
                outline="black", fill="yellow", width=5)
            cilvol3 = cilinder_canvas.create_oval(150,50, 375,100,
                outline="black", fill="#F4FA37", width=5)
        def on_leave_cilvol(e):
            global cilvol
            global cilvol2
            global cilvol3  
            cilinder_canvas.after(0, cilinder_canvas.delete, cilvol) 
            cilinder_canvas.after(0, cilinder_canvas.delete, cilvol2)
            cilinder_canvas.after(0, cilinder_canvas.delete, cilvol3)
                
        diameter_l.bind("<Enter>", on_enter_diacilinder)
        diameter_l.bind("<Leave>", on_leave_diacilinder)
        height_l.bind("<Enter>", on_enter_height)
        height_l.bind("<Leave>", on_leave_height)
        volume_l.bind("<Enter>", on_enter_cilvol)
        volume_l.bind("<Leave>", on_leave_cilvol)
            
             #Place widgets in grid
        back_button.grid(row = 1, column=3, columnspan=6)
        cilinder_canvas.grid(row=2, column=3, columnspan=53, rowspan=53)
        cilinder_oval = cilinder_canvas.create_oval(150,50, 375,100,
            outline="black", fill="#DFD3D3", width=5)
        cilinder_oval2 = cilinder_canvas.create_oval(150,430, 375,480,
            outline="black", fill="white", width=5)
        cilinder_l1 = cilinder_canvas.create_line(150,75, 150,455, width=5)
        cilinder_l2 = cilinder_canvas.create_line(375,75, 375,455, width=5)
        diameter_l.grid(row=9, column=57, rowspan=1, columnspan=1)
        diameter_entry.grid(row=9, column=58)
        height_l.grid(row=13, column=57, rowspan=1, columnspan=1)
        height_entry.grid(row=13, column=58)
        volume_l.grid(row=45, column=57, rowspan=1, columnspan=1)
        volume_output.grid(row=45, column=58)
        
        def assign_7(*args):
            """Collect inputvalues en calculate answers"""
            try:
                dia_m = float(diameter.get())
                heightcili = float(height_cilinder.get())
                volume_cil = (float(1/4)*math.pi*float(dia_m**2))*heightcili
            except ValueError:
                volume_cil = str(0.0)
            volume_output.config(text=(App.check_lastchar(str(volume_cil))))
            
            #trace inputvalues
        diameter.trace('w', assign_7)
        height_cilinder.trace('w', assign_7)
        
    def pyramid_screen():
        """Opens screen to input pyramid values (and calculate answers)"""
            #destroy menu window
        global pages_root
        pages_root.destroy()
        
            #Create new specific window
        pyramid_root = Screens()
        
            #Setup grid
        col_count = 65
        row_count = 80
        for col in range(col_count):
            pyramid_root.grid_columnconfigure(col, minsize=10)
        for row in range(row_count):
            pyramid_root.grid_rowconfigure(row, minsize=10)
            
            #Create widgets
        pyramid_canvas = tk.Canvas(pyramid_root, height=530, width=530,
            bg="white")
        back_button = tk.Button(pyramid_root, width=6, text="Back", 
            relief="raised", command=lambda:pyramid_root.destroy_screen(page=2))
            
                #input
        width_l = tk.Label(pyramid_root, height=1, width=14, relief="raised",
            text="Width", font=("Arial",16))
        width = tk.StringVar()
        width_entry = tk.Entry(pyramid_root, width=6, textvariable=width)
        height_l = tk.Label(pyramid_root, height=1, width=14, relief="raised",
            text="Height", font=("Arial",16))
        height_pyramid =  tk.StringVar()
        height_entry = tk.Entry(pyramid_root, width=6,     
            textvariable=height_pyramid)
            
                #output
        volume_l = tk.Label(pyramid_root, height=1, width=14, relief="raised",
            text="Volume", font=("Arial",16))
        volume_output = tk.Label(pyramid_root, width=6, relief="sunken", 
            bg="white")
            
            #Create mousehover events
        def on_enter_pyr_h(e):
            global pyr_h
            pyr_h = pyramid_canvas.create_line(200,475, 200,175, width=7, 
                fill="yellow")
        def on_leave_pyr_h(e):
            global pyr_h
            pyramid_canvas.after(0, pyramid_canvas.delete, pyr_h)
        def on_enter_pyr_w(e):
            global pyr_w
            pyr_w = pyramid_canvas.create_line(50,475, 350,475, width=7, 
                fill="yellow")
        def on_leave_pyr_w(e):
            global pyr_w
            pyramid_canvas.after(0, pyramid_canvas.delete, pyr_w)
        def on_enter_pyr_vol(e):
            global pyr_vol
            global pyr_vol2
            pyr_vol = pyramid_canvas.create_polygon(53,473, 200,180, 347,473,
                fill="yellow")
            pyr_vol2 = pyramid_canvas.create_polygon(350,470, 206,183, 398,351,
                fill="yellow")
        def on_leave_pyr_vol(e):
            global pyr_vol
            global pyr_vol2
            pyramid_canvas.after(0, pyramid_canvas.delete, pyr_vol)
            pyramid_canvas.after(0, pyramid_canvas.delete, pyr_vol2)
            
        height_l.bind("<Enter>", on_enter_pyr_h)
        height_l.bind("<Leave>", on_leave_pyr_h)
        width_l.bind("<Enter>", on_enter_pyr_w)
        width_l.bind("<Leave>", on_leave_pyr_w)
        volume_l.bind("<Enter>", on_enter_pyr_vol)
        volume_l.bind("<Leave>", on_leave_pyr_vol)
            
            #Place widgets in grid
        back_button.grid(row = 1, column=3, columnspan=6)
        pyramid_canvas.grid(row=2, column=3, columnspan=53, rowspan=53)
        pyramid_oval = pyramid_canvas.create_polygon(50,475, 200,175, 350,475,
            outline="black", fill="white", width=5)
        pyramid_oval2 = pyramid_canvas.create_polygon(350,475, 200,175, 400,350,
            outline="black", fill="#DFD3D3", width=5)
        width_l.grid(row=9, column=57, rowspan=1, columnspan=1)
        width_entry.grid(row=9, column=58)
        height_l.grid(row=13, column=57, rowspan=1, columnspan=1)
        height_entry.grid(row=13, column=58)
        volume_l.grid(row=45, column=57, rowspan=1, columnspan=1)
        volume_output.grid(row=45, column=58)
            
        def assign_8(*args):
            """" Collect values and calculate answers(+output)"""
            try:
                he_py = float(height_pyramid.get())
                wi_py = float(width.get())
                vol =  float(1/4)*float(he_py)*(float(wi_py**2))
            except ValueError:
                vol = str(0.0)
            volume_output.config(text=(App.check_lastchar(str(vol))))
         
            #trace input values
        height_pyramid.trace('w', assign_8)
        width.trace('w', assign_8)
        
    def parallel_screen():
        """Opens screen to input pyramid values (and calculate answers)"""
            #destroy menu window
        global pages_root
        pages_root.destroy()
        
            #Create new specific window
        parallel_root = Screens()
        
            #Setup grid
        col_count = 65
        row_count = 80
        for col in range(col_count):
            parallel_root.grid_columnconfigure(col, minsize=10)
        for row in range(row_count):
            parallel_root.grid_rowconfigure(row, minsize=10)
            
            #Create widgets
        parallel_canvas = tk.Canvas(parallel_root, height=530, width=530,
            bg="white")
        back_button = tk.Button(parallel_root, width=6, text="Back", 
            relief="raised", command=lambda:parallel_root.destroy_screen(page=3))
            
                #input
        width_l = tk.Label(parallel_root, height=1, width=14, relief="raised",
            text="Width", font=("Arial",16))
        width = tk.StringVar()
        width_entry = tk.Entry(parallel_root, width=6, textvariable=width)
        height_l = tk.Label(parallel_root, height=1, width=14, relief="raised",
            text="Height", font=("Arial",16))
        height =  tk.StringVar()
        height_entry = tk.Entry(parallel_root, width=6,     
            textvariable=height)
            
                #output
        area_l = tk.Label(parallel_root, height=1, width=14, relief="raised",
            text="Volume", font=("Arial",16))
        area_output = tk.Label(parallel_root, width=6, relief="sunken", 
            bg="white")
            
            #Create mousehover evets
        def on_enter_par_h(e):
            global h_line
            global par_corner1
            global par_corner2
            par_corner1 = parallel_canvas.create_line(127,358, 147,358, fill="black", 
                width=2)
            par_corner2 = parallel_canvas.create_line(128,358, 128,378, fill="black",
                width=2)
            h_line = parallel_canvas.create_line(150,149, 150,378, width=7, 
                fill="yellow")
        def on_leave_par_h(e):
            global h_line
            global par_corner1
            global par_corner2
            parallel_canvas.after(0, parallel_canvas.delete, h_line)
            parallel_canvas.after(0, parallel_canvas.delete, par_corner1)
            parallel_canvas.after(0, parallel_canvas.delete, par_corner2)
        def on_enter_par_w(e):
            global w_line
            w_line = parallel_canvas.create_line(50,380, 380,380, width=7, 
                fill="yellow")
        def on_leave_par_w(e):
            global w_line
            parallel_canvas.after(0, parallel_canvas.delete, w_line)
        def on_enter_par_ar(e):
            global par_ar
            global par_line1
            global par_line2
            global par_line3
            global par_line4
            par_ar = parallel_canvas.create_polygon(151,153, 476,153, 379,378, 53,378,
                fill="yellow")
            par_line1 = parallel_canvas.create_line(223,380, 213,370, width=5)
            par_line2 = parallel_canvas.create_line(203,380, 193,370, width=5)
            par_line3 = parallel_canvas.create_line(335,150, 325,160, width=5)
            par_line4 = parallel_canvas.create_line(315,150, 305,160, width=5)
        def on_leave_par_ar(e):
            global par_ar
            global par_ar
            global par_line1
            global par_line2
            global par_line3
            global par_line4
            parallel_canvas.after(0, parallel_canvas.delete, par_ar)
            parallel_canvas.after(0, parallel_canvas.delete, par_line1)
            parallel_canvas.after(0, parallel_canvas.delete, par_line2)
            parallel_canvas.after(0, parallel_canvas.delete, par_line3)
            parallel_canvas.after(0, parallel_canvas.delete, par_line4)
            
        height_l.bind("<Enter>", on_enter_par_h)
        height_l.bind("<Leave>", on_leave_par_h)
        width_l.bind("<Enter>", on_enter_par_w)
        width_l.bind("<Leave>", on_leave_par_w)
        area_l.bind("<Enter>", on_enter_par_ar)
        area_l.bind("<Leave>", on_leave_par_ar)
            
            #Place widgets in grid
        back_button.grid(row = 1, column=3, columnspan=6)
        parallel_canvas.grid(row=2, column=3, columnspan=53, rowspan=53)
        parallel_fig = parallel_canvas.create_polygon(150,150, 480,150, 380,380, 50,380,
            outline="black", fill="white", width=5)
        parline1 = parallel_canvas.create_line(223,380, 213,370, width=5)
        parline1_2 = parallel_canvas.create_line(223,380, 213,390, width=5)
        parline2 = parallel_canvas.create_line(203,380, 193,370, width=5)
        parlline2_2 = parallel_canvas.create_line(203,380, 193,390, width=5)
        parline3 = parallel_canvas.create_line(335,150, 325,140, width=5)
        parline3_2 = parallel_canvas.create_line(335,150, 325,160, width=5)
        parline4 = parallel_canvas.create_line(315,150, 305,140, width=5)
        parline4_2 = parallel_canvas.create_line(315,150, 305,160, width=5)
        width_l.grid(row=9, column=57, rowspan=1, columnspan=1)
        width_entry.grid(row=9, column=58)
        height_l.grid(row=13, column=57, rowspan=1, columnspan=1)
        height_entry.grid(row=13, column=58)
        area_l.grid(row=45, column=57, rowspan=1, columnspan=1)
        area_output.grid(row=45, column=58)
        
        def assign_9(*args):
            """collect input values en calculate answers+output"""
            try:
                par_he = float(height.get())
                par_wi = float(width.get())
                par_area = float(par_he)*float(par_wi)
            except ValueError:
                par_area = str(0.0)
            area_output.config(text=(App.check_lastchar(str(par_area))))
            
        height.trace('w', assign_9)
        width.trace('w', assign_9)
        
    def trapezoid_screen():
        """Opens screen to input trapezoid values (and calculate answers)"""
            #destroy menu window
        global pages_root
        pages_root.destroy()
        
            #Create new specific window
        trapezoid_root = Screens()
        
            #Setup grid
        col_count = 65
        row_count = 80
        for col in range(col_count):
            trapezoid_root.grid_columnconfigure(col, minsize=10)
        for row in range(row_count):
            trapezoid_root.grid_rowconfigure(row, minsize=10)
            
            #Create widgets
        trapezoid_canvas = tk.Canvas(trapezoid_root, height=530, width=530,
            bg="white")
        back_button = tk.Button(trapezoid_root, width=6, text="Back", 
            relief="raised", command=lambda:trapezoid_root.destroy_screen(page=3))
            
                #input
        length_aside = tk.Label(trapezoid_root, height=1, width=14, relief="raised",
            text="Length a", font=("Arial",16))
        length_a_side = tk.StringVar()
        length_a_entry = tk.Entry(trapezoid_root, width=6, textvariable=length_a_side)
        length_bside = tk.Label(trapezoid_root, height=1, width=14, relief="raised",
            text="Length b", font=("Arial",16))
        length_b_side = tk.StringVar()
        length_b_entry = tk.Entry(trapezoid_root, width=6, textvariable=length_b_side)
        height_l = tk.Label(trapezoid_root, height=1, width=14, relief="raised",
            text="Height", font=("Arial",16))
        height =  tk.StringVar()
        height_entry = tk.Entry(trapezoid_root, width=6,     
            textvariable=height)
            
                #output
        area_trap = tk.Label(trapezoid_root, height=1, width=14, relief="raised",
            text="Area", font=("Arial",16))
        area_output = tk.Label(trapezoid_root, width=6, relief="sunken", 
            bg="white")
            
            #Create mousehover evets
        def on_enter_trap_h(e):
            global h_trap
            global trap_corner1
            global trap_corner2
            trap_corner1 = trapezoid_canvas.create_line(146,448, 146,428, fill="black", 
                width=2)
            trap_corner2 = trapezoid_canvas.create_line(146,428, 168,428, fill="black",
                width=2)
            h_trap = trapezoid_canvas.create_line(168,103, 168,448, width=7, 
                fill="yellow")
        def on_leave_trap_h(e):
            global h_trap
            global trap_corner1
            global trap_corner2
            trapezoid_canvas.after(0, trapezoid_canvas.delete, h_trap)
            trapezoid_canvas.after(0, trapezoid_canvas.delete, trap_corner1)
            trapezoid_canvas.after(0, trapezoid_canvas.delete, trap_corner2)
        def on_enter_lengtha(e):
            global a_line
            a_line = trapezoid_canvas.create_line(166,105, 420,105, width=7, 
                fill="yellow")
        def on_leave_lengtha(e):
            global a_line
            trapezoid_canvas.after(0, trapezoid_canvas.delete, a_line)
        def on_enter_lengthb(e):
            global b_line
            b_line = trapezoid_canvas.create_line(35,450, 490,450, width=7, 
                fill="yellow")
        def on_leave_lengthb(e):
            global b_line
            trapezoid_canvas.after(0, trapezoid_canvas.delete, b_line)
        def on_enter_trap_ar(e):
            global trap_ar
            trap_ar = trapezoid_canvas.create_polygon(38,448, 167,108, 419,108, 487,448,
                fill="yellow")
        def on_leave_trap_ar(e):
            global trap_ar
            trapezoid_canvas.after(0, trapezoid_canvas.delete, trap_ar)
            
        height_l.bind("<Enter>", on_enter_trap_h)
        height_l.bind("<Leave>", on_leave_trap_h)
        length_aside.bind("<Enter>", on_enter_lengtha)
        length_aside.bind("<Leave>", on_leave_lengtha)
        length_bside.bind("<Enter>", on_enter_lengthb)
        length_bside.bind("<Leave>", on_leave_lengthb)
        area_trap.bind("<Enter>", on_enter_trap_ar)
        area_trap.bind("<Leave>", on_leave_trap_ar)
            
            #Place widgets in grid
        back_button.grid(row = 1, column=3, columnspan=6)
        trapezoid_canvas.grid(row=2, column=3, columnspan=53, rowspan=53)
        trapezoid_canvas.create_polygon(35,450, 166,105, 420,105, 490,450,
            fill="white", outline="black", width=5)
        length_aside.grid(row=9, column=57, rowspan=1, columnspan=1)
        length_a_entry.grid(row=9, column=58)
        length_bside.grid(row=13, column=57, rowspan=1, columnspan=1)
        length_b_entry.grid(row=13, column=58)
        height_l.grid(row=17, column=57, rowspan=1, columnspan=1)
        height_entry.grid(row=17, column=58)
        area_trap.grid(row=45, column=57, rowspan=1, columnspan=1)
        area_output.grid(row=45, column=58)
        
        def assign_10(*args):
            """collect input values en calculate answers+output"""
            try:
                aside_num = float(length_a_side.get())
                bside_num = float(length_b_side.get())
                height_num = float(height.get())
                area_str = float(0.5)*float(height_num)*(float(aside_num)+float(bside_num))
            except ValueError:
                area_str = str(0.0)
            area_output.config(text=(App.check_lastchar(str(area_str))))
            
        height.trace('w', assign_10)
        length_a_side.trace('w', assign_10)
        length_b_side.trace('w', assign_10)


    def check_lastchar(str_to_check):
        """rounds up or rounds down value if the string of digits is longer than 6 
        characters and checks if last character in outputbox is not '.', rounds
        up or down value depending on next digit"""
        
        check_last = list(str_to_check)
        print(check_last)
        print(len(str_to_check))
        try:
            # checks if decimal point is on position 1 to 4 en if length of the string is not longer 
            # than 7 chars. if so
            if check_last[1] == '.' and len(str_to_check) < 7 \
            or check_last[2] == '.' and len(str_to_check) < 7 \
            or check_last[3] == '.' and len(str_to_check) < 7 \
            or check_last[4] == '.' and len(str_to_check) < 7:
                new_str = "".join(check_last)
                str_to_check = new_str
                return str_to_check
            elif check_last[1] == '.' and len(str_to_check) > 5 \
            or check_last[2] == '.' and len(str_to_check) > 5 \
            or check_last[3] == '.' and len(str_to_check) > 5 \
            or check_last[4] == '.' and len(str_to_check) > 5:
                if int(check_last[6]) > 4:
                    check_last[5] = str(int(check_last[5])+1)
                    new_str = "".join(check_last)
                    str_to_check = new_str
                    return str_to_check[:6]
                elif int(check_last[6]) < 5:
                    new_str = "".join(check_last)
                    str_to_check = new_str
                    return str_to_check[:6]
            elif check_last[5] == '.':
                if int(check_last[6]) > 4:
                    check_last[5] = str(int(check_last[5])+1)
                    new_str = "".join(check_last)
                    str_to_check = new_str
                    return str_to_check[:5]
                elif int(check_last[6]) < 5:
                    check_last.remove('.')
                    new_str = "".join(check_last)
                    str_to_check = new_str
                    return str_to_check[:5]
            elif int(check_last.index('.')) > 6:
                messagebox.showwarning("Warning", "Value is too high for display")
                return str_to_check[:6]
        except IndexError:
            if len(str_to_check) > 6:
                messagebox.showwarning("Warning", "Value is too high for display")
                print("Index error"+ str(str_to_check))
            elif len(str_to_check) <6:
                new_str = "".join(check_last)
                str_to_check = new_str
                return str_to_check[:5]
            
 


if __name__ == "__main__":
    app = App(page=1)
    app.mainloop()
