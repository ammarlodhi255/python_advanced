from getpass import getpass 

username = input('Username: ')

# Instead of using input to get the password, we used 'getpass' so that the when the user types out the password, it is invisible.
password = getpass('Password: ') 

print('Logging in....')