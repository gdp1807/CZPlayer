# CZPlayer

CZPlayer is a song player and downloader for Ubuntu OS written in Python 3.x. It has been developed and tested on Ubuntu 18.04 OS.

# Pre-requisites

1. `youtube-dl`

    Install `youtube-dl` by running the following two commands on the terminal,

    `sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl`

    `sudo chmod a+rx /usr/local/bin/youtube-dl`

2. `playsound`

    Install `playsound` by running the following command on the terminal,

    `sudo pip install playsound`

    If you don't have `pip3` installed then install it by running the following
    command on the terminal,

    `sudo apt-get -y install python-pip`

# Installation

1. Run, `sudo wget https://github.com/gdp1807/CZPlayer/archive/master.zip -O /usr/local/CZPlayer_Zip`
2. Run, `sudo unzip /usr/local/CZPlayer_Zip`
3. Run, `sudo mv /usr/local/CZPlayer-master /usr/local/CZPlayer`
4. Run, `python3 /usr/local/CZPlayer/setup.py your_sudo_password your_ubuntu_username`

# Usage

Use `czplayer help` to get information about usage.

# Backup
1. Run, `sudo mkdir /usr/local/CZPlayer_Backup/`
2. Run, `sudo cp -r /usr/local/CZPlayer/Downloads /usr/local/CZPlayer_Backup/`
3. Run, `sudo cp -r /usr/local/CZPlayer/playlists /usr/local/CZPlayer_Backup/`
4. Run, `sudo cp -r /usr/local/CZPlayer/data /usr/local/CZPlayer_Backup/`
This step is strictly recommended. If you will not backup your playlists after installation then it may lead to loss of Downloads, playlists and data on installing the updates. We will make the backingup process automatic in the upcoming updates. 

# Customizing `Downloads/songs.txt`

The format of `Downloads/songs.txt` is as follows,
```
<song_name_without_spaces> <youtube_link_of_the_song>
<song_name_without_spaces> <youtube_link_of_the_song>
<song_name_without_spaces> <youtube_link_of_the_song>
.
.
.
<song_name_without_spaces> <youtube_link_of_the_song>
```
For example, if the song is `Treat You Better`, then `songs.txt` will be like,
```
TreatYouBetter https://www.youtube.com/watch?v=lY2yjAdbvdQ
```
To add more songs to your playlist just add more lines to the `songs.txt` in
the above mentioned format. You can do that without sudo rights on gedit.

# Short run plans
1. Allowing multiple playlists.
2. Rectifying issues raised on github.
3. Adding more documentation.
4. Making it available via `apt-get`.
5. Automatic installation of pre-requisites.
6. Automatic backing up of songs.

# Long run plans
1. Looping the playlists.
2. Pausing the songs.
3. Skipping a song.
4. Making CZPlayer compatible on mac OS.

Create issues to enjoy music via terminal.

Made with love by `Gagandeep Singh(singh.23@iitj.ac.in)`
