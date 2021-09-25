import os

def mv_aud_func():

    os.system('mkdir -p ~/youtubedl_files')
    os.system('mkdir -p ~/youtubedl_files/audios')
    os.system('DUMMY=$(mv *.m4a *.webm *.aav *.aac *.wma *.ogg *.wav *.opus *.mp3 ~/youtubedl_files/audios 2>&1)')