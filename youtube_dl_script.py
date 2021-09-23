import os
import time

from functions_youtube import type_abfrage
from functions_youtube import url_abfrage
from functions_youtube import download_audio
from functions_youtube import download_video

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

    type_abfrage

    if type_abfrage.Type_Abfrage_func == "1":
        print("Okay, you chosed Video.")
        download_video()

    elif type_abfrage.Type_Abfrage_func == "2":
        print("Okay, you chosed Audio.")
        download_audio()

    else:
        print(bcolors.WARNING + "Falsche Eingabe!\n" + bcolors.ENDC)

    re_run()

main_programm()