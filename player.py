from mutagen.mp3 import MP3
import pygame
import customtkinter
import tkinter
import os

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
pygame.mixer.init()

app = customtkinter.CTk()
app.geometry("600x500")
app.title("Music")
pygame.init()

def get_music():
    music_pos = music_list.curselection()
    
    if not music_pos: return None
    
    music = music_list.get(music_pos)
    
    return music

def play_sound():
    music = get_music()
    if not music: return # TODO: "selecione uma musica"
    
    global is_pause
    is_pause = False
    
    print(music)
    sound_mutagen = MP3(music)
    sound_duration = sound_mutagen.info.length
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()

    s = steps(sound_duration)
    update_progress_bar(s)

def update_progress_bar(gerador_steps):
    global is_pause
    
    if is_pause:
        app.after(100, lambda: update_progress_bar(gerador_steps))
        return
    
    try:
        t = next(gerador_steps)
        progress.set(t)
        app.after(10, lambda: update_progress_bar(gerador_steps))
        
    except:
        pass

def steps(valor_original):
    total_passos = int(valor_original * 100)  # cada 0.01s é um passo
    for passo in range(total_passos + 1):
        novo_valor = (passo / total_passos)  # valor de 0.0 até 1.0
        yield novo_valor

def pause_sound():
    global is_pause
    
    if is_pause:
        pygame.mixer.music.unpause()
        is_pause = False
        
    else:
        pygame.mixer.music.pause()
        is_pause = True


music_frame = tkinter.Frame(app, bg="#2e2e2e")
music_frame.pack(fill="both", expand=True)

music_list = tkinter.Listbox(music_frame, width=60, height=20)
music_list.pack(expand=True, padx=20, pady=5)

for item in os.listdir(os.getcwd()):
    if os.path.splitext(item)[-1] == ".mp3":
        music_list.insert(0, item)

play_button = customtkinter.CTkButton(app, text="Play", command=play_sound)
play_button.pack(pady=10)

pause_button = customtkinter.CTkButton(app, text="Pause", command=pause_sound)
pause_button.pack(pady=10)

progress = customtkinter.CTkProgressBar(app, width=400)
progress.pack(side="bottom", pady=(0, 40))

app.mainloop()
