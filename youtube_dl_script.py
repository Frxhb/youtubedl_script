import os
import time
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

main_programm()