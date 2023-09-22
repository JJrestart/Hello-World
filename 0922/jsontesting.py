import json

with open('sungjuk.json', 'rt') as fread :
    result = json.load(fread)
    print(result[0]['irum'])