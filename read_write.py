import json
class Read:
    def __init__(self):
        self.file = ""

    def set_file(self, *args):
        self.file = args[0]

    def read_user_data(self):
        """
        This method is used for reading data from data.json.
        """
        file_json = open(self.file, 'r')
        json_decode = json.load(file_json)
        output_path = json_decode["output_path"]
        input_file_path = json_decode["input_file_path"]
        username = json_decode["username"]
        return (output_path, input_file_path, username)

    def read_player_data(self):
        """
        This method is used for reading data from player_data.json
        """
        file_json = open(self.file, 'r')
        json_decode = json.load(file_json)
        playlist = json_decode["playlist"]
        songs = json_decode["songs"]
        return (songs, playlist)

    def read_playlist(self):
        file_txt = open(self.file, 'r')
        playlist = []
        song = file_txt.readline()
        while song != "":
            playlist.append(song.rstrip('\n'))
            song = file_txt.readline()
        return playlist

    def read_requested_songs(self):
        file_txt = open(self.file, 'r')
        songs = {}
        line = file_txt.readline()
        while line != "":
            line = line.rstrip('\n')
            song, y_link = line.split(" ")
            songs[song] = y_link
            line = file_txt.readline()
        return songs

class Write:
    def __init__(self):
        self.paths = {}
        self.file = ""

    def set_file(self, *args):
        self.file = args[0]

    def write_user_json(self, *args):
        self.paths["output_path"] = args[0]
        self.paths["input_file_path"] = args[1]
        self.paths["username"] = args[2]
        file_json = open(self.file, 'w')
        json.dump(self.paths, file_json)

    def write_player_json(self, *args):
        self.paths["playlist"] = args[0]
        self.paths["songs"] = args[1]
        file_json = open(self.file, 'w')
        json.dump(self.paths, file_json)

    def write_playlist(self, *args):
        playlist = args[0]
        file_txt = open(self.file, 'w')
        for song in playlist:
            file_txt.write(song+'\n')
