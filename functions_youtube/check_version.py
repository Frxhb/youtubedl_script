import os

from youtube-dl-py-sc

def check_ver_func():

    test = os.popen('youtube-dl --version').read()
    print("Your youtube-dl version is:\n" + bcolors_style.bcolors.OKGREEN + test + bcolors_style.bcolors.ENDC + "\n")