import os
import time
import subprocess

from tkinter import *
import tkinter as tk
import string
from typing import Collection

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main_programm():
    clear = lambda: os.system('clear')
    clear()
    def re_run():
        clear()
        ask_re_run = input("Re run? Y/n:\n>>> ")
        if ask_re_run in ['yes', 'Yes', 'Y', 'y']:
            main_programm()
        else:
            print("Exiting program...")
            time.sleep(1)
            exit()

    def youtubedl_video():
        os.system('youtube-dl ' + URL_Abfrage)
        print("\n\n")

    def youtubedl_audio():
        os.system('youtube-dl -x --audio-format best ' + URL_Abfrage)
        print("\n\n")

    URL_Abfrage = input("Which URL? Paste URL and press enter.\n>>> ")

    Type_Abfrage = input("Video [1] or Audio [2] ?\n>>> ")

    if Type_Abfrage == "1":
        print("Okay, you chosed Video.")
        youtubedl_video()

    elif Type_Abfrage == "2":
        print("Okay, you chosed Audio.")
        youtubedl_audio()

    else:
        print(bcolors.WARNING + "Falsche Eingabe!\n" + bcolors.ENDC)

    re_run()

#main_programm()


def close_window(): 
    root.destroy() 

def retrieve_input():
    global inputValue
    inputValue=text2.get("1.0","end-1c")


def video_download():
    os.popen('youtube-dl ' + inputValue)

def audio_download():
    os.popen('youtube-dl ' + inputValue)    


def get_work_output_video():
    out = subprocess.run(["youtube-dl", inputValue], capture_output=True)
    text3.insert(END, out)

def get_work_output_audio():
    out = subprocess.run(["youtube-dl" , "-x" ,  "--audio-format",  "best", inputValue], capture_output=True)
    text3.insert(END, out)


######TK

root = Tk()
root.title("ADB GUI")
root.geometry("900x700")
#root.eval('tk::PlaceWindow . center')

btn1 = Button(root, text="Video", command=get_work_output_video)
#=video_download)
btn1.grid(row=1, column=1)

btn2 = Button(root, text="Audio",command=get_work_output_audio)
#=audio_download)
btn2.grid(row=1, column=2)

btn3 = Button(root, text="Cancel",command=close_window)
btn3.grid(row=3, column=3)

buttonCommit=Button(root, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())
buttonCommit.grid(row=3, column=0)


text2 = Text(root, height = 2, width = 30)
text2.grid(row=1, column=0)
text2.configure(state='normal')

text3 = Text(root)
text3 = Text(root, height = 10, width = 50)
text3.grid(row=2, column=0)
#text3.insert(END, output)


lbl_phone_status = Label(root, font=("times", 15))
lbl_phone_status.grid(row=0, column=0)
lbl_phone_status.config(text="URL")

root.mainloop()