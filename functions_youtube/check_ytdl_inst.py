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

def youtube_dl_check():

    path_youtubedl = "/usr/local/bin/youtube-dl"
    global isfile_yt
    isfile_yt = os.path.isfile(path_youtubedl)

    if isfile_yt == True:

        print(bcolors.OKGREEN + "      Youtube dl is installed! ✓\n" + bcolors.ENDC)
    else:
        print(bcolors.WARNING + "      Youtube-dl isn't installed! ✕\n" + bcolors.ENDC)