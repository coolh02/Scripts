# Libraries to use
import pathlib
from os import listdir, mkdir
from os.path import join, isdir
from shutil import copy
import json

# Get current path
path = pathlib.Path(__file__).parent.resolve()

out_name = input("Playlist Name: ")
out_folder = input("Playlist folder name: ")

auto = False
while True:
    out_auto = input("(1) Use file name for song name/keep artist blank\n(2) Enter title/artist for each song\nChoose one: ")
    if out_auto.lower() == "1":
        auto = True
    elif out_auto.lower() == "2":
        auto = False
    else:
        print("Please enter 1 or 2.")
        continue
    break   

folder = listdir(path)
songs = []

for item in folder:
    if not item.endswith(".bik"):
        # Not a song/not in a valid format, ignore
        continue
    # Add full path of current song to songs list
    songs.append(item)

# We now have all songs we want to add

# Create the folders
path_data = join(str(path), "Data")
path_music = join(str(path), "Data\\Music")
path_outfolder = join(str(path), "Data\\Music\\" + out_folder)


if not isdir(path_data):
    print("Created folder " + path_data)
    mkdir(path_data)

if not isdir(path_music):
    print("Created folder " + path_music)
    mkdir(path_music)

if not isdir(path_outfolder):
    print("Created folder " + path_outfolder)
    mkdir(path_outfolder)

musicpath = join(path, "Data\\Music\\" + out_folder)

out_json = {
    "soundtrack_folder": out_folder,
    "soundtrack_name": out_name,
    "num_tracks": 0,
    "tracks": []
}

# Move the songs and add them to the object for the json file
for song in songs:
    songdata = {
        "band": "artist",
        "title": "title",
        "filename": song[:-4],
        "genre": 0
    }

    if auto:
        songdata["band"] = "_"
        songdata["title"] = song[:-4]
    else:
        print("File name: " + song)
        songdata["title"] = input("Song title: ")
        songdata["band"] = input("Artist: ")

    out_json["tracks"].append(songdata)
    copy(join(path, song), join(musicpath, song))

out_json["num_tracks"] = len(out_json["tracks"])

with open(join(path, out_folder + ".sound.json"), "w") as out_file:
    out_file.write(json.dumps(out_json))
    print("Created file " + str(join(path, out_folder + ".sound.json")))

print("Finished")
input()