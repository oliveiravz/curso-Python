from pygame import mixer

# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

mixer.init()
mixer.music.load('mcpoze.mp3')
mixer.music.set_volume(10.0)
mixer.music.play()
