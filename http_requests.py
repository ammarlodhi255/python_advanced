import requests 
# import antigravity 

r = requests.get('https://xkcd.com/353/')
print(r.status_code)

# Website source:
# print(r.text) 


r = requests.get('https://imgs.xkcd.com/comics/python.png')
if r.ok: # Apart from client errors (400's) and server errors (500's), everything else is 'ok'
    with open('./Miscellaneous/downloaded.png', 'wb') as png:
        png.write(r.content)