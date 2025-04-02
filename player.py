import pygame.mixer
import customtkinter
import tkinter
import os
import threading
import time

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x500")

music_frame = tkinter.Frame(app, bg="#2e2e2e")
music_frame.pack(fill="both", expand=True)

music_list = tkinter.Listbox(music_frame, width=60, height=20)
music_list.pack(expand=True, padx=20, pady=5)

for item in os.listdir(os.getcwd()):
    music_list.insert(0, item)

pause_button = customtkinter.CTkButton(app, text="Pause")
pause_button.pack(pady=10)

progress = customtkinter.CTkProgressBar(app, width=400)
progress.pack(side="bottom", pady=(0, 40))
progress.set(0)

app.mainloop()
