import json
from datetime import date

# with open('mainData.json') as f:
#   mainData = json.load(f)


# girls = []
# for person in mainData:
#     for liker in person['likersId']:
#         firstName = liker.split(".")
#         if firstName[0][-1] == 'a' or firstName[0][-1] == 'i':
#             name = firstName[0].split('/')
#             girls.append(name[1])
            
# print("pathak has", len(girls), 'girlfriends')
# with open('mensroomNew.json') as mensroomNew:
#     mensroomNew = json.load(mensroomNew)
    
# with open('mensroom.json') as mensroom:
#     mensroom = json.load(mensroom)
    
# with open('members.json') as members:
#     members = json.load(members)
    
# print('List of intersection are', len(list(set(mensroomNew) & set(mensroom) & set(members))))
# samples = list(set().union(mensroom, mensroomNew, members))
    

# mensroomNew = list(set(mensroomNew))
# print(len(mensroomNew))
# with open('samples.json', 'w') as f:
#     json.dump(samples, f, ensure_ascii=False, indent = 3)

with open ('mainData.json') as mainData:
    mainData = json.load(mainData)
print(mainData)
    
# with open ('mainData2.json') as mainData2:
#     mainData2 = json.load(mainData2)
    
# with open('data.json') as data:
#     data = json.load(data)


# sample1 = []
# sample2 = []

# for one in mainData:
#     sample1.append(one['photoOf'])

# for one in mainData2:
#     sample2.append(one['photoOf'])

# # print(len(list(sample1+sample2)))
# alreadyDone = list(set().union(sample1, sample2))

# testArr = []
# pureData = []
# for item in data:
#     if item['photoOf'][0] == '/':
#         item['photoOf'] = item['photoOf'][1:]
#     if item['photoOf'] not in testArr:
#         pureData.append(item)
#     else:
#         testArr.append(item['photoOf'])

# print(len(pureData))

# with open('data.json', 'w') as ff:
#     json.dump(data, ff, ensure_ascii=False, indent = 3)












# notDone = list(set(samples)-set(alreadyDone))


# with open('pureSamples.json', 'w') as pureSamples:
#     json.dump(notDone, pureSamples, ensure_ascii=False, indent = 3)


# with open('samples.json', 'w') as f:
#     json.dump(samples, f, ensure_ascii=False, indent = 3)





# for i in notDone:
#     print(i)
    
# print(len(samples))
# print(len(notDone))



# for i in alreadyDone:
#     print(i)
# print(len(alreadyDone))