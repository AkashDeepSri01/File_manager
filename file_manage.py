import os
import shutil

path = input("Enter your path: ")

files = os.listdir(path)
for i in files:
    filename, extension = os.path.splitext(i)
    extension_1 = extension[1:]
    folder_path = path + '\\' + extension_1  # Fix the folder path assignment
    if os.path.exists(folder_path):
        shutil.move(path + "\\" + i, path + "\\" + extension_1 + "\\" + i)
    else:
        os.makedirs(path + "\\" + extension_1)
        shutil.move(path + "\\" + i, path + "\\" + extension_1 + "\\" + i)
