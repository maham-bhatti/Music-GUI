import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize pygame mixer
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")
        self.root.config(bg = "Pink")
        self.root.resizable(False, False)

        self.current_track = None
        self.paused = False

        self.music_dir = os.path.join(os.path.expanduser("~"), "Desktop", "Music")
        self.playlist = self.load_music_files()
        
        self.track_label = tk.Label(self.root, fg='Purple', text='No track playing', font= 'Times_New_Roman', wraplength=300, bg= "Pink")
        self.track_label.pack(pady=10)

        self.play_button = tk.Button(self.root, text='Play', command=self.play_music, bg="White", fg="purple")
        self.play_button.pack(side=tk.LEFT, padx=20)

        self.pause_button = tk.Button(self.root, text='Pause', command=self.pause_music, bg="White",fg="purple")
        self.pause_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(self.root, text='Stop', command=self.stop_music, bg="white", fg="purple")
        self.stop_button.pack(side=tk.LEFT, padx=20)

        self.next_button = tk.Button(self.root, text='Next', command=self.next_track, bg="White", fg="purple")
        self.next_button.pack(side=tk.LEFT, padx=20)

        self.prev_button = tk.Button(self.root, text='Previous', command=self.prev_track, bg="White", fg="purple")
        self.prev_button.pack(side=tk.LEFT, padx=20)

        self.current_track_index = 0
        if self.playlist:
            self.update_track_label()

    def load_music_files(self):
        if not os.path.exists(self.music_dir):
            messagebox.showinfo("Info", "Music directory not found on desktop.")
            return []
        return [file for file in os.listdir(self.music_dir) if file.endswith(('.mp3'))]

    def play_music(self):
        if not self.playlist:
            messagebox.showinfo("Info", "No music files found in the directory.")
            return

        if self.current_track_index < 0 or self.current_track_index >= len(self.playlist):
            print("Invalid track number.")
            return
        
        self.current_track = os.path.join(self.music_dir, self.playlist[self.current_track_index])
        pygame.mixer.music.load(self.current_track)
        pygame.mixer.music.play()
        self.paused = False
        self.update_track_label()

    def pause_music(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            self.track_label.config(text=f"Playing: {self.playlist[self.current_track_index]}", fg="blue")
        else:
            pygame.mixer.music.pause()
            self.paused = True
            self.track_label.config(text=f"Paused: {self.playlist[self.current_track_index]}", fg="blue")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_track = None
        self.paused = False
        self.track_label.config(text="No track playing", fg="blue")

    def next_track(self):
        if not self.playlist:
            return
        self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        self.play_music()

    def prev_track(self):
        if not self.playlist:
            return
        self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        self.play_music()

    def update_track_label(self):
        if self.current_track:
            self.track_label.config(text=f"Playing: {self.playlist[self.current_track_index]}", fg="blue")
        else:
            self.track_label.config(text="No track playing", fg="blue")

def main():
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
if __name__ == "__main__":
    main()
