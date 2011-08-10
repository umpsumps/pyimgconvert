#!/bin/python

import os




def rename_reincrement(directory):
        filename_index = []        
        for file in os.listdir(directory):
		file = file.strip('.jpg')
                file, num = file.rsplit('_', 1) 
                filename_index.append((file,int(num)))

        inputfiles = os.listdir(directory)
        inputfiles.sort()
        inputfiles = inputfiles[::-1]

        for prefix, suffix in sorted(filename_index, key=lambda index: index[1])[::-1]:
                suffix += 1
                os.rename(inputfiles[0], ("%s_%02d.jpg" % (prefix, suffix)))
                print inputfiles[0], "%s_%02d.jpg" % (prefix, suffix)
                inputfiles.pop(0)
