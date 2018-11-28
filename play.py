import sys
import random
from playsound import playsound
from read_write import Read, Write
import os
import json

class Play:
    def __init__(self):
        self.order = ""
        self.playlist = []
        self.read = Read()

    def set_order(self, *args):
        self.order = args[0]
        if self.order == "custom":
            try:
                for song in args[1]:
                    self.playlist.append(song)
            except:
                raise Exception("Invalid format. Please use 'czplayer help' to get usage information.")

    def generate(self):
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
        self.read.set_file('playlists/universal.txt')
        if self.order == "random":
            self.playlist = self.read.read_playlist()
            rand_order = shuffle(0, len(self.playlist) - 1)
            new_playlist = []
            for i in rand_order:
                new_playlist.append(self.playlist[i])
            self.playlist = new_playlist
        elif self.order != "custom":
            raise Exception("Invalid type of playlist!Please use 'czplayer help' to get usage information.")

    def play(self):
        for song in self.playlist:
            print('Playing ' + song + '...')
            playsound('Downloads/' + song +'.mp3')
