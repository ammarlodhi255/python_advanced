import os 

with open('./Miscellaneous/test.txt', 'r') as f: # Opening files without context managers may lead to forgetting to close the file explicity leading to leaks.
    print(f'Filename: {os.path.basename(f.name)}') 
    print(f'File Mode: {f.mode}') 
    
    # Read all of the content in the file at once:
    # f_content = f.read()

    # However, a file can be very large, therefore, it is better to read each line at once, in case of large file.
    for line in f:
        print(line, end='')

    # Instead of reading only a single line per iteration, you can read chunks of a file:
    size_to_read = 100 # Print out first 100 characters of the file.

    f_content = f.read(size_to_read)
    while len(f_content) > 0: # When we reach the end of the file, the f.read() will return an empty string.
        print(f_content)
        f_content = f.read(size_to_read)


    f.seek(0) # Start at the beginning of the file.


# WRITING:
    
with open('./Miscellaneous/sample.txt', 'w') as f: # 'w' for overwriting and 'a' for appending
    f.write('Write')

    # f.seek(0) # Go to the beginning of the file and replace content


