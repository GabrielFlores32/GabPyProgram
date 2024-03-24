#program 3
#create a program that gather user's info and adding fancy text 
#gather users information(name, gender, age,date of birth, dream job)

#add customtkinter
import customtkinter
import customtkinter as ctk
import tkinter
from art import *

#theme
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("100% safe window promise") #window title
app.geometry("500x500") #window size
frame = customtkinter.CTkFrame(master=app,
                               width=350,
                               height=350,
                               corner_radius=10)
frame.pack(padx=20, pady=20)

name_entry=customtkinter.CTkEntry(master=frame,
                                  placeholder_text="Name",
                                  width=150,
                                  height=30,
                                  border_width=2,
                                  corner_radius=10)
name_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

age_entry=customtkinter.CTkEntry(master=frame,
                                  placeholder_text="Age",
                                  width=150,
                                  height=30,
                                  border_width=2,
                                  corner_radius=10)
age_entry.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

date_of_birth_entry=customtkinter.CTkEntry(master=frame,
                                  placeholder_text="Date of Birth",
                                  width=150,
                                  height=30,
                                  border_width=2,
                                  corner_radius=10)
date_of_birth_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

optionmenu_var = customtkinter.StringVar(value="")
gender_combobox = customtkinter.CTkComboBox(master=frame,
                                            values=["Male","Female"],
                                            variable=optionmenu_var)
gender_combobox.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

dream_job_entry=customtkinter.CTkEntry(master=frame,
                                  placeholder_text="Dream job",
                                  width=150,
                                  height=30,
                                  border_width=2,
                                  corner_radius=10)
dream_job_entry.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)


def button_function():
    name=str(name_entry.get())
    age=str(age_entry.get())
    date_of_birth=str(date_of_birth_entry.get())
    gender=str(gender_combobox.get())
    dream_job=str(dream_job_entry.get())
    styled_name = text2art(name, font='block',chr_ignore=True)
    styled_age = text2art(age, font='block',chr_ignore=True)
    styled_date_of_birth = text2art(date_of_birth,"rand")
    styled_gender = text2art(gender, font='block',chr_ignore=True)
    styled_dream_job = text2art(dream_job,"rand")
    print("""
██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░██╗
██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗██║
███████║█████╗░░██║░░░░░██║░░░░░██║░░██║██║
██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║╚═╝
██║░░██║███████╗███████╗███████╗╚█████╔╝██╗
╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░╚═╝""""\033[1;36m" + styled_name, styled_age, styled_date_of_birth, styled_gender, """
░█████╗░██╗░░░██╗██████╗░  ███████╗██╗░░░██╗████████╗██╗░░░██╗██████╗░███████╗
██╔══██╗██║░░░██║██╔══██╗  ██╔════╝██║░░░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝
██║░░██║██║░░░██║██████╔╝  █████╗░░██║░░░██║░░░██║░░░██║░░░██║██████╔╝█████╗░░
██║░░██║██║░░░██║██╔══██╗  ██╔══╝░░██║░░░██║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░
╚█████╔╝╚██████╔╝██║░░██║  ██║░░░░░╚██████╔╝░░░██║░░░╚██████╔╝██║░░██║███████╗
░╚════╝░░╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝""""\033[1;35m" + styled_dream_job)

button = customtkinter.CTkButton(master=app, text ="Click the buttom if you like to share your personal info",command=button_function)
button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
app.mainloop()

