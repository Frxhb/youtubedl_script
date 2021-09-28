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

def check_os_func():

    string =  os.popen('hostnamectl').read()
    index = string.find('System:')
    Test2= (string[index:])
    indextwo = Test2.find('Kernel')
    os_sstring = (Test2[:indextwo])

    print(bcolors.OKBLUE + "Your system seems to be: " + os_sstring.partition(' ')[2] + bcolors.ENDC)
    time.sleep(1)