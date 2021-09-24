"""

import time
import os

def re_run_func():
    global ask_re_run
    ask_re_run = input("Re run? Y/n:\n>>> ")

    if ask_re_run in ['yes', 'Yes', 'Y', 'y']:
        clear = lambda: os.system('clear')
        clear()
        import youtube_dl_script
        youtube_dl_script.main_programm()

    else:
        print("Exiting program...")
        time.sleep(1)
        exit()

"""