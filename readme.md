CZPlayer is a song player and downloader for Ubuntu OS written in Python 3.x. It has been developed and tested on Ubuntu 18.04 OS.

Pre-requisites:
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

Usage:

For downloading songs, you can try the following steps:
1. Make a folder `Songs` in your home directory.
2. Copy the files `playlist.txt` and `songs.txt` present in the `examples` folder
to the `Songs` folder.
3. Run on the terminal,
  ```
  `python3 song-dl.py path_to_your_home_directory/Songs/ path_to_your_home_directory/Songs/songs.txt your_sudo_password your_username_on_ubuntu`
  ```
The example song will be downloaded. After performing the above you will be able to download
your next song by simply running the following command,
```
  `python3 song-dl.py your_sudo_password`
```

For playing songs, you can try the following steps:
1. Change your current directory to `CZPlayer`.
2. Run on the terminal,
  ```
  `python3 play.py path_to_your_home_directory/Songs/playlist.txt path_to_your_home_directory/Songs/`
  ```
The example song will be played. After performing the above, you will be able to listen
to your playlist by simply writing,
```
`python3 play.py`
```

Customizing `songs.txt`
The format of `songs.txt` is as follows,
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

Short run plans:
1. Allowing multiple playlists.
2. Accepting custom order of songs for playling.
3. Rectifying issues raised on github.
4. Adding more documentation.

Long run plans:
1. Looping the playlists.
2. Pausing the songs.
3. Skipping a song.

Create issues to enjoy music via terminal.

Made with love by `Gagandeep Singh(singh.23@iitj.ac.in)`

