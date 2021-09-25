# youtube-dl-py-script
Python script for youtube-dl



- [DISCLAIMER](#Disclaimer)
- [SYSTEM REQUIREMENTS](#system-requirements)
- [PREPARATION](#Preparation)
- [INSTALLATION](#Installation)
- [NOTES](#Notes)


## Disclaimer
In this script I use [Youtube-dl](https://github.com/ytdl-org/youtube-dl).


## System requirements?
Right now I tested this script with [Ubuntu 20.04.3 LTS](https://releases.ubuntu.com/20.04/) and [Debian 10](https://www.debian.org/index.de.html)

In order to run this script, few programs are needed. You can see it in [PREPARATION](#Preparation).

## Preparation

1. Update and upgrade packages:

```bash
sudo apt-get update && sudo apt-get upgrade
```

2.  Install python if you havent already (at least Python 3.6)
```bash
sudo apt-get install python3
```
3. If you havent already curl installed, install curl. I you have, move to step 4.
```bash
sudo apt-get install curl
```
4. Install [youtube-dl](https://github.com/ytdl-org/youtube-dl#installation)
```bash
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl

sudo chmod a+rx /usr/local/bin/youtube-dl
```
5. Sometimes python3 is a bit buggy, so you need to install python-is-python3:
```bash
sudo apt-get install python-is-python3
```
## Installation

1. Clone this git repository:
```bash
git clone git@github.com:Frxhb/youtube-dl-py-script.git
```
2. cd into cloned directory.
```bash
cd /path/to/directory
```
3. Change permissions:
```bash
chmod +x youtube_dl_script.py
```
4. Run script with python:
```bash
python3 youtube_dl_script.py
```

## Notes

You will find your files in your users folder e.g.: 
<br>
<br>
```bash
/home/$USR/youtubedl_files/audios
```

or <br>

```bash
/home/$USR/youtubedl_files/videos
```
<br> 
Enjoy!