import time
import os

def re_run_func():
    ask_re_run = input("Re run? Y/n:\n>>> ")

    if ask_re_run in ['yes', 'Yes', 'Y', 'y']:
        clear()
        from functions_youtube import type_abfrage
        type_abfrage.Type_Abfrage()

    else:
        print("Exiting program...")
        time.sleep(1)
        exit()