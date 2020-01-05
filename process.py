import json

with open('mainData.json') as f:
  mainData = json.load(f)


girls = []
for person in mainData:
    for liker in person['likersId']:
        firstName = liker.split(".")
        if firstName[0][-1] == 'a' or firstName[0][-1] == 'i':
            name = firstName[0].split('/')
            girls.append(name[1])
            
print("pathak has", len(girls), 'girlfriends')