import os
from functions_youtube.styles import bcolors_style
from styles import bcolors_style

#import bcolors_style


def check_ver_func():

    test = os.popen('youtube-dl --version').read()
    print("Your youtube-dl version is:\n" + bcolors_style.bcolors.OKGREEN + test + bcolors_style.bcolors.ENDC + "\n")


check_ver_func()