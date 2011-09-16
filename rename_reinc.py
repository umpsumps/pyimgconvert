#!/usr/bin/python

import sys
import os
import glob
import argparse

### Argument parser
parser = argparse.ArgumentParser(description='Rename and Reincrement Photos')

parser.add_argument('-dirpath', action='store', dest='dirpath', type=str, help='directory path')
parser.add_argument('-suffix', action='store', dest='suffix', type=str, help='filename suffix in format')

arg_values = parser.parse_args()


def main():
    if len(sys.argv[1:]) < 2:
        print "Please select a directory path and filename suffix"
        sys.exit()
    elif arg_values.suffix == None:
        print "you forgot a suffix"
    else:
        rename_reinc(arg_values.dirpath, arg_values.suffix)




def rename_reinc(directory_path, filename_suffix):
    os.chdir(directory_path)
    getFileList = glob.glob(filename_suffix)
    filename_index = []
    for file in getFileList:
        file = file.strip(filename_suffix)
        file, num = file.rsplit('_', 1)
        filename_index.append((file,int(num)))

   
    getFileList.sort()
    getFileList = getFileList[::-1]

    for prefix, suffix in sorted(filename_index, key=lambda index: index[1])[::-1]:
        suffix += 1
        os.rename(getFileList[0], ("%s_%02d%s" % (prefix, suffix, filename_suffix.strip('*'))))
        print getFileList[0], "%s_%02d%s" % (prefix, suffix, filename_suffix.strip('*'))
        getFileList.pop(0)
    
if __name__=="__main__":
    main()
