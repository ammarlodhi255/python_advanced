
print("Importing search module")

def search_list(to_search, target):
    for i, current in enumerate(to_search):
        if current == target:
            return True 
        
    return False