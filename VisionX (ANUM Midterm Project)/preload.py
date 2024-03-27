'''
[!] SPLASH SCREEN FILE

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
import tkinter as tk
import tkinter.ttk as ttk
import random
import FalsePosition_Numeric
from tkinter import *

###############################################################
###########        WINDOW APPLICATION SETTING        ##########
###############################################################

class Preload:
    def switch_page(self):
        win = Toplevel()
        FalsePosition_Numeric.Home(win)
        self.window.withdraw()
        win.deiconify
        
    def __init__(self, window):
        self.window = window

        # initiate window w, h
        wind_w = 700 # width of window 
        wind_h = 400 # height of window

        # get screen w, h
        scr_w = window.winfo_screenwidth()
        scr_h = window.winfo_screenheight()

        # get coords of screen
        scr_coord_x = (scr_w/2) - (wind_w/2)
        scr_coord_y = (scr_h/2) - (wind_h/2)

        # universal variables
        uni_bg = "#0E0E0E"

        # config window 
        self.window.geometry("%dx%d+%d+%d" %(wind_w, wind_h, scr_coord_x, scr_coord_y))
        self.window.overrideredirect(1) # False = hide titlebar
        self.window.configure(bg=uni_bg)

###############################################################
###########        WINDOW APPLICATION CONTENT        ##########
###############################################################
        
        # initiate content frame
        frame = tk.Frame(master=self.window, width=wind_w, height=wind_h, bg=uni_bg).place(x=0, y=0)

        # application logo
        logo_path = "C:/Users/ngrok/Documents/[45] ANUM 2024/VisionX (ANUM Midterm Project)/logo_vision.png"
        self.logo = tk.PhotoImage(file=logo_path)
        resized_logo = self.logo.subsample(5, 5) # resize logo 1/5th
        logo_label = tk.Label(master=frame, image=resized_logo, bg=uni_bg)
        logo_label.image = resized_logo  # Store reference to the image to prevent garbage collection
        logo_lbl_w = logo_label.winfo_reqwidth()
        logo_lbl_x = (wind_w - logo_lbl_w)/2
        logo_label.place(x=logo_lbl_x, y=60)

        # application slogan
        slogan_label = tk.Label(master=frame, text="We Make it Happen", fg='white', bg=uni_bg)
        slogan_label.configure(font=("Poppins Regular", 11))
        slogan_lbl_w = slogan_label.winfo_reqwidth()
        slogan_lbl_x = (wind_w - slogan_lbl_w)/2
        slogan_label.place(x=slogan_lbl_x, y = 140)

        # application version
        version_label = tk.Label(master=frame, text='v1.0', fg='white', bg=uni_bg)
        version_label_w = version_label.winfo_reqwidth() 
        version_label_x  = wind_w - version_label_w - 20 
        version_label.configure(font=("Poppins", 11))
        version_label.place(x=version_label_x, y=wind_h - 35)

        # application credit
        author_label = tk.Label(master=frame, text='By John Bryan', fg='white', bg=uni_bg)
        author_label.configure(font=("Poppins Light", 11))
        author_label.place(x=10, y=wind_h - 35)

        # application loading bar
        loading_bar = ttk.Progressbar(master=frame, orient='horizontal',  mode='determinate', length=450)
        loading_bar_w = loading_bar.winfo_reqwidth()
        loading_bar_x = (wind_w - loading_bar_w)/2
        loading_bar.place(x=loading_bar_x, y=230)

        # application process label for loading bar
        process_label = tk.Label(master=frame, text="", fg='white', bg="#0E0E0E")
        process_label.configure(font=("Poppins Light", 8))
        process_label.place(relx=0.5, rely=0.7, anchor="center")

###############################################################
###########           TKINTER PAGE LOGIC             ##########
###############################################################

    # # switching pages
    # def switch_page(self):
    #     wind = Toplevel()

###############################################################
###########            LOADING BAR LOGIC             ##########
###############################################################
       
        # increase progress function
        def increase_progress():
            current_value = loading_bar['value'] # storing current value

            # random process (fiction/listed)
            rand_proc = [
                "Using willtru64xhaag.dll", 
                "Executing process_monitor.exe",
                "Loading data_analysis_module.dll",
                "Running system_diagnostic_tool.py",
                "Initializing neural_network_model.h5",
                "Applying image_processing_algorithm.cpp",
                "Utilizing encryption_module.dll",
                "Parsing log_files.log",
                "Accessing database_server.sql",
                "Launching user_interface.exe",
                "Optimizing performance with performance_tuning_tool.py",
                "Analyzing network_traffic.pcap",
                "Generating report with report_generator.py",
                "Compiling source_code.c",
                "Scanning for viruses with antivirus_scanner.exe",
                "Simulating user_interaction_scenario.py",
                "Deploying software_update_patch.exe",
                "Configuring network_settings.ini",
                "Debugging application with debugger_tool.exe",
                "Automating tasks with task_automation_script.py",
                "Monitoring system_health with health_monitor.dll"
            ]
            
            # loading logics, bars
            if current_value < 100:
                rand_index = random.randint(0, len(rand_proc) - 1)
                rand_msg = rand_proc[rand_index]
                if current_value == 30:
                    loading_bar.step(15)
                    process_label.config(text=rand_msg)
                    window.after(1000, increase_progress)
                elif current_value == 99:
                    self.switch_page()
                else:
                    loading_bar.step(1)  # increase by 1%
                    process_label.config(text=rand_msg)
                    window.after(40, increase_progress)

        # calling loading bar function 
        increase_progress()

def page():
    window = tk.Tk()
    Preload(window)
    # loop window
    window.mainloop()

if __name__ == '__main__':
    page()

###############################################################
###########                    END                   ##########
###############################################################