import sys
import subprocess
import json
import os
from write_to_json import write_json

def read_json(file):
    """
    This method is used for reading data from data.json.
    """
    file_json = open(file, 'r')
    json_decode = json.load(file_json)
    output_path = json_decode["output_path"]
    input_file_path = json_decode["input_file_path"]
    username = json_decode["username"]
    return (output_path, input_file_path, username)

if not os.path.exists('data.json') or len(sys.argv) == 5:
    output_path = sys.argv[1]
    if output_path[-1] != '/':
        output_path = output_path + '/'
    input_file_path = sys.argv[2]
    sudo_pass = sys.argv[3]
    username = sys.argv[4]
    write_json('data.json', output_path, input_file_path, sudo_pass, username)
else:
    sudo_pass = sys.argv[1]
    output_path, input_file_path, username = read_json('data.json')

file_songs = open(input_file_path, 'r')
downloaded = []
file_playlist = open(output_path + 'playlist.txt', 'r')
song = file_playlist.readline()
while song != "":
    downloaded.append(song.rstrip('\n'))
    song = file_playlist.readline()

file_playlist = open(output_path + 'playlist.txt', 'w')
line = file_songs.readline()
while line != "":
     song, y_link = line.split(" ")
     if song not in downloaded:
         download_command = 'youtube-dl --extract-audio --audio-format mp3 -o "' + output_path + song + '.mp3" '+y_link
         subprocess.call('echo '+sudo_pass+' | sudo -S ' + download_command, shell=True)
     file_playlist.write(song + '\n')
     line = file_songs.readline()

subprocess.call('echo ' + sudo_pass + ' | sudo -S chown -R ' + username + ' ' + output_path, shell=True)
