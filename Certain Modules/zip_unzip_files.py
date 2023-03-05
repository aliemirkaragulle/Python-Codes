# Zipping and Unzipping Files

import zipfile
import shutil

# As you are probably aware, files can be compressed to a zip format. 
# Often people use special programs on their computer to unzip these files, luckily for us, Python can do the same task with just a few simple lines of code.

# Create Files to Compress

f = open("new_file1.txt",'w+')
f.write("Here is some text")
f.close()

f = open("new_file2.txt",'w+')
f.write("Here is some text")
f.close()

# Move the Files to Desktop
#shutil.move("new_file1.txt", "/Users/aliemirkaragulle/Desktop")
#shutil.move("new_file2.txt", "/Users/aliemirkaragulle/Desktop")



# Zipping Files

# The zipfile library is built in to Python, we can use it to compress folders or files. 
# To compress all files in a folder, just use the os.walk() method to iterate this process for all the files in a directory.

#  Create Zip file first , then write to it (the write step compresses the files.)
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write("new_file1.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# Extracting from Zip Files

# We can easily extract files with either the extractall() method to get all the files, or just using the extract() method to only grab individual files.
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")



# Using shutil library

# Often you don't want to extract or archive individual files from a .zip, but instead archive everything at once. 
# The shutil library that is built in to Python has easy to use commands for this:

"""
directory_to_zip='C:\\Users\\Marcial\\Pierian-Data-Courses\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules'
output_filename = 'example'

# Creating a zip archive
# Just fill in the output_filename and the directory_to_zip
shutil.make_archive(output_filename,'zip',directory_to_zip)

# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here
shutil.unpack_archive(output_filename,dir_for_extract_result,'zip')
"""