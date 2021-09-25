from functions_youtube import check_installation
from functions_youtube import type_abfrage
from functions_youtube import move_audios
from functions_youtube import move_videos

check_installation.all_func_check()

def main_func():

    move_audios.mv_aud_func()
    move_videos.mv_vid_func()
    type_abfrage.Type_Abfrage()

    global ask_run
    ask_run = input ("Would you like to continue? Y/n:\n>>> ")

    if ask_run in ['yes', 'Yes', 'Y', 'y']:

        main_func()
        move_audios.mv_aud_func()
        move_videos.mv_vid_func()

    else:

        print("Okay, close program now...")
        move_audios.mv_aud_func()
        move_videos.mv_vid_func()
        exit()

main_func()