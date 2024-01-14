'''
I have a folder which contains the following files:
test 1.txt
test 2.txt
test 3.txt
test 4.txt
test 5.txt

I want the number at the end of each file name to be at the beginning,
so that the files are stored in the sorted order inside the folder.
'''

import os

dir_path = '/Users/ammarahmed/My Files/Code Files/Python Code/Miscellaneous/automate'
os.chdir(dir_path)
files = os.listdir(dir_path)

for file in files:
    filename, fileext = os.path.splitext(file)
    new_filename = filename.split(' ')
    new_filename = f'{new_filename[-1].zfill(2)} {new_filename[0]}{fileext}'
    os.rename(os.path.join(dir_path, file), new_filename)