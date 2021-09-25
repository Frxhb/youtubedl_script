import time
import os
from functions_youtube import check_installation
from functions_youtube import type_abfrage

check_installation.all_func_check()

def main_func():

    type_abfrage.Type_Abfrage()

    global ask_run
    ask_run = input ("Would you like to continue? Y/n:\n>>> ")
    if ask_run in ['yes', 'Yes', 'Y', 'y']:
        main_func()
    else:
        print("Okay, close program now...")
        exit()

main_func()