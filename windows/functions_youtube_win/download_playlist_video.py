def download_playlist_video_func():
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
        
    url_var = input(bcolors.BOLD + "Which playlist ID? Paste your playlist ID and press enter.\n>>> " +bcolors.ENDC)
    print("\n\n")

    os.system('youtube-dl --ignore-errors --output "%(title)s.%(ext)s" --yes-playlist https://www.youtube.com/playlist?list=' + url_var)