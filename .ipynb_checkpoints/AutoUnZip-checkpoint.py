import os
import subprocess

root = r"K:\Abide Dataset"
universities = os.listdir(root)
for university in universities:
    directory = os.path.join(root, university)

    FolderList = os.listdir(directory)

    for i, folder in enumerate(FolderList):
            
        direc = os.path.join(directory, folder, r'session_1\anat_1')
        if os.path.exists(direc):
            print(direc)  
            subprocess.run([
                r"C:\Program Files\WinRAR\WinRAR.exe", 'x', '-r', 
                os.path.join(direc, '*.gz'), direc,
            ], shell=True)
        
        direc = os.path.join(directory, folder, r'session_1\rest_1')
        if os.path.exists(direc):
            print(direc)  
            subprocess.run([
                r"C:\Program Files\WinRAR\WinRAR.exe", 'x', '-r', 
                os.path.join(direc, '*.gz'), direc,
            ], shell=True)
