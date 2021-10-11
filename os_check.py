global os_check_func
def os_check_func():

    import time
    import platform

    global os_name
    os_name = platform.system()
    global fullstring
    fullstring = os_name

    global matches_win
    matches_win = ["Windows" , "windows" , "Windows11" , "Windows10", "windows11" , "windows10" , "win"]
    global matches_linux
    matches_linux = ["Linux" , "Debian" , "linux" , "ubuntu", "Ubuntu" , "Mint" , "raspberrypi"]

    print("I am going to look for your OS.....")

    time.sleep(1)

    if any (x in fullstring for x in matches_win):
        print("Your device seems to be Windows!")
    elif any (x in fullstring for x in matches_linux):
        print("Your device seems to be Linux!")
        print("Couldn't detect your system.")