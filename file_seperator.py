import os
import shutil
import sys
import zipfile

def separator(path):
    for file in os.listdir(path):
        name = file.split("_")[0]
        print(name)
        if(os.path.isdir(path+"\\"+name) == True):
            shutil.move(path+"\\"+file, path+"\\"+name+"\\"+file)
        else:
            os.mkdir(path+"\\"+name)
            shutil.move(path+"\\"+file, path+"\\"+name+"\\"+file)
        if(file.endswith(".zip")):
            with zipfile.ZipFile(path+"\\"+name+"\\"+file, 'r') as zip_ref:
                zip_ref.extractall(path+"\\"+name+"\\"+file.split("_")[-1][:-4])
        


if __name__ == "__main__":
    for i in range(1,len(sys.argv)):
        print(sys.argv[i])
        separator(sys.argv[i])