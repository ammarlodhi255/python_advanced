import json 

### Working with json strings ###

json_str = '''
{
    "fruit": "Apple",
    "size": "Large",
    "color": "Red"
}
'''

data = json.loads(json_str)
print(type(data))

for key, value in data.items():
    print('{}: {}'.format(key, value))


### Working with json file ###

with open('./Miscellaneous/states.json', 'r') as f:    
    data = json.load(f)

states = data['states']
for i, state in enumerate(states):
    print('State {}: {}, ({})'.format((i+1), state['name'], state['abbreviation']))


### Working with json file from the web ###