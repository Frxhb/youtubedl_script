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

    what_type = input(bcolors.OKGREEN + "Video [1] " +bcolors.ENDC + "or " +bcolors.OKBLUE + "Audio [2] " + bcolors.ENDC + "?\n\n>>> ")

    if what_type == "1":
        print(bcolors.OKGREEN + "Okay, you chosed Video.\n" + bcolors.ENDC)
        from functions_youtube import download_video
        download_video

    elif what_type== "2":
        print(bcolors.OKBLUE + "Okay, you chosed Audio.\n" + bcolors.ENDC)
        from functions_youtube import download_audio
        download_audio

    else:
        print(bcolors.FAIL + "Falsche Eingabe!\n" + bcolors.ENDC)
        from functions_youtube import re_run
        re_run.re_run_func()