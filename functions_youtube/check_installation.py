import os
import time

from functions_youtube import check_update
from functions_youtube import check_version
from functions_youtube import check_os

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

clear = lambda: os.system('clear')
clear()

check_os.check_os_func()

def all_func_check():

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

    print(bcolors.HEADER + "Checking dependencies.....\n" + bcolors.ENDC)
    time.sleep(1)

    def youtube_dl_check():

        path_youtubedl = "/usr/local/bin/youtube-dl"
        global isfile_yt
        isfile_yt = os.path.isfile(path_youtubedl)

        if isfile_yt == True:
            
            print (bcolors.OKGREEN + "      youtube dl is installed! ✓\n" +bcolors.ENDC)
        else:
            print (bcolors.WARNING + "      youtube-dl isn't installed! ✕\n" +bcolors.ENDC)

    def ffmpeg_check():

        path_ffmpeg = "/usr/bin/ffmpeg"
        global isfile_ffmpeg
        isfile_ffmpeg = os.path.isfile(path_ffmpeg)

        if isfile_ffmpeg == True:
            print (bcolors.OKGREEN + "      ffmpeg is installed! ✓\n" +bcolors.ENDC)
        else:
            print (bcolors.WARNING + "      ffmpeg isn't installed! ✕\n" + bcolors.ENDC)

    def curl_check():

        path_curl = "/usr/bin/curl"
        global isfile_curl
        isfile_curl = os.path.isfile(path_curl)

        if isfile_curl == True:
            print (bcolors.OKGREEN + "      curl is installed! ✓\n" +bcolors.ENDC)
        else:
            print (bcolors.WARNING + "      curl isn't installed! ✕\n" + bcolors.ENDC)

    youtube_dl_check()
    ffmpeg_check()
    curl_check()

    if isfile_yt == False or isfile_ffmpeg == False or isfile_curl == False:

        print ("In order to run this program, you need to download a few more dependencies:\n ")

        install_now = input("Do you want to install those dependencies now? Y/n\n>>> ")

        if install_now in ['yes', 'Yes', 'Y', 'y']:

            if isfile_yt == False:
                os.system("sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && sudo chmod a+rx /usr/local/bin/youtube-dl")
                print("\n\n")
                
            elif isfile_ffmpeg == False:
                os.system("sudo apt-get install ffmpeg")
                print("\n\n")
            
            elif isfile_curl == False:
                os.system("sudo apt-get install curl")
                print("\n\n")

        else:
            ("Okay, exiting now...")
    else:
        time.sleep(1)
        check_update.update_func()
        check_version.check_ver_func()
        print (bcolors.BOLD + "Okay, we can continue!\n\n" + bcolors.ENDC)
        print ("\n\n")