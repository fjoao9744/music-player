from mutagen.mp3 import MP3
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

def get_music():
    music = music_list.get(music_list.curselection())

    return music

def play_sound():
    music = get_music()
    sound_mutagen = MP3(music)
    sound_duration = sound_mutagen.info.length
    print(sound_duration)

    sound = pygame.mixer.Sound(music)
    sound.play()

    progress.set(0)
    for t in range(101):
        time.sleep(0.01)
        progress.set((t / sound_duration) )
        app.update_idletasks()
        
music_frame = tkinter.Frame(app, bg="#2e2e2e")
music_frame.pack(fill="both", expand=True)

music_list = tkinter.Listbox(music_frame, width=60, height=20)
music_list.pack(expand=True, padx=20, pady=5)

for item in os.listdir(os.getcwd()):
    if os.path.splitext(item)[-1] == ".mp3":
        music_list.insert(0, item)

pause_button = customtkinter.CTkButton(app, text="Pause", command=play_sound)
pause_button.pack(pady=10)

progress = customtkinter.CTkProgressBar(app, width=400)
progress.pack(side="bottom", pady=(0, 40))

app.mainloop()
