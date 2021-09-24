def all_func_check():
    import os
    import time

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

    print(bcolors.HEADER + "Checking dependencies.....\n" + bcolors.ENDC)
    time.sleep(1)

    def youtube_dl_check():

        path_youtubedl = "/usr/local/bin/youtube-dl"
        global isfile_yt
        isfile_yt = os.path.isfile(path_youtubedl)

        if isfile_yt == True:
            
            print (bcolors.OKGREEN + "      Youtube dl is installed! ✓\n" +bcolors.ENDC)
        else:
            print (bcolors.WARNING + "      Youtube-dl isn't installed! ✕\n" +bcolors.ENDC)

    def ffmpeg_check():

        path_ffmpeg = "/usr/bin/ffmpeg"
        global isfile_ffmpeg
        isfile_ffmpeg = os.path.isfile(path_ffmpeg)

        if isfile_ffmpeg == True:
            print (bcolors.OKGREEN + "      ffmpeg is installed! ✓\n" +bcolors.ENDC)
        else:
            print (bcolors.WARNING + "      ffmpeg isn't installed! ✕\n" + bcolors.ENDC)

    youtube_dl_check()
    ffmpeg_check()


    if isfile_yt == False or isfile_ffmpeg == False:

        print ("In order to run this program, you need to download a few more dependencies:\n ")

        install_now = input("Do you want to install those dependencies now? Y/n\n>>> ")

        if install_now in ['yes', 'Yes', 'Y', 'y']:

            if isfile_yt == False:
                os.system("sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && sudo chmod a+rx /usr/local/bin/youtube-dl")

            if isfile_ffmpeg == False:
                os.system("sudo apt-get install ffmpeg")
        else:
            ("Okay, exiting now...")
    else:
        time.sleep(1)
        print (bcolors.BOLD + "Okay, we can continue!\n\n" + bcolors.ENDC)
        time.sleep(2)