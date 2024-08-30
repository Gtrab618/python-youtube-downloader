import os
import threading

import pygame

# Inicializar el módulo de mezcla de pygame
pygame.mixer.init()

def play_sound(file_path):
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    while pygame.mixer.get_busy():
        pygame.time.delay(100)

def start_playing_error():
    gif_relativeLoad = os.path.join("..", "assets", "error.wav")
    sound_thread = threading.Thread(target=play_sound, args=(gif_relativeLoad,))
    sound_thread.start()

def start_playing_saved():
    gif_relativeLoad = os.path.join("..", "assets", "saved.wav")  # Cambia el archivo si es necesario
    sound_thread = threading.Thread(target=play_sound, args=(gif_relativeLoad,))
    sound_thread.start()

def start_playing_search():
    gif_relativeLoad = os.path.join("..", "assets", "search.wav")  # Cambia el archivo si es necesario
    sound_thread = threading.Thread(target=play_sound, args=(gif_relativeLoad,))
    sound_thread.start()