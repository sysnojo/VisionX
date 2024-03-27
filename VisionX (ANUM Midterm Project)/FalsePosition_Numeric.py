'''
[!] MAIN FILE

               ,ggg,          ,gg
              dP"""Y8,      ,dP' 
              Yb,_  "8b,   d8"   
               `""    Y8,,8P'    
                       Y88"      
                      ,888b      
                     d8" "8b,    
                   ,8P'    Y8,   
                  d8"       "Yb, 
                ,8P'          "Y8

          "Numeric Analysis: Mid-term"

Topic  : Comparing False Position vs Numeric Method on equation y
Author : - John Bryan Khornelius
         - Muhammad Al Gisna Syuban
         - Muhammad Ananta Arya Novandi
         - Irvan Nurfauzan Saputra
         - Kafka Ramadityo

> VisionX - We Make it Happen
'''
import time
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Entry, Scrollbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

###############################################################
###########        WINDOW APPLICATION SETTING        ##########
###############################################################
# Fungsi untuk mengkalkulasikan y sesuai dengan koefisien
def f(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

def find_max_min(a, b, c, d):
    discriminant = b**2 - 3*a*c
    if discriminant < 0:
        return None, None, None, None  # No real roots

    x_critical_points = np.roots([3 * a, 2 * b, c])
    y_critical_points = f(x_critical_points, a, b, c, d)

    y_max = max(y_critical_points)
    y_min = min(y_critical_points)

    x_max = x_critical_points[np.argmax(y_critical_points)]
    x_min = x_critical_points[np.argmin(y_critical_points)]

    return y_max, y_min, x_max, x_min

class Home:     
    def __init__(self, window):
        self.window = window
        self.draggable = False
        self.x = 0
        self.y = 0

        # initiate window w, h
        wind_w = 1280  # width of window
        wind_h = 720  # height of window

        # get screen w, h
        scr_w = window.winfo_screenwidth()
        scr_h = window.winfo_screenheight()

        # get coords of screen
        scr_coord_x = (scr_w / 2) - (wind_w / 2)
        scr_coord_y = (scr_h / 2) - (wind_h / 2)

        # universal variables
        uni_bg = "#000000"

        # config window
        self.window.geometry("%dx%d+%d+%d" % (wind_w, wind_h, scr_coord_x, scr_coord_y))
        self.window.overrideredirect(True)  # False = hide titlebar
        self.window.configure(bg=uni_bg)

        # Create frame
        self.mmc_frame = tk.Frame(master=self.window, width=wind_w, height=30, background=uni_bg)
        self.mmc_frame.pack()

        # Bind double-click event
        self.mmc_frame.bind("<Button-1>", self.toggle_drag)

        # Create close button (MMC)
        close_btn = tk.Button(
            master=self.mmc_frame, 
            text="x", 
            fg="#FFFFFF", 
            background=uni_bg, 
            borderwidth=0, 
            highlightthickness=0,
            command=self.on_close_clicked  # Use self.on_close_clicked here
            )
        close_btn.configure(font=("Poppins Bold", 13))
        close_btn_w = close_btn.winfo_reqwidth()
        close_btn_x = wind_w - close_btn_w - 20
        close_btn.place(x=close_btn_x, y=3)

        # Create sidebar (for input)
        sidebar_path = "C:/Users/ngrok/Documents/[45] ANUM 2024/VisionX (ANUM Midterm Project)/sidebar.png"
        self.sidebar = tk.PhotoImage(file=sidebar_path)
        self.resized_img = self.sidebar.subsample(2, 2) # resize logo 1/5th
        sidebar_frame = tk.Label(master=self.window, image=self.resized_img, bg=uni_bg)
        sidebar_frame.place(x=20, y=40)

        # sidebar 2
        sidebar_2_path = "C:/Users/ngrok/Documents/[45] ANUM 2024/VisionX (ANUM Midterm Project)/sidebar2.png"
        self.sidebar_2 = tk.PhotoImage(file=sidebar_2_path)
        self.resized_sidebar_2 = self.sidebar_2.subsample(2, 2) # resize logo 1/5th
        sidebar_2 = tk.Label(master=self.window, image=self.resized_sidebar_2, bg=uni_bg)
        sidebar_2.place(x=20, y=160)

        # sidebar 2
        sidebar_3_path = "C:/Users/ngrok/Documents/[45] ANUM 2024/VisionX (ANUM Midterm Project)/sidebar3.png"
        self.sidebar_3 = tk.PhotoImage(file=sidebar_3_path)
        self.resized_sidebar_3 = self.sidebar_3.subsample(2, 2) # resize logo 1/5th
        sidebar_3 = tk.Label(master=self.window, image=self.resized_sidebar_3, bg=uni_bg)
        sidebar_3.place(x=wind_w - 220, y=40)

        # header sidebar3
        lbl_header_sbar = tk.Label(master=self.window, text="Output", fg="#FFFFFF", background="#121212")
        lbl_header_sbar.configure(font=("Poppins", 17))
        lbl_header_sbar.place(x=wind_w - 170, y=50)

        # akar toggle
        akar_path = "C:/Users/ngrok/Documents/[45] ANUM 2024/VisionX (ANUM Midterm Project)/akar_toggle.png"
        self.akar = tk.PhotoImage(file=akar_path)
        self.resized_img_4 = self.akar.subsample(1,1)
        logo_label= tk.Label(master=self.window, image=self.resized_img_4, bg="#121212")
        logo_label.place(x=wind_w - 180, y=100)

        # LOG OUTPUT
        log_frame_w = 300
        log_frame_h = 400
        fpos_log_frame = tk.Frame(master=self.window, width=log_frame_w, height=log_frame_h, bg="#FFFFFF")
        fpos_log_frame.place(x=wind_w - 204, y=160)

        # scrollbar
        scrollbar_fpos = Scrollbar(master=fpos_log_frame)
        
        # Create a text widget inside fpos_log_frame
        self.log_output_text = tk.Text(master=fpos_log_frame, wrap="word", yscrollcommand=scrollbar_fpos.set, width=20, height=22, bg="#2D2D2D", fg="#FFFFFF", font=("Poppins Medium", 9), borderwidth=0)
        self.log_output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        # Configure the scrollbar to control the text widget
        scrollbar_fpos.config(command=self.log_output_text.yview)

        # mmc logo
        logo_path = "C:/Users/ngrok/Documents/[45] ANUM 2024/VisionX (ANUM Midterm Project)/logo_vision.png"
        self.logo = tk.PhotoImage(file=logo_path)
        self.resized_img_2 = self.logo.subsample(25,25)
        logo_label= tk.Label(master=self.window, image=self.resized_img_2, bg=uni_bg)
        logo_label.place(x=10, y=5)

        # header sidebar
        lbl_header_sbar = tk.Label(master=self.window, text="Equation", fg="#FFFFFF", background="#121212")
        lbl_header_sbar.configure(font=("Poppins", 17))
        lbl_header_sbar.place(x=50, y=50)

        # equation toggle
        equ_path = "C:/Users/ngrok/Documents/[45] ANUM 2024/VisionX (ANUM Midterm Project)/equation_toggle.png"
        self.equ = tk.PhotoImage(file=equ_path)
        self.resized_img_3 = self.equ.subsample(1,1)
        logo_label= tk.Label(master=self.window, image=self.resized_img_3, bg="#121212")
        logo_label.place(x=320, y=50)

        # parameters toggle
        param_path = "C:/Users/ngrok/Documents/[45] ANUM 2024/VisionX (ANUM Midterm Project)/parameters_toggle.png"
        self.param = tk.PhotoImage(file=param_path)
        self.res_param = self.param.subsample(1,1)
        param_lbl= tk.Label(master=self.window, image=self.res_param, bg="#121212")
        param_lbl.place(x=230, y=180)

        # Input Parameters
        lbl_parameter = tk.Label(master=self.window, text="Parameters", fg="#FFFFFF", background="#121212")
        lbl_parameter.configure(font=("Poppins", 17))
        lbl_parameter.place(x=50, y=180)

        # create equation
        lbl_y = tk.Label(master=self.window, text="f(x) =", fg="#9D9D9D", background="#121212")
        lbl_a_coef = tk.Label(master=self.window, text="_", fg="white", background="#121212")
        lbl_a = tk.Label(master=self.window, text="x^3   +", fg="#9D9D9D", background="#121212")
        lbl_b_coef = tk.Label(master=self.window, text="_", fg="white", background="#121212")
        lbl_b = tk.Label(master=self.window, text="x^2   +", fg="#9D9D9D", background="#121212")
        lbl_c_coef = tk.Label(master=self.window, text="_", fg="white", background="#121212")
        lbl_c = tk.Label(master=self.window, text="x   +", fg="#9D9D9D", background="#121212")
        lbl_d_coef = tk.Label(master=self.window, text="_", fg="white", background="#121212")

        # equation configuration
        font = ("Poppins Medium", 13)
        lbl_y.configure(font=font)
        lbl_a_coef.configure(font=font)
        lbl_a.configure(font=font)
        lbl_b_coef.configure(font=font)
        lbl_b.configure(font=font)
        lbl_c_coef.configure(font=font)
        lbl_c.configure(font=font)
        lbl_d_coef.configure(font=font)

        # places
        equ_uni_y = 100
        equ_uni_x = 50
        lbl_y.place(x=equ_uni_x, y=equ_uni_y)

        lbl_a_coef.place(x=equ_uni_x + 55, y=equ_uni_y)
        lbl_a.place(x=equ_uni_x + 83, y=equ_uni_y)

        lbl_b_coef.place(x=equ_uni_x + 55 + 85, y=equ_uni_y)
        lbl_b.place(x=equ_uni_x + 83 + 83, y=equ_uni_y)

        lbl_c_coef.place(x=equ_uni_x + 55 + 85 + 83, y=equ_uni_y)
        lbl_c.place(x=equ_uni_x + 83 + 83 + 80, y=equ_uni_y)

        lbl_d_coef.place(x=equ_uni_x+ 55 + 85 + 83 + 60, y=equ_uni_y)

        # create label entry
        entry_lbl_font = ("Poppins Medium", 12)
        entry_lbl_font_info = ("Poppins Medium", 10)

        # label entry a
        entry_a_lbl = tk.Label(master=self.window, text="Input coefficient a", fg="white", font=entry_lbl_font, background="#121212")
        entry_a_lbl.place(x=50, y=240)
        entry_a_lbl_info = tk.Label(master=self.window, text="(example: 0.2)", fg="#414141", font=entry_lbl_font_info, background="#121212")
        entry_a_lbl_info.place(x=50, y=265)

        # label entry b
        entry_b_lbl = tk.Label(master=self.window, text="Input coefficient b", fg="white", font=entry_lbl_font, background="#121212")
        entry_b_lbl.place(x=50, y=290)
        entry_b_lbl_info = tk.Label(master=self.window, text="(example: 1.4)", fg="#414141", font=entry_lbl_font_info, background="#121212")
        entry_b_lbl_info.place(x=50, y=315)

        # label entry c
        entry_c_lbl = tk.Label(master=self.window, text="Input coefficient c", fg="white", font=entry_lbl_font, background="#121212")
        entry_c_lbl.place(x=50, y=340)
        entry_c_lbl_info = tk.Label(master=self.window, text="(example: -8)", fg="#414141", font=entry_lbl_font_info, background="#121212")
        entry_c_lbl_info.place(x=50, y=365)
       
        # label entry d
        entry_d_lbl = tk.Label(master=self.window, text="Input coefficient d", fg="white", font=entry_lbl_font, background="#121212")
        entry_d_lbl.place(x=50, y=390)
        entry_d_lbl_info = tk.Label(master=self.window, text="(example: -23)", fg="#414141", font=entry_lbl_font_info, background="#121212")
        entry_d_lbl_info.place(x=50, y=415) 

        # label entry xl
        entry_xl_lbl = tk.Label(master=self.window, text="Input x low (xl)", fg="white", font=entry_lbl_font, background="#121212")
        entry_xl_lbl.place(x=50, y=440)
        entry_xl_lbl_info = tk.Label(master=self.window, text="(example: -12)", fg="#414141", font=entry_lbl_font_info, background="#121212")
        entry_xl_lbl_info.place(x=50, y=465) 

        # label entry xu
        entry_xu_lbl = tk.Label(master=self.window, text="Input x upper (xu)", fg="white", font=entry_lbl_font, background="#121212")
        entry_xu_lbl.place(x=50, y=490)
        entry_xu_lbl_info = tk.Label(master=self.window, text="(example: 8)", fg="#414141", font=entry_lbl_font_info, background="#121212")
        entry_xu_lbl_info.place(x=50, y=515) 

        # Notes
        lbl_note = tk.Label(
            master=self.window, 
            text="Note: This parameter will compare two different methods",
            fg="white",
            font=("Poppins Light", 8),
            background="#121212"
            )
        lbl_note.place(x=50, y=565)
        lbl_note_2 = tk.Label(
            master=self.window, 
            text="namely false position and numeric.",
            fg="white",
            font=("Poppins Light", 8),
            background="#121212"
            )
        lbl_note_2.place(x=83, y=580)

        # compare button
        compare_btn = tk.Button(
            master=self.window, 
            text="Compare", 
            fg="#FFFFFF", 
            background="#2D2D2D", 
            borderwidth=0, 
            highlightthickness=0,
            width=13,
            command=self.compare_methods
            )
        compare_btn.configure(font=("Poppins Bold", 13))
        compare_btn.place(x=140, y=620)

        # create entry
        padd = 80
        padd_x = 230
        entry_font = ("Poppins Light", 11)
        self.entry_a = Entry(master=self.window, background="#2D2D2D", borderwidth=0, width=10, fg="white", font=entry_font)
        self.entry_a.place(x=padd_x, y=equ_uni_y +padd + 60)
        self.entry_b = Entry(master=self.window, background="#2D2D2D", borderwidth=0, width=10, fg="white", font=entry_font)
        self.entry_b.place(x=padd_x, y=equ_uni_y +padd+ 60 + 55)
        self.entry_c = Entry(master=self.window, background="#2D2D2D", borderwidth=0, width=10, fg="white", font=entry_font)
        self.entry_c.place(x=padd_x, y=equ_uni_y +padd+ 60 + 60 + 45)
        self.entry_d = Entry(master=self.window, background="#2D2D2D", borderwidth=0, width=10, fg="white", font=entry_font)
        self.entry_d.place(x=padd_x, y=equ_uni_y +padd+ 60 + 60 + 60 + 35)
        self.entry_xl = Entry(master=self.window, background="#2D2D2D", borderwidth=0, width=10, fg="white", font=entry_font)
        self.entry_xl.place(x=padd_x, y=equ_uni_y +padd+ 60 + 60 + 60 + 60 + 25)
        self.entry_xu = Entry(master=self.window, background="#2D2D2D", borderwidth=0, width=10, fg="white", font=entry_font)
        self.entry_xu.place(x=padd_x, y=equ_uni_y +padd+ 60 + 60 + 60 + 60 + 60 + 15)

        # PLOT FRAME
        plot_frame_w = 600
        plot_frame_h = 300
        fig_size = (6, 3.14)
        plot_frame_y = 42

        # Membuat plot (inisiasi kosong)
        self.fpos_fig = plt.figure(figsize=fig_size, facecolor="#121212")
        x = np.linspace(-20, 20, 100)
        y = x - x * 0

        ax = plt.axes()
        ax.set_facecolor("#2D2D2D")
        plt.tick_params(axis='x', colors='white')
        plt.tick_params(axis='y', colors='white')

        plt.title('False Position Plot (Empty)', color='white')

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.grid(True, color='#222222')

        self.num_fig = plt.figure(figsize=fig_size, facecolor="#121212")
        x = np.linspace(-20, 20, 100)
        y = x - x * 0
        ax = plt.axes()
        ax.set_facecolor("#2D2D2D")
        plt.tick_params(axis='x', colors='white')
        plt.tick_params(axis='y', colors='white')
        plt.title('Numeric Method Plot (Empty)', color='white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.grid(True, color='#222222')

        # false position frame
        false_position_plot_frame = tk.Frame(master=self.window, width=plot_frame_w, height=plot_frame_h)
        false_position_plot_frame.place(x=450, y=plot_frame_y) 

        self.canvas_fpos = FigureCanvasTkAgg(self.fpos_fig, master=false_position_plot_frame)
        self.canvas_fpos.get_tk_widget().pack()

        # numeric method frame
        numeric_method_plot_frame = tk.Frame(master=self.window, width=plot_frame_w, height=plot_frame_h)
        numeric_method_plot_frame.place(x=450, y=plot_frame_y + 330) 

        num_fig = plt.figure(figsize=fig_size)
        self.canvas_num = FigureCanvasTkAgg(self.num_fig, master=numeric_method_plot_frame)
        self.canvas_num.get_tk_widget().pack()

        # bind the entry to a function that updates lbl_a_coef
        self.entry_a.bind("<KeyRelease>", lambda event, label=lbl_a_coef, coef='a': self.update_coef(event, label, coef))
        self.entry_b.bind("<KeyRelease>", lambda event, label=lbl_b_coef, coef='b': self.update_coef(event, label, coef))
        self.entry_c.bind("<KeyRelease>", lambda event, label=lbl_c_coef, coef='c': self.update_coef(event, label, coef))
        self.entry_d.bind("<KeyRelease>", lambda event, label=lbl_d_coef, coef='d': self.update_coef(event, label, coef))
        # get xl, xu
        self.entry_xl.bind("<KeyRelease>", lambda event, coef='xl': self.update_coef(event, None, coef))
        self.entry_xu.bind("<KeyRelease>", lambda event, coef='xu': self.update_coef(event, None, coef))

    def update_coef(self, event, label, coef):
        # get the value from the entry and update the respective coefficient label
        entry = event.widget
        coef_value = entry.get()
        # storing xl, xu
        global xl, xu, a, b, c, d

        if label is not None:
            label.config(text=coef_value)
            try:
                value = float(coef_value)
                if coef == 'a':
                    a = value if value != 0 else 0
                elif coef == 'b':
                    b = value if value != 0 else 0
                elif coef == 'c':
                    c = value if value != 0 else 0
                else:
                    d = value if value != 0 else 0
            except ValueError:
                print("Empty")
        else:
            try:
                value = float(coef_value)
                if coef == 'xl':
                    xl = value if value != 0 else 0
                else:
                    xu = value if value != 0 else 0
            except ValueError:
                print("Empty")
        # Set default values if variables are not defined
        a = a if 'a' in globals() else 0
        b = b if 'b' in globals() else 0
        c = c if 'c' in globals() else 0
        d = d if 'd' in globals() else 0
        xl = xl if 'xl' in globals() else -10
        xu = xu if 'xu' in globals() else 10

        print(xl, xu)
        x = np.linspace(xl, xu, 400)
        y = a*x**3 + b*x**2 + c*x + d
        x_line = np.linspace(xl-5, xu+5, 400)
        sb_x = x_line - x_line - 0

        # find xmax, xmin
        ymax, ymin, xmax, xmin = find_max_min(a, b, c, d)
        
        # for false position
        self.fpos_fig.clear()
        plt.figure(self.fpos_fig.number)
        
        ax = plt.axes()
        ax.set_facecolor("#2D2D2D")
        plt.tick_params(axis='x', colors='white')
        plt.tick_params(axis='y', colors='white')


        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.grid(True, color='#222222')
        
        plt.axvline(x=xmax, color='magenta', linestyle='--', label='xmax')
        plt.scatter(xmax, ymax, color='magenta')
        plt.scatter(xmin, ymin, color='orange')
        plt.axvline(x=xmin, color='orange', linestyle='--', label='xmin')
        plt.axvline(x=xl, color='cyan', linestyle='--', label='xl')
        plt.axvline(x=xu, color='red', linestyle='--', label='xu')
        plt.plot(x, y, color='green', label='y')
        plt.plot(x_line, sb_x, color='#121212', label='sumbu x')
        plt.title(f'Plot False Position', color='white')
        plt.legend(fontsize='small')

        self.canvas_fpos.draw()

        # for numeric
        self.num_fig.clear()
        plt.figure(self.num_fig.number)
        ax = plt.axes()
        ax.set_facecolor("#2D2D2D")
        plt.tick_params(axis='x', colors='white')
        plt.tick_params(axis='y', colors='white')


        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.grid(True, color='#222222')
        
        plt.axvline(x=xmax, color='magenta', linestyle='--', label='xmax')
        plt.scatter(xmax, ymax, color='magenta')
        plt.scatter(xmin, ymin, color='orange')
        plt.axvline(x=xmin, color='orange', linestyle='--', label='xmin')
        plt.axvline(x=xl, color='cyan', linestyle='--', label='xl')
        plt.axvline(x=xu, color='red', linestyle='--', label='xu')
        plt.plot(x, y, color='green', label='y')
        plt.plot(x_line, sb_x, color='#121212', label='sumbu x')
        plt.title(f'Plot Numeric Method', color='white')
        plt.legend(fontsize='small')

        self.canvas_num.draw()
    
    def compare_methods(self):
        # Dapatkan nilai-nilai variabel dari entry masing-masing
        self.a = float(self.entry_a.get()) if hasattr(self, 'entry_a') else 0
        self.b = float(self.entry_b.get()) if hasattr(self, 'entry_b') else 0
        self.c = float(self.entry_c.get()) if hasattr(self, 'entry_c') else 0
        self.d = float(self.entry_d.get()) if hasattr(self, 'entry_d') else 0
        self.xl = float(self.entry_xl.get()) if hasattr(self, 'entry_xl') else -10
        self.xu = float(self.entry_xu.get()) if hasattr(self, 'entry_xu') else 10

        # find xmax, xmin
        self.ymax, self.ymin, self.xmax, self.xmin = find_max_min(self.a, self.b, self.c, self.d)

        # Metode False Position
        err_m = 0.0001
        dx = 0.00001
        i = 0

        self.log_output_text.insert(tk.END, "=====[CONFIG]=====\n")
        self.log_output_text.insert(tk.END, f"err_m: {err_m}\n")
        self.log_output_text.insert(tk.END, f"dx: {dx}\n")
        self.log_output_text.insert(tk.END, f"x_max: {self.xmax:.9f}\n")
        self.log_output_text.insert(tk.END, f"x_min: {self.xmin:.9f}\n\n")

        self.log_output_text.insert(tk.END, "===[FALSE POSITION]===\n")

        i, akar_1 = self.false_position(self.xl, self.xmax, self.a, self.b, self.c, self.d, err_m=err_m)
        i, akar_2 = self.false_position(self.xmax, self.xmin, self.a, self.b, self.c, self.d, err_m=err_m)
        i, akar_3 = self.false_position(self.xmin, self.xu, self.a, self.b, self.c, self.d, err_m=err_m)

        # ANIMASI FALSE POSITION
        x_line = np.linspace(self.xl, self.xu, 100)
        sb_x = x_line - x_line - 0

        y_vals = f(x_line, self.a, self.b, self.c, self.d)

        plt.figure(self.fpos_fig.number)  # Pindahkan ini di luar loop
        ax = plt.axes()

        self.log_output_text.insert(tk.END, "=================\n")
        self.log_output_text.insert(tk.END, f"Iterasi: {i} kali\n")
        self.log_output_text.insert(tk.END, f"Root 1: {akar_1:.9f}\n")
        self.log_output_text.insert(tk.END, f"Root 2: {akar_2:.9f}\n")
        self.log_output_text.insert(tk.END, f"Root 3: {akar_3:.9f}\n\n")
        # Metode Numerik Dasar
        x = self.xl
        y = f(x, self.a, self.b, self.c, self.d)
        dx = 0.00001
        err_m = 0.0001

        root_num_x, root_num_y, num_i = self.numeric_method(self.xl, self.xu, self.a, self.b, self.c, self.d, dx, err_m)
       
        self.log_output_text.insert(tk.END, "==[NUMERIC METHOD]==\n")
        self.log_output_text.insert(tk.END, f"Iterasi: {num_i} kali\n")
        self.log_output_text.insert(tk.END, f"Root 1: {root_num_x[0]:.9f}\n")
        self.log_output_text.insert(tk.END, f"Root 2: {root_num_x[1]:.9f}\n")
        self.log_output_text.insert(tk.END, f"Root 3: {root_num_x[2]:.9f}\n")

        # Plot hasil False Position
        self.fpos_fig.clear()
        plt.figure(self.fpos_fig.number)
        ax = plt.axes()
        ax.set_facecolor("#2D2D2D")
        plt.tick_params(axis='x', colors='white')
        plt.tick_params(axis='y', colors='white')

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        # garis potong
        # Calculate ymin and ymax

        # Add diagonal line from xl to xmax
        plt.plot([self.xl, self.xmax], [-25, self.ymax], color='orange', linestyle='-')
        plt.plot([self.xmax, self.xmin], [self.ymax, self.ymin], color='orange', linestyle='-')
        plt.plot([self.xmin, self.xu], [self.ymin, 25], color='orange', linestyle='-')
        
        plt.axvline(x=self.xmax, color='cyan', linestyle='--')
        plt.axvline(x=self.xmin, color='purple', linestyle='--')
        plt.plot(x_line, sb_x, '#121212')
        plt.axvline(x=self.xl, color='r', linestyle='--')
        plt.axvline(x=self.xu, color='g', linestyle='--')
        plt.plot(x_line, y_vals)
        plt.scatter([akar_1, akar_2, akar_3], [f(akar_1, self.a, self.b, self.c, self.d), f(akar_2, self.a, self.b, self.c, self.d), f(akar_3, self.a, self.b, self.c, self.d)], color='red', label='Akar')
        plt.title('False Position Root Plot', color='white')
        plt.legend(fontsize='small')
        plt.grid(True, color='#222222')
        self.canvas_fpos.draw()

        # Plot hasil Numerik
        self.num_fig.clear()
        plt.figure(self.num_fig.number)
        ax = plt.axes()
        ax.set_facecolor("#2D2D2D")
        plt.tick_params(axis='x', colors='white')
        plt.tick_params(axis='y', colors='white')


        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        
        plt.axvline(x=self.xmax, color='cyan', linestyle='--')
        plt.axvline(x=self.xmin, color='purple', linestyle='--')
        plt.plot(x_line, sb_x, '#121212')
        plt.axvline(x=self.xl, color='r', linestyle='--')
        plt.axvline(x=self.xu, color='g', linestyle='--')
        plt.plot(x_line, y_vals)
        plt.scatter([root_num_x[0], root_num_x[1], root_num_x[2]], [f(root_num_x[0], self.a, self.b, self.c, self.d), f(root_num_x[1], self.a, self.b, self.c, self.d), f(root_num_x[2], self.a, self.b, self.c, self.d)], color='red', label='Akar')
        plt.title('Numeric Method Root Plot', color='white')
        plt.legend(fontsize='small')
        plt.grid(True, color='#222222')
        self.canvas_num.draw()


    def numeric_method(self, x_awal, x_akhir, a, b, c, d, dx, err_m):
        x_roots = []  # List untuk menyimpan koordinat x akar
        y_roots = []  # List untuk menyimpan nilai fungsi di koordinat x akar
        root_counter = 1  # Counter untuk akar
        max = False  # Flag untuk menandai apakah fungsi melewati batas error_m
        i = 0

        while x_awal < x_akhir:
            fx = f(x_awal, a, b, c, d)

            if (fx > err_m) and not max:
                x_roots.append(x_awal)
                y_roots.append(fx)
                max = True
                root_counter += 1
            if (fx < err_m) and max:
                x_roots.append(x_awal)
                y_roots.append(fx)
                max = False
                root_counter += 1
            i += 1
            x_awal += dx

        return x_roots, y_roots, i

    def false_position(self, xl, xu, a, b, c, d, err_m=0.0001):
        iterasi = 0

        while True:
            xr = xu - f(xu, a, b, c, d) * (xu - xl) / (f(xu, a, b, c, d) - f(xl, a, b, c, d))

            # akar ditemukan
            if abs(f(xr, a, b, c, d)) < err_m:
                break

            # ada perpotongan antara garis dan sumbu x antara xl dan xr
            if f(xl, a, b, c, d) * f(xr, a, b, c, d) < 0:
                xu = xr
            else:
                # jika tidak berarti perpotongan ada di xr dan xu
                xl = xr
            iterasi += 1
        return iterasi, xr
        
    def on_close_clicked(self):
        self.window.destroy()

    def toggle_drag(self, event):
        if not self.draggable:
            self.draggable = True
            self.mmc_frame.bind("<B1-Motion>", self.on_drag)
            self.mmc_frame.bind("<ButtonRelease-1>", self.stop_drag)
            if hasattr(event, 'x') and hasattr(event, 'y'):
                self.x = event.x
                self.y = event.y
        else:
            self.draggable = False
            self.mmc_frame.unbind("<B1-Motion>")
            self.mmc_frame.unbind("<ButtonRelease-1>")

    def on_drag(self, event):
        x = self.window.winfo_x() + (event.x - self.x)
        y = self.window.winfo_y() + (event.y - self.y)
        self.window.geometry(f"+{x}+{y}")

    def stop_drag(self, event):
        self.x = event.x
        self.y = event.y

###############################################################
###########           APPLICATION RELEASE            ##########
###############################################################
    
def page():
    window = tk.Tk()
    Home(window)
    # loop window
    window.mainloop()

if __name__ == '__main__':
    page()

###############################################################
###########                    END                   ##########
###############################################################
