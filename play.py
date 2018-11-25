import vlc
import sys
import random
from playsound import playsound
from write_to_json import write_json
import os
import json

def shuffle(l, u):
    """
    This method is used for shuffling the songs in the playlist.
    """
    order = []
    for i in range(l, u+1):
        num = random.randint(l, u)
        while num in order:
            num = random.randint(l, u)
        order.append(num)
    return order

def read_json(file):
    """
    This method is used for reading data from player_data.json
    """
    file_json = open(file, 'r')
    json_decode = json.load(file_json)
    playlist = json_decode["playlist"]
    songs = json_decode["songs"]
    return (playlist, songs)

if len(sys.argv) == 3 or not os.path.exists('player_data.json'):
    playlist = sys.argv[1]
    songs = sys.argv[2]
    write_json('player_data.json', playlist, songs)
else:
    playlist, songs = read_json('player_data.json')
    print(playlist, songs)

file = open(playlist, 'r')
song = file.readline()
song_list = []
while song != "":
    song_list.append(song.rstrip('\n'))
    song = file.readline()
queue = shuffle(0, len(song_list) - 1)
for index in queue:
    print('Playing ' + song_list[index] + '...')
    playsound(songs + song_list[index] + '.mp3')
