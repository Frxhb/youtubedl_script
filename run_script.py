import os
import re
import time
import platform
from x_styles.bcolor import bcolors

os_name = platform.system()

matches_win = ["Windows" , "windows" , "Windows11" , "Windows10", "windows11" , "windows10" , "win"]
matches_linux = ["Linux" , "Debian" , "linux" , "ubuntu", "Ubuntu" , "Mint" , "raspberrypi"]

print("I am going to look for your OS.....")

search_list_win = ['windows' , 'Windows', 'Windows11' , 'Windows10' , 'windows10', 'windows11']
search_list_linux = ['Linux' , 'linux']


if re.compile('|'.join(search_list_win),re.IGNORECASE).search(os_name):
    print(bcolors.OKGREEN + "Your system seems to be Windows." + bcolors.ENDC)
    time.sleep(2)
    from windows import youtube_dl_script_win
elif re.compile('|'.join(search_list_linux),re.IGNORECASE).search(os_name):
    print(bcolors.OKGREEN + "Your system seems to be Linux." + bcolors.ENDC)
    time.sleep(2)
    from linux import youtube_dl_script_linux
else:
    print(bcolors.FAIL + "Error!\nClosing program now..." + bcolors.ENDC)
    time.sleep(2)
    exit()