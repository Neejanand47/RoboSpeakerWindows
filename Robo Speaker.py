#First Import OS Module
# Its a Robo Speaker Program Windows Version
import os

if __name__ == '__main__':
    print("Welcome to robo speaker, created by Ankit")
    while (True):
         x = input(" enter what you want to pronounce: ")
         if x == "q":
             break
         command = f"PowerSHELL -Command "f"Add-Type -AssemblyName System.Speech;" \
                   f" (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"
         os.system(command)