#!/usr/bin/env python
import sys
from songdl import Songs
from play import Play
if sys.argv[1] == "download":
    downloader = Songs()
    if len(sys.argv) == 4:
        downloader.get_files('Downloads/', 'Downloads/songs.txt', sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        downloader.get_files(sys.argv[2])
    else:
        raise Exception("Invalid format! Please use 'czplayer help' to get usage information.")
    downloader.get_download_list()
    downloader.download()

elif sys.argv[1] == "play":
    player = Play()
    if len(sys.argv) == 4:
        player.set_order(sys.argv[2], sys.argv[3])
    else:
        player.set_order("random")
    player.generate()
    player.play()

elif sys.argv[1] == "help":
    print("Use CZPlayer by executing one of the following commands - ")
    print("'python3 czplayer.py help' for usage information.")
    print("'python3 czplayer.py download your_sudo_password your_username' for downloading songs present in Downloads/songs.txt. Playlist will be automatically updated.")
    print("'python3 czplayer.py download your_sudo_password' if you have executed the above command at least once.")
    print("'python3 czplayer.py play random' for listening to the songs in the playlist random order.")
    print("'python3 czplayer.py play custom [song_name_without_spaces, song_name_without_spaces, ..., song_name_without_spaces]'.")
    print("You can view the playlist by opening playlists/universal.txt.")

else:
    print("Invalid format! Please use 'czplayer help' to get usage information.")
