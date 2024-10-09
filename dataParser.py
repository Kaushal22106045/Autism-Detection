import os
import subprocess

root = r"/root/miniconda3/Minor Project/dataset/"
internal_folder = r'session_1/anat_1'

# Define the data_parsing decorator
def data_parsing(func):
    def wrapper(*args, **kwargs):
        root, internal_folder = args  # Get the root and internal folder from function arguments
        
        # List all directories (universities) in the root folder
        universities = os.listdir(root)
        
        for university in universities:
            directory = os.path.join(root, university)
            
            # List all folders in each university directory
            FolderList = os.listdir(directory)
            
            for folder in FolderList:
                # Construct the full path to the internal folder (session_1/anat_1)
                direc = os.path.join(directory, folder, internal_folder)
                
                # Check if the folder exists, if so, call the decorated function (unZip)
                if os.path.exists(direc):
                    func(direc)  # Pass the directory to the unZip function
    return wrapper

# Define the unZip function and use the data_parsing decorator
@data_parsing
def unZip(direc):
    subprocess.run([
        r"C:\Program Files\WinRAR\WinRAR.exe", 'x', '-r', 
        os.path.join(direc, '*.gz'), direc
    ], shell=True)

# Now, call the unZip function with root and internal_folder as arguments
# unZip(root, internal_folder)





