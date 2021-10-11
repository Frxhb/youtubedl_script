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

def Type_Abfrage():

    what_type = input(bcolors.OKGREEN + "Video [1] " +bcolors.ENDC + "or " +bcolors.OKBLUE + "Audio [2] " + bcolors.ENDC + "or " +bcolors.OKCYAN + "Playlist [SONGS] [3] " + bcolors.ENDC + bcolors.WARNING + "Playlist [Videos] [4] " + bcolors.ENDC + "?\n\nChoose a number and press enter!\n\n>>> ")

    if what_type == "1":
        print(bcolors.OKGREEN + "Okay, you chosed Video.\n" + bcolors.ENDC)
        from functions_youtube_win import download_video
        download_video.download_video_func()

    elif what_type== "2":
        print(bcolors.OKBLUE + "Okay, you chosed Audio.\n" + bcolors.ENDC)
        from functions_youtube_win import download_audio
        download_audio.download_audio_func()

    elif what_type== "3":
        print(bcolors.OKBLUE + "Okay, you chosed Playlist-Audio.\n" + bcolors.ENDC)
        from functions_youtube_win import download_playlist_audio
        download_playlist_audio.download_playlist_audio_func()

    elif what_type== "4":
        print(bcolors.OKBLUE + "Okay, you chosed Playlist-Video.\n" + bcolors.ENDC)
        from functions_youtube_win import download_playlist_video
        download_playlist_video.download_playlist_video_func()

    else:
        print(bcolors.FAIL + "Falsche Eingabe! Quitting program...\n" + bcolors.ENDC)
        time.sleep(1)
        exit()