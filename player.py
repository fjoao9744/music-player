import pygame
import customtkinter
import tkinter
import os
import threading
import time

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x500")
pygame.init()

def play_music(music = ""): #TODO: pegar o nome da musica pegando o item selecionado no listbox
    sound = pygame.mixer.Sound(music)

    sound.play()

    progress.set(0)
    for t in range(101):
        time.sleep(0.01)
        progress.set(t / 100)  
        app.update_idletasks()
        
    pygame.quit()

music_frame = tkinter.Frame(app, bg="#2e2e2e")
music_frame.pack(fill="both", expand=True)

music_list = tkinter.Listbox(music_frame, width=60, height=20)
music_list.pack(expand=True, padx=20, pady=5)

for item in os.listdir(os.getcwd()):
    music_list.insert(0, item)

pause_button = customtkinter.CTkButton(app, text="Pause", command=play_music)
pause_button.pack(pady=10)

progress = customtkinter.CTkProgressBar(app, width=400)
progress.pack(side="bottom", pady=(0, 40))

app.mainloop()

