#!/usr/bin/python

import argparse
import string
import os
import sys
import shutil
import subprocess

### Argument parser
parser = argparse.ArgumentParser(description='Python/Bash imageMagick resizer')

parser.add_argument('-photo', action='store', dest='photo', type=str, help='Input photo name')
parser.add_argument('-format', action="store", dest='format', default='prof', help='Choose a a file format, prof, home, bullet, etc..')
parser.add_argument('-id', action='store', dest='idnumber', type=str, help='Doctor ID number')
parser.add_argument('-width', action="store", dest="width", default='165', type=int)

arg_values = parser.parse_args()

targetfile = "%s_%s_01.jpg" % (arg_values.format, arg_values.idnumber)

### Image Paths and Target Dir
DIRECTORY_IMG_PATH = '<<PATH HERE>>' 
JOURNAL_IMG_PATH = '<<PATH HERE>>'

cdtargetdir = "%s%s" % (DIRECTORY_IMG_PATH, arg_values.idnumber) #targetdir
cjtargetdir = ""		#JOURNAL target dir - not yet implemented

def main():
    if len(sys.argv[1:]) < 3:
        print "you need more options"
        sys.exit()
    elif arg_values.idnumber == None:
        print "you forgot idnumber"
        sys.exit()
    else:
        resizePicture(arg_values.width, sanitize_photoname(arg_values.photo), targetfile)
        publishPhoto(targetfile, cdtargetdir)

def sanitize_photoname(photo_file):
	### this is to clean out spaces in filenames as to not create errors when converting
	cleaned_photo = photo_file.replace('\\', '')
	cleaned_photo = photo_file.replace(' ', '')
	os.rename(photo_file, cleaned_photo)
	return cleaned_photo

def resizePicture(width, inputfile, outputfile):
	RESIZE = """convert %s -resize %s %s""" % (inputfile, width, outputfile)
	print "Resizing %s..." % (inputfile)
	subprocess.call(RESIZE, shell=True)
	print "Job Done."

def publishPhoto(outputfile, target_dir):
	#check and see if doctor already has a directory created
	if os.path.exists(target_dir):
		print "Directory %s found!" % (outputfile)
		print "Copying photo to %s/%s" % (target_dir, outputfile)
		shutil.copy(outputfile, target_dir)
	else:
		print "Directory %s NOT found! creating directory..." % (target_dir)
		os.mkdir(target_dir)
		print "Copying photo..."
		shutil.copy(outputfile, target_dir)

if __name__=="__main__":
    main()

		
