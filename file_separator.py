import os
import shutil
import sys
import zipfile

def find_source(path, source_code_extension):
    # We don't need to check for the source code directory,
    # Since we (normally) check for it in separator
    delim = ""
    if sys.platform == "win32":
        delim = "\\"
    else:
        delim = "/"
    source_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file.endswith(source_code_extension)):
                source_files.append(os.path.join(root,file))
    for i in source_files:
        name = i
        name = name.replace(path,'').split(delim)[0]
        print(name)
        print("FROM: "+i)
        print("TO:   "+os.path.join(path,source_code_extension.split(".")[1]+"_files",name+source_code_extension))
        shutil.copy(i,os.path.join(path,source_code_extension.split(".")[1]+"_files",name+source_code_extension))

def removeMacOSX(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))
            if("MACOSX" in os.path.join(root, file)):
                try:
                    shutil.rmtree(os.path.join(root))
                except Exception:
                    print("Folder already deleted (probably), skipping")

def separator(path, source_code_extension):
    if(os.path.isdir(os.path.join(path,source_code_extension.split(".")[1]+"_files")) != True):
        os.mkdir(os.path.join(path,source_code_extension.split(".")[1]+"_files"))
    for file in os.listdir(path):
        if(file != source_code_extension.split(".")[1]+"_files"):
            name = file.split("_")[0]
            print(name)
            if(os.path.isdir(os.path.join(path,name)) == True):
                shutil.move(os.path.join(path,file), os.path.join(path,name,file))
            else:
                os.mkdir(os.path.join(path,name))
                shutil.move(os.path.join(path,file), os.path.join(path,name,file))
            if(file.endswith(".zip")):
                with zipfile.ZipFile(os.path.join(path,name,file), 'r') as zip_ref:
                    zip_ref.extractall(os.path.join(path,name,file.split("_")[-1][:-4]))
    removeMacOSX(path)
    find_source(path, source_code_extension)
    
                
        


if __name__ == "__main__":
    print(sys.argv[1]+","+sys.argv[2])
    separator(sys.argv[1],sys.argv[2])
