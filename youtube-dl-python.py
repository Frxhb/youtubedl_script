import os
import time
import glob

from tkinter import *
import tkinter as tk

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


def close_window(): 
    root.destroy() 

def retrieve_input():
    global inputValue
    inputValue=textbox1.get("1.0","end-1c")


def video_download():
    os.system('youtube-dl ' + inputValue)

def audio_download():
    os.system('youtube-dl ' + inputValue)    

'''
def show_url():
    textbox3.configure(state='normal')
    textbox3.delete('1.0', END)
    textbox3.insert(END, inputValue)
    textbox3.configure(state='disabled')
'''

def show_video_files():
    textbox2.configure(state='normal')
    textbox2.delete('1.0', END)
    textbox2.configure(state='disabled')
    initial_count = 0
    direc = ('./')
    files = os.listdir(direc)
    os.chdir(direc)
    textbox2.delete('1.0', END)
    for file in (glob.glob("*.mp4")):
        initial_count += 1
        textbox2.configure(state='normal')
        textbox2.insert(END, file + '\n\n\n')
        textbox2.configure(state='disabled')

    for file in (glob.glob("*.webm")):
        initial_count += 1
        textbox2.configure(state='normal')
        textbox2.insert(END, file + '\n\n\n')    
        textbox2.configure(state='disabled')


def show_audio_files():
    textbox2.configure(state='normal')
    textbox2.delete('1.0', END)
    textbox2.configure(state='disabled')
    initial_count = 0
    direc = ('./')
    files = os.listdir(direc)
    os.chdir(direc)
    for file in (glob.glob("*.aac")):
        initial_count += 1
        textbox2.configure(state='normal')
        textbox2.insert(END, file + '\n\n\n')
        textbox2.configure(state='disabled')
    
    for file in (glob.glob("*.m4a")):
        initial_count += 1
        textbox2.configure(state='normal')
        textbox2.insert(END, file + '\n\n\n')
        textbox2.configure(state='disabled')

    for file in (glob.glob("*.mkv")):
        initial_count += 1
        textbox2.configure(state='normal')
        textbox2.insert(END, file + '\n\n\n')
        textbox2.configure(state='disabled')

    for file in (glob.glob("*.mp3")):
        initial_count += 1
        textbox2.configure(state='normal')
        textbox2.insert(END, file + '\n\n\n')    
        textbox2.configure(state='disabled')


#Tk definition begins here:

root = Tk()
root.title("ADB GUI")
root.geometry("1100x700")
#root.eval('tk::PlaceWindow . center')


textbox1 = Text(root, height = 3, width = 40)
textbox1.grid(row=1, column=0, sticky="NW")
textbox1.configure(state='normal')

textbox2 = Text(root, height = 20, width = 75)
textbox2.grid(row=3, column=0,sticky="NW")
textbox2.configure(state='disabled')

textbox3 = Text(root, height = 3, width = 40)
textbox3.grid(row=5, column=0,sticky="NW")
textbox3.configure(state='disabled')

def show_url_box():
    textbox3.configure(state='normal')
    textbox3.delete('1.0', END)
    textbox3.insert(END, inputValue)
    textbox3.configure(state='disabled')


btn1 = Button(root, text="Video", command=video_download)
btn1.grid(row=1, column=2)

btn2 = Button(root, text="Audio",command=audio_download)
btn2.grid(row=1, column=3)

btn3 = Button(root, text="Cancel", bg="red", fg="white", command=close_window)
btn3.grid(row=5, column=3, sticky="SE")

btn4 = Button(root, text="Show Video Files",command=show_video_files)
btn4.grid(row=2, column=2, sticky="E")

btn5 = Button(root, text="Show Audio Files",command=show_audio_files)
btn5.grid(row=2, column=3, sticky="E")

'''
btn6 = Button(root, text="Show URL",command=show_url)
btn6.grid(row=4, column=3, sticky="E")
'''

buttonCommit=Button(root, height=1, width=10, text="Commit", command=lambda: [retrieve_input(), show_url_box()])
buttonCommit.grid(row=1, column=1)


lbl_url = Label(root)
lbl_url.grid(row=0, column=0, sticky="NW")
lbl_url.config(text="Insert URL here:")

lbl_download = Label(root)
lbl_download.grid(row=0, column=2, sticky="NE")
lbl_download.config(text="Download Option:")

lbl_status = Label(root)
lbl_status.grid(row=4, column=0, sticky="W")
lbl_status.config(text="Inserted URL:")

lbl_files = Label(root)
lbl_files.grid(row=2, column=0, sticky="W")
lbl_files.config(text="Files:")

root.mainloop()