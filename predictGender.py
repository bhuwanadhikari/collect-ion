# Pip install the client:
# pip install clarifai
import time
import json
from datetime import date

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
# Create your API key in your account's Application details page:
# https://clarifai.com/apps

app = ClarifaiApp(api_key='67ed35e690244348b66e2a7548271910')



def delay( timeValue):
    time.sleep(timeValue)
        


model = app.public_models.general_model
model.model_version = 'c0c0ac362b03416da06ab3fa36fb58e3'
response = model.predict(ClImage(url="https://scontent.fktm3-1.fna.fbcdn.net/v/t1.0-9/23319285_1746152652356782_2967698470842630899_n.jpg?_nc_cat=111&_nc_ohc=mAp9jkm27mMAX_p6YwK&_nc_ht=scontent.fktm3-1.fna&oh=77cd71d5d31521c9f052db904c4f3ed3&oe=5E95F676"))
print(response)




# with open ('dumbasData.json', encoding="utf-8") as fff55:
#     dumbasData = json.load(fff55)


# withGender = []

# for person in dumbasData:
#     response = model.predict(ClImage(url="person.pictureUrl"))
#     delay(0.0010)
#     print(response)
#     person.gender = response
#     withGender.append(gender)


# with open('withGender.json', 'w', encoding="utf-8") as ff3:
#     json.dump(withGender, ff3, ensure_ascii=False, indent = 3)
     

