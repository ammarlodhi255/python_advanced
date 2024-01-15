try:
    f = open('./Miscellaneous/sampl.txt')
    # raise Exception
except FileNotFoundError:
    print('Sorry, File Not Found!')
except Exception:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('File is closed')