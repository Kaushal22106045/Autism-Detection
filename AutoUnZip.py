import os
import subprocess

universities = os.listdir(r"C:\Users\91700\Minor Project\dataset")
for university in universities:
    directory = os.path.join(r"C:\Users\91700\Minor Project\dataset", university)

    FolderList = os.listdir(directory)

    for i, folder in enumerate(FolderList):
            
        direc = os.path.join(directory, folder, r'session_1\anat_1')
        if os.path.exists(direc):
            print(direc)  
            subprocess.run([
                r"C:\Program Files\WinRAR\WinRAR.exe", 'x', '-r', 
                os.path.join(direc, '*.gz'), direc,
            ], shell=True)

            subprocess.run([
                
            ], shell = True)
        
        direc = os.path.join(directory, folder, r'session_1\rest_1')
        if os.path.exists(direc):
            print(direc)  
            subprocess.run([
                r"C:\Program Files\WinRAR\WinRAR.exe", 'x', '-r', 
                os.path.join(direc, '*.gz'), direc,
            ], shell=True)

        

