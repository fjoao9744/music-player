# bibliotecas padrão
import os

# bibliotecas de interface
import tkinter as tk
import customtkinter as ctk

# biblitecas para audio
from mutagen.mp3 import MP3
import pygame.mixer

class App(ctk.CTk):
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("green")
    
    def __init__(self):
        super().__init__()
        pygame.init()
        self.geometry("600x500")
        self.title("Music")
        self.configure(fg_color="#1C2D33")
        
        # lista de musicas
        musics_frame = tk.Frame(self, bg="#024059")
        musics_frame.pack(fill="both", expand=True)
        
        self.musics_list = tk.Listbox(musics_frame, width=60, height=13, background="#026873", fg="#04BF8A", justify="center", relief="flat", activestyle="none")
        self.musics_list.pack(expand=True, pady=5)
        
        for file in os.listdir(os.getcwd()):
            if os.path.splitext(file)[-1] == ".mp3":
                self.musics_list.insert(0, file)
                
        # opções
        
        play_button = ctk.CTkButton(self, text="Play", command=self.play_sound, fg_color="#025940", corner_radius=20)
        play_button.pack(pady=(10, 0))
        
        pause_button = ctk.CTkButton(self, text="Pause", command=self.pause_sound, fg_color="#025940", corner_radius=20)
        pause_button.pack(pady=10)
        
        self.progress = ctk.CTkProgressBar(self, width=400, fg_color="#025940")
        self.progress.pack(side="bottom", pady=(0, 40))
        
        self.is_pause = False
        
        self.slider = ctk.CTkSlider(self, from_=0, to=1, command=self.change_volume, fg_color="#025940")
        self.slider.pack(pady=10)
        
    def play_sound(self):
        self.music = self.get_music()
        
        if not self.music: return # TODO: "selecione uma musica"
        
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play()
        
        self.steps_gerador = self.steps()
        self.progress_bar()
        
    def pause_sound(self):
        if self.is_pause:
            pygame.mixer.music.unpause()
            self.is_pause = False
            self.progress_bar()
            
        else:
            pygame.mixer.music.pause()
            self.is_pause = True
        
    def get_music(self):
        music_pos = self.musics_list.curselection()
        
        if not music_pos: return None
                
        return self.musics_list.get(music_pos)
    
    def get_sound_duration(self):
        sound_mutagen = MP3(self.music)
        sound_duration = sound_mutagen.info.length
        return sound_duration

    def progress_bar(self):
        if self.is_pause or not pygame.mixer.music.get_busy():
           return
        
        try:
            t = next(self.steps_gerador)
            self.progress.set(t)
            self.after(10, self.progress_bar)
            
        except StopIteration:
            pass
            
    def steps(self):
        total_steps = int(self.get_sound_duration() * 100) # porcentagem
        for step in range(total_steps + 1):
            new_step = step / total_steps # 0.0 até 1.0
            yield new_step
    
    def change_volume(self, value):
        pygame.mixer.music.set_volume(value)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()


