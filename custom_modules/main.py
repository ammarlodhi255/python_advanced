# import search 
from search import search_list
import sys 

courses = ['Math', 'Philosophy', 'History', 'Logic']
# print(search.search_list(courses, 'History'))
print(search_list(courses, 'History'))


# Following are the locations that python checks, when we try to import a module.
print(sys.path) 

# If you want to use a specific folder to import your modules from, add it to the sys path as follows:
# sys.path.append('path_to_modules_folder')

# FUN MODULE:

# import antigravity