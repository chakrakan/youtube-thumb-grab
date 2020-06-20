# Thumb-Grab

Get thumbnails of YouTube videos in any given playlist, resize them to your custom res of choice.

Orginially built while I was a part of TEDxUTSC and volunteered as a webmaster. This script allowed me to automate the whole process of grabbing thumnails of 160+ TED videos from large youtube playlists, and re-sizing them so they could be displayed on the TEDxUTSC website. 

## Usage

1. Set up a virtual env for the project once cloned locally
2. `pip install -r requirements.txt` to grab all requirements to run the script
3. Run the script from your terminal using `python thumbgrab.py`
4. Enter/Copy paste the Youtube Playlist URL when prompted
5. Follow the prompts to download thumbnails for all videos in the playlist

> The thumbnails will be placed in a new folder based on the playlist name within the script directory

6. If you want to resize images to a custom `width` and `height`, follow the prompt after
7. Enter respective width and height as necessary for pictures

> Resized thumbnails will be placed in the same folder with the word "resized" added to the title.

## Sample

Here's a sample performed on this playlist by TED titled, [The 20 Most-Watched TEDTalks](https://www.youtube.com/playlist?list=PL70DEC2B0568B5469)
![](https://github.com/chakrakan/youtube-thumb-grab/blob/master/screenshots/demo.gif)

The output of the above demo is available in this repository as a sample within the titled folder.

### Dependencies:
- Pafy  http://np1.github.io/pafy/
- wget  https://bitbucket.org/techtonik/python-wget/src
- Pillow (PIL)  https://python-pillow.github.io/
