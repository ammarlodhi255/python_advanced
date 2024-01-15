import requests 
# import antigravity 

r = requests.get('https://xkcd.com/353/')
print(r.status_code)

# Print website source:
# print(r.text) 

###### Downloading an Image ######
r = requests.get('https://imgs.xkcd.com/comics/python.png')
if r.ok: # Apart from client errors (400's) and server errors (500's), everything else is 'ok'
    with open('./Miscellaneous/downloaded.png', 'wb') as png:
        png.write(r.content)
        print(r.headers)


###### Testing queries using httpbin.org ######
print('----------------------------------')
payload = {'username': 'Ammar', 'password': '12345'}
req = requests.get('https://httpbin.org/get', params=payload)

print(req.text)
print(req.url)

###### POST, passing information to web ######
post_req = requests.post('https://httpbin.org/post', data=payload) 
# The data that we passed should be displayed inside of the form.
print(post_req.text)

r_dict = post_req.json()
print(r_dict['form'])

###### Basic Authentication ######
user_info = ('ammar', 'test')
auth_req = requests.get('https://httpbin.org/basic-auth/ammar/test', auth=user_info)
if auth_req.ok:
    print(auth_req.text) 
else:
    print('User info incorrect!')

###### Adding Timeout to a Request ######
delay = 3
delayed_req = requests.get(f'https://httpbin.org/delay/{delay}', timeout=6)
print(delayed_req)