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

def ffmpeg_check():

    path_ffmpeg = "/usr/bin/ffmpeg"
    global isfile_ffmpeg
    isfile_ffmpeg = os.path.isfile(path_ffmpeg)

    if isfile_ffmpeg == True:
        print(bcolors.OKGREEN + "      ffmpeg is installed! ✓\n" + bcolors.ENDC)
    else:
        print(bcolors.WARNING + "      ffmpeg isn't installed! ✕\n" + bcolors.ENDC)