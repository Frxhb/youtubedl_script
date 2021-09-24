import time
import os
from functions_youtube import check_installation
from functions_youtube import type_abfrage

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

def main_func():
    from functions_youtube import check_installation
    check_installation.all_func_check()

    type_abfrage.Type_Abfrage()

    global ask_run
    ask_run = input ("Would you like to continue? Y/n:\n>>> ")
    if ask_run in ['yes', 'Yes', 'Y', 'y']:
        main_func()
    else:
        print("Okay, close program now...")
        exit()

main_func()