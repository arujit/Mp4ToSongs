# usr/bin/pyhton 2.7

"""
author : jamesbondu
description : a basic python script for converting video play list(directry to simple mp3 files)
"""

import sys
import subprocess
import os


#basic ffmpeg command for a video to audio conversion
#os.system( "ffmpeg -i %s -vn -ab 320k -acodec libmp3lame -ac 2 %s" % (sys.argv[1] ,sys.argv[2]) )

def conversion(input_dir , output_dir):
    try :
        #existance of the folders
        if not os.path.exists(input_dir):
            exit("Error: Input dirctory /"+input_dir+" does not exists")
        #existance of the folders
        if not os.path.exists(output_dir):
            exit("Error: Input dirctory /"+output_dir+" does not exists")
            
            
        print "[%s/*.mp4] -->[%s/*.mp3]" % ( input_dir,output_dir)

        files = []
        filelist = [f for f in os.listdir(input_dir) if f.endswith(".mp4")]
        print sys.argv[0]
        for path in filelist:
            print path
            basename = os.path.basename(path)
            #print basename
            filename = basename.split(".")[0]
            #print filename
            files.append(filename)

        if len(files) == 0:
            exit("No files found")

    except OSError as e:
        exit(e)
    
    
        #converting files individually

    for file in files:
        in_file = file + ".mp4"
        out_file = file + ".mp3"
        print out_file
        os.system( "ffmpeg -i "+input_dir+"/"+in_file+" -vn -ab 320k -acodec libmp3lame -ac 2 "+output_dir+"/"+out_file)

#setting default directories to the current directory or get input directories from user


   
if __name__ == '__main__':
    args = [".","."]
    #setting current derectory
    for i in range (1,min(len(sys.argv),3)):
        args[i-1 ] = sys.argv[i]

    if len(sys.argv) == 2:
        args[1] = sys.argv[0]
    

    conversion(args[0] , args[1])


