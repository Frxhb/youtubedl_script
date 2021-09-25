import os

def mv_vid_func():

    os.system('mkdir -p ~/youtubedl_files')
    os.system('mkdir -p ~/youtubedl_files/videos')
    os.system('DUMMY=$(mv *.mp4 *.webm *.mkv ~/youtubedl_files/videos 2>&1)')