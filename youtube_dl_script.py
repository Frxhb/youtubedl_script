import time
import os

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

def main_programm():
    clear = lambda: os.system('clear')
    #clear()

    from functions_youtube import type_abfrage
    type_abfrage.Type_Abfrage()

main_programm()