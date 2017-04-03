import os

def rename_files():
    # (1) get file names from folder
    file_list = os.listdir("/Users/lima/Downloads/prank")
    #print(file_list)

    # Change directory path | If we don't change, will get FileNotFoundError:
    os.chdir("/Users/lima/Downloads/prank")
    
    # (2) for each file, rename filename
    for file_name in file_list:
        
        file_rename = os.rename(file_name, file_name.translate({ord(i):None for i in '0123456789'}))

    # Change dir path back
    os.chdir("/Users/lima/Documents/Udacity/PythonFoundations")
    
rename_files()
