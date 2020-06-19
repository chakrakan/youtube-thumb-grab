# Youtube-Thumbnail-Grabber
# Download HQ Thumbnails of YouTube videos in any playlist
# Resize them to your custom res

import logging
import os
import os.path
import sys
import re

import pafy
import wget
from PIL import Image

logging.getLogger().setLevel(logging.ERROR)


def thumb_grab(playlist, size):
    dir_name = playlist['title']  # Playlist title directory
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        os.chdir(dir_name)
        download_thumbnail(playlist, size)
    else:
        os.chdir(dir_name)
        download_thumbnail(playlist, size)


def download_thumbnail(playlist, size):
    invalid_chars = {'<': '', '>': '', ':': '', '"': '', '/': '', "\\": '', '|': '', '?': '', '*': ''}
    try:
        for video in playlist['items']:  # default playlist dict obj has no
            video_id = video['playlist_meta']['encrypted_id']  # attribute for HQ thumb dl
            video_obj = pafy.new(video_id)  # so must grab vid ID & use pafy obj
            video_title = str(video['playlist_meta']['title']).translate(str.maketrans(invalid_chars))
            print(video_title)
            name_format = video_title + ".jpg"  # UNDER GIVEN NAMING CONVENTION w/ delimiter
            thumb_url = video_obj.bigthumb
            wget.download(thumb_url, name_format)  # download and rename
            print(" Downloading, Please wait...")
    except Exception as e:
        print("Error:", e.__class__, "Issue grabbing video thumbnail")
        print("NOTE: Certain video names can create file output issues (if they have special characters no allowed in"
              "file naming schemas. Please create an issue at \n"
              "https://github.com/chakrakan/youtube-thumb-grab/"
              "with the name of the file where the bug occurred.")
        sys.exit(2)


def resize_thumbnail(video, playlist, size):
    if video['playlist_meta']['encrypted_id'] == playlist['items'][size - 1]['playlist_meta']['encrypted_id']:
        print("Thumbnails downloaded!")
        print("Would you like to resize images? Y/N")
        rez_resp = input().lower().strip()
        if rez_resp == "y":  # this portion should create a resized version image along with orig
            path = os.getcwd()
            c_dir = os.listdir(path)
            print("Please enter width: ")
            width = int(input())
            print("Please enter height: ")
            height = int(input())
            for item in c_dir:
                if os.path.isfile(item):
                    im = Image.open(item)
                    f, e = os.path.splitext(item)
                    resize = im.resize((width, height), Image.ANTIALIAS)
                    resize.save(f + ' resized.jpg', 'JPEG', quality=90)
                    if item == c_dir[-1]:
                        print("Resizing Complete!")
                        reset()

        elif rez_resp == "n":
            reset()


def reset():
    print("Would you like to download from another playlist? Y/N")
    d = input(': ').lower().strip()
    if d == "y":
        os.chdir(os.path.dirname(sys.argv[0]))
        thumb_grab()
    else:
        end_script()


def end_script():
    print("Thanks for using Thumb Grab!")
    sys.exit(0)


def main():
    """
    Driver function
    """
    print("Enter Youtube playlist url: ")
    playlist_url = input()

    # grab playlist id
    try:
        playlist = pafy.get_playlist(playlist_url)
        size = len(playlist['items'])
        print('This playlist has %s videos. Grab thumbnails? Y/N' % size)
        init_resp = input().lower().strip()

        if init_resp == "y":
            thumb_grab(playlist, size)
        else:
            end_script()
    except Exception as e:
        print("Error:", e.__class__, "Please make sure Youtube Playlist URL is valid.")
        sys.exit(2)


if __name__ == "__main__":
    main()
# EOF
