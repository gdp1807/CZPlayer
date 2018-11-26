# CZPlayer

CZPlayer is a song player and downloader for Ubuntu OS written in Python 3.x. It has been developed and tested on Ubuntu 18.04 OS.

# Pre-requisites

1. `youtube-dl`

    Install `youtube-dl` by running the following two commands on the terminal,

    `sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl`

    `sudo chmod a+rx /usr/local/bin/youtube-dl`

2. `playsound`

    Install `playsound` by running the following command on the terminal,

    `sudo pip3 install playsound`

    If you don't have `pip3` installed then install it by running the following
    command on the terminal,

    `sudo apt-get -y install python3-pip`

# Usage

Use `python3 czplayer.py help` to get information about usage.

# Customizing `Downloads/ongs.txt`

The format of `Dpwnloads/songs.txt` is as follows,
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
the above mentioned format.

# Short run plans
1. Allowing multiple playlists.
2. Accepting custom order of songs for playling.
3. Rectifying issues raised on github.
4. Adding more documentation.
5. Create a better `setup.py` file.

# Long run plans
1. Looping the playlists.
2. Pausing the songs.
3. Skipping a song.

Create issues to enjoy music via terminal.

Made with love by `Gagandeep Singh(singh.23@iitj.ac.in)`
