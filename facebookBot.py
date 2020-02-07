from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import json
from urllib.parse import urlparse

with open('samples.json') as f0:
    samplesPhotos = json.load(f0)


# driver = webdriver.Chrome()
# driver.get("http://www.instagram.com")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# # driver.close()

def delay( timeValue):
        time.sleep(timeValue)
        
## global variables here
startUrl = 'https://www.facebook.com'
myId = 'yourusername'
myEmail = 'yourdamnemail@gmail.com'
myPassword = 'yourpassword'

class instaBot():
    def __init__(self, email, password):
        
        
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
        self.sampleFriends = []
        self.startTime = datetime.now().strftime("%H:%M")
        

    def signIn(self):
        self.browser.get('https://www.facebook.com/')
        delay(2)
        emailInput =  self.browser.find_element_by_name("email")
        passwordInput = self.browser.find_element_by_name("pass")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        delay(2)
    
    def closePopup(self):
        buttons = self.browser.find_elements_by_tag_name('button')
        button = buttons[len(buttons)-1]
        button.click()
        delay(2)
    
    def goProfile(self):
        # self.browser.get('https://www.instagram.com/testman/')
        delay(2)
        
    def updateSamples(self, urlToBeRemoved):
        with open('samples.json') as f11:
            allSamples = json.load(f11)
        allSamples.remove(urlToBeRemoved)
            
        with open('samples.json', 'w') as f12:
            json.dump(allSamples, f12, ensure_ascii=False, indent = 3)
                
        
    def goToPhoto(self):
        # self.browser.get(startUrl)
        # # see likers
        # delay(2)
        # likeNumber1 = self.browser.find_elements_by_class_name("_3dlf")[1]
        # likeNumber1.click()
        # delay(3)
        
        # #click the more samples
        # moreSamples = True
        # while moreSamples:
        #     try:
        #         delay(3)
        #         samples =  self.browser.find_elements_by_class_name("uiMorePagerPrimary")[0]
        #         samples =  self.browser.find_elements_by_class_name("pam")[0]
        #         samples =  self.browser.find_elements_by_class_name("uiBoxLightblue")[0]
        #         jsCode = "document.getElementsByClassName('uiBoxLightblue pam uiMorePagerPrimary')[0].click();"
        #         self.browser.execute_script(jsCode)
        #         print("Loading more samples of the start photo")
        #     except:
        #         moreSamples = False
        #         print("No more samples to load in the page")
            
        # #get primary likers
        # delay(2)
        # samples =  self.browser.find_elements_by_class_name("_5i_s")
        # sampleUrls = []
        # for sample in samples:
        #     sampleUrl = sample.get_attribute('href')
        #     sampleUrls.append(sampleUrl)
            
            
        data = []
        doneSamples = []
        counter = 0
        # for url in sampleUrls:
        for url in samplesPhotos:
            counter += 1
                
            #visit one of the liker
            # self.browser.get(url)
            
            #get username of liker
            
            #-----------------------
            # sampleId = urlparse(url).path
            samplePhotoData = {}
            # #-----------
            #visit all photos of liker
            sampleId = url
            print('Visiting all photo samples of', sampleId)
            if sampleId == myId or sampleId == '/profile.php' or sampleId == '/photo.php': continue
            self.browser.get('https://www.facebook.com/'+sampleId+'/photos_all')
            
            #visit one photo of liker
            photosOfLiker =  self.browser.find_elements_by_class_name("uiMediaThumbMedium")
            if  len(photosOfLiker) < 1 :
                print('User has no photos to load load')
                self.updateSamples(url)
                continue
            photoOfLiker = photosOfLiker[0]
            # photoOfLiker.click()
            self.browser.get(photoOfLiker.get_attribute('href'))
            print('Visiting a single photo of', sampleId)
            
            
        
            #visit to the list of secondary likers
            delay(2)
            clickButtons = self.browser.find_elements_by_class_name("_3dlf")
            print('Length of buttons is', len(clickButtons))
            if len(clickButtons) < 2:
                print("Cannot enter into the list of likers")
                self.updateSamples(url)
                continue
            likeNumber2= clickButtons[1]
            likeNumber2.click()
            print('Seeing Likers of a photo of', sampleId)
            delay(2)
            
            #click the more likers
            moreLikers = True
            limitLoad = 0
            # while moreLikers and limitLoad<1:
            while moreLikers:
                try:
                    delay(2)
                    samples =  self.browser.find_elements_by_class_name("uiMorePagerPrimary")[0]
                    samples =  self.browser.find_elements_by_class_name("pam")[0]
                    samples =  self.browser.find_elements_by_class_name("uiBoxLightblue")[0]
                    jsCode = "document.getElementsByClassName('uiBoxLightblue pam uiMorePagerPrimary')[0].click();"
                    self.browser.execute_script(jsCode)
                    print("Loading more likers of the sample photo")
                  
                    
                except:
                    moreLikers = False
                    print("No more likers to load in the page")
        
        
            #get all secondary likers
            likers = self.browser.find_elements_by_class_name("_5i_s")
            
            
            likersId =[]
            
            for liker in likers:
                likerUrl = liker.get_attribute('href')
                likerId = urlparse(likerUrl).path
                if likerId !='/photo.php':
                    if likerId == '/profile.php':
                        likerId = likerUrl.split('?')[1]
                        likerId = likerId.split('&')[0]
                        likerId = '/'+likerId.split('=')[1]
                    print('Liker is ', likerId)
                    likersId.append(likerId)
        
            # make sample photo data ready
            
            
            samplePhotoData['photoOf'] = sampleId
            # samplePhotoData['likersUrl'] = likersUrl
            samplePhotoData['likersId'] = likersId
            
            print('----------------------------------------------------------------')
            print('----------------------------------------------------------------')
            
            try:
                with open('data.json') as f1:
                    data = json.load(f1)
                data.append(samplePhotoData)
                print('-----Total Samples: ', len(data), '--------')
            except:
                
                print('Error in main data opening')
            
            # add sample photo data to main data
            with open('data.json', 'w') as f2:
                json.dump(data, f2, ensure_ascii=False, indent = 3)
            
            
            self.updateSamples(url)
            
            
            print("-----Completed Samples: ", counter, '-----')
            print("-----Started Time is: ", self.startTime, '---')
            print('----------------------------------------------------------------')
            print('----------------------------------------------------------------')
            
            if counter >= 70:
                print("Warning may arise!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                return
            
            
# use conda to store keys
# get 4 girls from each batch
# get likers(username, name, profilepic ) of those photos
# 






myInstaBot = instaBot(myEmail, myPassword)

myInstaBot.signIn()
# myInstaBot.closePopup()
# myInstaBot.goProfile()
myInstaBot.goToPhoto()
delay(1)
# webdriver.Chrome().close()