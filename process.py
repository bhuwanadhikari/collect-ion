import json
from datetime import date

# with open('mainData.json') as f:
#   mainData = json.load(f)

# FIND OUT THE GIRLS THE LIST
# girls = []
# for person in mainData:
#     for liker in person['likersId']:
#         firstName = liker.split(".")
#         if firstName[0][-1] == 'a' or firstName[0][-1] == 'i':
#             name = firstName[0].split('/')
#             girls.append(name[1])
            
# print("he has", len(girls), 'girlfriends')



#LOAD MEMBERS OF MENS ROOM 1
# with open('mensroomNew.json') as mensroomNew:
#     mensroomNew = json.load(mensroomNew)
    
    
#LOAD MEMBERS OF MENS ROOM 2
    
# with open('mensroom.json') as mensroom:
#     mensroom = json.load(mensroom)
    
    
    
#LOAD MEMBERS OF STUDENT SOCIETY
# with open('members.json') as members:
#     members = json.load(members)
   
   
   
#    ----------------- 
# print('List of intersection are', len(list(set(mensroomNew) & set(mensroom) & set(members))))
# samples = list(set().union(mensroom, mensroomNew, members))
    

# mensroomNew = list(set(mensroomNew))
# print(len(mensroomNew))
# with open('samples.json', 'w') as f:
#     json.dump(samples, f, ensure_ascii=False, indent = 3)

# ----------------------
    
    
#MAKE THE DATA READY FOR MINING
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



# //FILTER OUT THE PHOTO.PHP AND PROFILE.PHP
# with open ('data.json') as data:
#     data = json.load(data)


# newData = []

# count = 0
# for one in data:
#     # print(one['likersId'])
#     allLikers = one['likersId']
#     for euta in allLikers:
        
        
#         if euta == '/photo.php':
#             count += 1
#             allLikers.remove('/photo.php')
        
#         if euta == '/profile.php':
#             count += 1
#             allLikers.remove('/profile.php')
    
    
#     sampleData = {
#         "photoOf" : one['photoOf'],
#         "likersId" : allLikers
#     }        
#     newData.append(sampleData)
# print(count)

# with open('data.json', 'w') as ff:
#     json.dump(newData, ff, ensure_ascii=False, indent = 3)


# GENERATE FAKE LIST OF GIRLS
# with open ('data.json') as data:
#     data = json.load(data)
    
# count = 0
# girls = []
# for one in data:
#     allLikers = one['likersId']
#     for euta in allLikers:
#         if euta.split('.')[0][-1] == 'a' or euta.split('.')[0][-1] == 'i':
#             # print(euta)
#             count += 1
#             girls.append(euta)
            
# with open('fakeGirls.json', 'w') as ff:
#     json.dump(girls, ff, ensure_ascii=False, indent = 3)

# print(count)






# REMOVE DATA OF GENUINE PEOPLE
# with open('data.json') as data:
#     data = json.load(data)

# with open('genuineSamples.json') as fff:
#     genuines = json.load(fff)
    
# donePeople = []
# count = 0
# for one in data:
#     donePeople.append('/' + one['photoOf'])

# for gen in genuines:
#     if gen in donePeople:
#         count +=1
#         print(gen, count)
    



        
        

# # DATA READY FOR THE PROCESSING
# with open ('data.json') as data:
#     data = json.load(data)


# with open ('genuineData.json') as genuineData:
#     genuineData = json.load(genuineData)

# count = 0
# wrcians = []
# allPeople = []
# doneSamples = []
# genuineSamples = []

# genuineData2 = []
# data2 = []


# for one in data:
#     allLikers = one['likersId']
#     allPeople  = allPeople + allLikers
#     one['photoOf'] = '/'+one['photoOf']
#     data2.append(one)
#     doneSamples.append(one['photoOf'])
    
# with open('data2.json', 'w') as ff1:
#     json.dump(data2, ff1, ensure_ascii=False, indent = 3)

# for one in genuineData:
#     allLikers = one['likersId']
#     allPeople  = allPeople + allLikers
#     one['photoOf'] = '/'+one['photoOf']
#     genuineData2.append(one)
#     genuineSamples.append(one['photoOf'])

    
# with open('genuineData2.json', 'w') as ff2:
#     json.dump(genuineData2, ff2, ensure_ascii=False, indent = 3)



# for gen in genuineSamples:
#     if gen in doneSamples:
#         print(gen)

       
        

# FIND OUT PEOPLE FROM WRC
with open ('data.json') as data:
    data = json.load(data)


with open ('genuineData.json') as genuineData:
    genuineData = json.load(genuineData)


#merge genuineData and data
data = data+genuineData


wrcians = []

#get genuine wrcians
for genuinePhoto in genuineData:
    wrcians.append(genuinePhoto['photoOf'])


allPeople = []
doneSamples = []
allLikers = []
samples = []
#get wrcians from data
for one in data:
    allLikers = one['likersId']
    allPeople  = allPeople + allLikers
    doneSamples.append(one['photoOf'])
    samples.append(one['photoOf'])
    
allPeople = list(set(allPeople))

for liker in allPeople:
    count = 0
    for item in data:
        if liker in item['likersId']:
            count += 1 
    if liker in samples:
        count += 1
    if(count>3):
        wrcians.append(liker)
        
        
    




allPeople = []
allLikers = []
doneSamples = []
#get wrcians from genuineData
for one in genuineData:
    allLikers = one['likersId']
    allPeople  = allPeople + allLikers
    doneSamples.append(one['photoOf'])

for liker in allPeople:
    count = 0
    for item in genuineData:
        if liker in item['likersId']:
            count += 1 
    if(count>2):
        wrcians.append(liker)
    


wrcians = list(set(wrcians))

for pal in wrcians:
    print(pal)
    # fn = pal.split('.')[0]
    # if fn[-1] == 'a' or fn[-1] == 'i':
    
    
print(len(wrcians))
# print(len(list(set(doneSamples))))

    
with open('wrcians.json', 'w') as ff3:
    json.dump(wrcians, ff3, ensure_ascii=False, indent = 3)
        