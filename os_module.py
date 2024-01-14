import os 

print(dir(os)) # List out all the attributes and methods that we have access to in the OS module.
print(os.getcwd()) # Current working dir

# Change the current working directory.
# os.chdir('new_path') 

# List all the folders and files within a particular directory
print(os.listdir(os.getcwd()))

# Make a directory or directories 
# os.makedirs('top_path/sub_path')

# Remove a directory:
# os.rmdir('your_path_to_dir')

# rename a file:
# os.rename('file_to_rename', 'new_name')

# Print the name of the file only:
# os.path.basename('file_path')

# Print only the directory without the filename:
# os.path.dirname('file_path')

# Split both dirname and filename:
# os.path.split('file_path')

# Whether a dir or file exists:
# os.path.exists('path')

# Whether a path is dir or a file:
# os.path.isdir('path')
# os.path.isfile('path')

# Split the path and the file extension:
# os.path.splitext('file_path')

# OS STAT
from datetime import datetime
mtime = os.stat(os.path.join(os.getcwd(), 'os_module.py')).st_mtime
print(datetime.fromtimestamp(mtime))


# Recursively iterate all the directories:
for current_path, dirnames, filenames in os.walk(os.getcwd()):
    print(f'Current Path: {current_path}\nDirectories: {dirnames}\nFiles: {filenames}')