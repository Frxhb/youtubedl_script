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


from functions_youtube import check_installation
check_installation.all_func_check()

def main_func():
    type_abfrage.Type_Abfrage()
    ask_run = input ("Would you like to continue? Y/n:\n>>> ")
    if ask_run in ['yes', 'Yes', 'Y', 'y']:
        ""
    else:
        print("okay program will close...")
        exit()

global ask_re_run
ask_re_run = input("Would you like to start? Y/n:\n>>> ")

if ask_re_run == "y":
    ask_re_run = True

elif ask_re_run == "n":
    ask_re_run = False

while ask_re_run == "y":
    main_func()
else:
    print("End..")
    exit()