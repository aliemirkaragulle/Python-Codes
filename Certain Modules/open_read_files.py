# Opening and Reading Files
import os
import shutil
import send2trash

# Create Practice File
 
f = open("practice.txt", "w+")
f.write("This is a test txt.")
f.close()


# Getting Directories

# Python has a built-in os module that allows us to use operating system dependent functionality.
# You can get the current directory:
print(os.getcwd())



# Listing Files in a Directory

# You can also use the os module to list directories.

# In your current directory
print(os.listdir())
print("\n")

# In any directory you pass
print(os.listdir("/Users/aliemirkaragulle/Desktop"))
print("\n")



# Moving Files

# You can use the built-in shutil module to move files to different locations.
# Keep in mind, there are permission restrictions. 
# For example, if you are logged in User A, you won't be able to make changes to the top level Users folder without the proper permissions.
shutil.move("practice.txt", "/Users/aliemirkaragulle/Desktop")



# Deleting Files

# Note: The os module provides 3 methods for deleting files:
# os.unlink(path) -> which deletes a file at the path you provide
# os.rmdir(path) -> which deletes a folder (folder must be empty) at the path you provide
# shutil.rmtreee(path) -> this is the most dangerous, as it will remove all files and folders contained iin the path

# All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. 
# Instead we will use the send2trash module. A safer alternatiive that sends deleted files to the trash bin instead of permanent removal. 
send2trash.send2trash("/Users/aliemirkaragulle/Desktop/practice.txt")



# Walking Through a Directory

# Often you will just need to "walk through a directory", that is visit every file or folder and c
# heck to see if a file is in the directory, and then perhaps do something with that file.
# Usually recursively walking through every file and folder in a diirectory would be quite tricky to program, 
# but luckily the os module has a direct method call for this called os.walk().
# Let's explore how it works.

for folder , sub_folders , files in os.walk("/Users/aliemirkaragulle/Desktop/Life"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
    
    # Now look at subfolders