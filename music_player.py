# music_player.py

import pygame
import os
from tkinter import Tk, Button, Label, Scale

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x200")

        pygame.init()

        self.track_list = []
        self.current_track_index = 0

        self.load_tracks()
        self.load_ui()

    def load_tracks(self):
        # Add your music files to the 'music' folder and specify the folder path below
        music_folder = "music"
        for file in os.listdir(music_folder):
            if file.endswith(".mp3"):
                self.track_list.append(os.path.join(music_folder, file))

    def play_track(self):
        pygame.mixer.music.load(self.track_list[self.current_track_index])
        pygame.mixer.music.play()

    def pause_track(self):
        pygame.mixer.music.pause()

    def unpause_track(self):
        pygame.mixer.music.unpause()

    def stop_track(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.current_track_index = (self.current_track_index + 1) % len(self.track_list)
        self.play_track()

    def previous_track(self):
        self.current_track_index = (self.current_track_index - 1) % len(self.track_list)
        self.play_track()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume / 100)

    def load_ui(self):
        play_button = Button(self.root, text="Play", command=self.play_track)
        play_button.pack()

        pause_button = Button(self.root, text="Pause", command=self.pause_track)
        pause_button.pack()

        unpause_button = Button(self.root, text="Unpause", command=self.unpause_track)
        unpause_button.pack()

        stop_button = Button(self.root, text="Stop", command=self.stop_track)
        stop_button.pack()

        previous_button = Button(self.root, text="Previous", command=self.previous_track)
        previous_button.pack()

        next_button = Button(self.root, text="Next", command=self.next_track)
        next_button.pack()

        volume_label = Label(self.root, text="Volume:")
        volume_label.pack()

        volume_scale = Scale(self.root, from_=0, to=100, orient="horizontal", command=self.set_volume)
        volume_scale.pack()

def main():
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
