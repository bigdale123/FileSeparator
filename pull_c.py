import os
import shutil
import sys
import zipfile

def separator(path,output_path):
    platform = sys.platform
    if(os.path.isdir(output_path) == False):
        os.mkdir(output_path)
    for top, dirs, files in os.walk(path, topdown=True):
        for file in files:
            total_file = top+"/"+file
            name = total_file.split("/")[5]
            print(name)
            if(total_file.endswith(".h")):
                   #print(total_file)
                   print(output_path+name+"_"+file)
                   shutil.copy2(total_file,os.path.join(output_path,name+"_"+file))
        


if __name__ == "__main__":
    separator(sys.argv[1],sys.argv[2])
    #print(sys.argv[1],sys.argv[2])
