import os
import re
import shutil

sourceDir = r"your_source_dir_path"
targetDir = r"your_target_dir_path"

if not os.path.isdir(targetDir):
    raise ValueError(f"target dir not exist: {targetDir}")

if not os.path.isdir(sourceDir):
    raise ValueError(f"source dir not exist: {sourceDir}")


photos_dir_path = r".*(?:Photos from )(2\d\d\d)"
archive = r".*封存檔案"
non_photo= r"^.*\.json$"

# TODO: checkout if same name files in target dir before copy2

def main():
    for curdir, subdirs, files in os.walk(sourceDir):
        print(f"start in {curdir}")
        if (name:=re.match(photos_dir_path,curdir)):
            year=name.group(1)
            target=os.path.join(targetDir,year)

            if not os.path.isdir(target):
                os.makedirs(target)

            for f in files:
                if re.match(non_photo,f):
                    pass
                else : 
                    full_name = get_id(target,f)
                    shutil.copy2(os.path.join(curdir,f),full_name)
        elif (name:=re.match(archive,curdir)):
            target=os.path.join(targetDir,"archive")

            if not os.path.isdir(target):
                os.makedirs(target)
            
            for f in files:
                if re.match(non_photo,f):
                    pass
                else : 
                    full_name = get_id(target,f)
                    shutil.copy2(os.path.join(curdir,f),full_name)
        else:
            pass


def get_id(targetDir,fname:str):
    # check if same name files in target dir before copy2
    fullpath = os.path.join(targetDir,fname)
    id=0

    while True :
        test_value = fullpath if id==0 else fullpath+f"({id})"
        if os.path.isfile(test_value):
            id+=1
        else :
            break

    return fullpath if id==0 else fullpath+f"({id})"


if __name__ == "__main__":
    main()