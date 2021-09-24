def download_video_func():
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
        
    url_var = input(bcolors.BOLD + "Which URL? Paste URL and press enter.\n>>> " +bcolors.ENDC)
    print("\n\n")

    if "https://" in url_var:
        os.system('youtube-dl ' + url_var)
        os.system('mkdir -p ~/youtubedl_files')
        os.system('mkdir -p ~/youtubedl_files/videos')
        os.system('DUMMY=$(mv ./*.mp4 *.webm *.mkv ~/youtubedl_files/videos 2>&1)')

    else:
        print(bcolors.FAIL + "No Valid URL!" + bcolors.ENDC + bcolors.WARNING + " Please check your URL. You typed in:\n\n>>> " + url_var +bcolors.ENDC)