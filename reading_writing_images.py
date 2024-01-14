with open('./Miscellaneous/pic.jpeg', 'rb') as rf:
    with open('./Miscellaneous/pic_copy.jpeg', 'wb') as wf:
        chunk_size = 2000
        file_content = rf.read(chunk_size)

        while len(file_content) > 0:
            wf.write(file_content)
            file_content = rf.read(chunk_size)