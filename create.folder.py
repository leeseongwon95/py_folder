import os

def create_folder2():
    createFolder('경로지정')
    createFolder('경로지정')
    createFolder('경로지정')

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
create_folder2()
