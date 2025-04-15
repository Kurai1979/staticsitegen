import os.path
import shutil
from os.path import isfile




def copy_source_to_target(source_folder, target_folder):
    print("Start copy...")
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)
    if not os.path.exists(source_folder):
        raise Exception(f"Folder {source_folder} not found")
    folder_content = os.listdir(source_folder)
    print(f"Found items: {folder_content}")
    for item in folder_content:
        print(f"Found file {item}")
        source = os.path.join(source_folder, item)
        target = os.path.join(target_folder, item)
        if isfile(source):
            print(f"From: {source} - {target}")
            shutil.copy(source, target)
        else:
            copy_source_to_target(source, target)






