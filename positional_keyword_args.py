
# Positional and keyword arguments allow us to pass in positional as well as additional information.

def main(*args, **kwargs):
    print(args)
    print(kwargs)


# In the following case, the first two arguments are passed to the parameter "args", and the other two are passed to "kwargs" as additional info
main('Mathematics', 'Philosophy', name='Ammar', age=24)
# Its important to note that "args" is a tuple and "kwargs" is a dictionary that you can then later access.

# Unpacking values:

courses = ['Mathematics', 'Philosophy']
info = { 'name': 'Ammar', 'age':24}

main(courses, info) # The output is not what you expect.

main(*courses, **info)