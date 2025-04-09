import os
import random
import pygame
from mutagen.mp3 import MP3

class AudioControls:
    def __init__(self, folder_muzyki="."):
        self.folder_muzyki = folder_muzyki
        self.playlista = [file for file in os.listdir(folder_muzyki) if file.endswith(".mp3")]
        self.index_piosenki = 0
        self.loop = False
        self.shuffle = False

        pygame.mixer.init()
        self.channel = pygame.mixer.music

        if self.playlista:
            self.load_song(self.playlista[self.index_piosenki])

    def load_song(self, filename):
        self.current_file = os.path.join(self.folder_muzyki, filename)
        self.channel.load(self.current_file)
        self.audio = MP3(self.current_file)

    def play(self):
        self.channel.play()

    def pause(self):
        self.channel.pause()

    def unpause(self):
        self.channel.unpause()

    def stop(self):
        self.channel.stop()

    def restart(self):
        self.channel.play(start=0.0)

    def set_volume(self, volume):
        self.channel.set_volume(volume)

    def get_position(self):
        return self.channel.get_pos() // 1000

    def get_length(self):
        return int(self.audio.info.length) if hasattr(self, 'audio') else 0

    def get_current_title(self):
        return os.path.basename(self.current_file)

    def get_bitrate(self):
        return int(self.audio.info.bitrate / 1000)  # kbps

    def get_mixrate(self):
        return self.audio.info.sample_rate  # Hz

    def toggle_loop(self):
        self.loop = not self.loop

    def toggle_shuffle(self):
        self.shuffle = not self.shuffle

    def is_playing(self):
        return pygame.mixer.music.get_busy()