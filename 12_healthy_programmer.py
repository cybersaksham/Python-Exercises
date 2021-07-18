"""
You work against computer from 9am - 5pm
So you should foolow these steps for your health
Water - water.mp3 - every 30 min (1 glass) - enter drank to close & log it
Eyes - eyes.mp3 - every 30 min - enter Eydone to close & log it
Physical activity - physical.mp3 - every 45 min - enter Exdone to close & log it
Use Pygame module for play audio
"""

from pygame import mixer
from datetime import datetime
from time import time


def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    while True:
        mixer.music.play()
        a = input(f"Type {stopper} to stop music - ")
        if a == stopper:
            mixer.music.stop()
            break


def log(msg):
    with open("E12 log data.txt", "a") as f:
        f.write(f"{msg} --> {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exer = time()

    watersec = 5
    eyessec = 10
    exersec = 20

    while True:
        if time() - init_water > watersec:
            print("Drinking water alarm.")
            musicloop("water.mp3", "drank")
            init_water = time()
            log("Drank water at")
        if time() - init_eyes > eyessec:
            print("Exercise eyes alarm.")
            musicloop("eyes.mp3", "done-eyes")
            init_eyes = time()
            log("Done eye exercise at")
        if time() - init_exer > exersec:
            print("Physical exercise alarm.")
            musicloop("physical.mp3", "done-exer")
            init_exer = time()
            log("Physical activity at")
