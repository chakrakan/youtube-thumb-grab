# Youtube-Thumbnail-Grabber
# Download HQ Thumbnails of YouTube videos in any playlist
# Resize them to your custom res

import pafy
import sys
import os
import os.path
import wget
import errno
import logging
from PIL import Image

    
def thumb_grab():
    print("Enter Youtube playlist url")
    a = raw_input(': ')

    #grab playlist id
    playlist = pafy.get_playlist(a)
    size = len(playlist['items'])  
    print('This playlist has %s videos. Grab thumbnails? Y/N' % (size))
    b = raw_input(': ')

    if (b == "Y"):
        dir = str(playlist['title'])   
        if not os.path.exists(dir):  
            os.makedirs(dir)
            os.chdir(dir)
        for v in playlist['items']:            # default playlist dict obj has no
            v_id = str(v['playlist_meta']['encrypted_id']) # attribute for HQ thumb dl
            vid = pafy.new(v_id)             # so must grab vid ID & use pafy obj
            t = str(v['playlist_meta']['title']).split(':')  
            #v_t = t[1]                     # THIS WILL STOP THE APP IF VID IS NOT (specific for TEDxUTSC)
            format = t[:5] + ".jpg"    # UNDER GIVEN NAMING CONVENTION w/ delimiter
            root, ext = os.path.splitext(format)
            thumb_url = vid.bigthumb
            thumb = wget.download(thumb_url, format)  # download and rename
            print("Downloading, Please wait...")
            if(v['playlist_meta']['encrypted_id'] == playlist['items'][size-1]['playlist_meta']['encrypted_id']):
                print("Thumbnails downloaded!")
                print("Would you like to resize images? Y/N")
                c = raw_input(': ')
                if (c == "Y"):       # this portion should create a resized vs of
                    path = os.getcwd()    # image along with orig
                    c_dir = os.listdir(path)
                    print("Please enter width")
                    w = int(raw_input(': '))
                    print("Please enter height")
                    h = int(raw_input(': '))
                    for item in c_dir:
                        if (os.path.isfile(item)):
                            im = Image.open(item)
                            f, e = os.path.splitext(item)
                            imResize = im.resize((w, h), Image.ANTIALIAS)
                            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
                            if (item == c_dir[-1]):
                                print("Resizing Complete!")
                                resetter()
                                
                elif (c == "N"):
                    resetter()
    else:
        print("Thanks for using Thumb Grab!")
        sys.exit(0)
        

logging.getLogger().setLevel(logging.ERROR)  #stop random false warnings >:@
                                

def resetter():
    print("Would you like to download from another playlist? Y/N")
    d = raw_input(': ')
    if (d == "Y"):
        os.chdir(os.path.dirname(sys.argv[0]))
        thumb_grab()
    else:
        print("Thanks for using Thumb Grab!")
        sys.exit(0)

if __name__ == "__main__":
    thumb_grab()
#EOF
