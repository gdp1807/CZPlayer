import sys
import subprocess
import json
import os
from read_write import Read, Write

class Songs:
    def __init__(self):
        self.download_dict = {}
        self.read = Read()
        self.write = Write()
        self.output_path = ""
        self.input_file_path = ""
        self.sudo_pass = ""
        self.username = ""
        self.playlist = []

    def get_files(self, *args):
        if not os.path.exists(import_path + 'data/user_data.json') or len(args) == 4:
            self.output_path = args[0]
            if self.output_path[-1] != '/':
                self.output_path = self.output_path + '/'
            self.input_file_path = args[1]
            self.sudo_pass = args[2]
            self.username = args[3]
            if not os.path.exists(import_path + 'data/'):
                os.system('echo '+self.sudo_pass+' | sudo -S mkdir ' + import_path + 'data')
            self.write.set_file(import_path + 'data/user_data.json')
            self.write.write_user_json(self.output_path, self.input_file_path, self.username)
        elif len(args) == 1:
            self.sudo_pass = args[0]
            self.read.set_file(import_path + 'data/user_data.json')
            self.output_path, self.input_file_path, self.username = self.read.read_user_data()

    def get_download_list(self):
        self.read.set_file(import_path + 'playlists/universal.txt')
        self.playlist = self.read.read_playlist()
        self.read.set_file(import_path + 'Downloads/songs.txt')
        songs = self.read.read_requested_songs()
        for song in songs.keys():
            if song not in self.playlist:
                self.download_dict[song] = songs[song]

    def download(self):
        for song in self.download_dict.keys():
            self.playlist.append(song)
            download_command = 'youtube-dl --extract-audio --audio-format mp3 -o "' + import_path + self.output_path + song + '.mp3" '+self.download_dict[song]
            subprocess.call('echo '+self.sudo_pass+' | sudo -S ' + download_command, shell=True)
        self.write.set_file(import_path + 'playlists/universal.txt')
        self.write.write_playlist(self.playlist)
        subprocess.call('echo ' + self.sudo_pass + ' | sudo -S chown -R ' + self.username + ' ' + import_path + self.output_path, shell=True)
