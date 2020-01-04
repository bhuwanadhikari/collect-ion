from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import urlparse


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

class instaBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
        self.sampleFriends = []
    


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
        self.browser.get('https://www.instagram.com/luminousbhuwan/')
        delay(2)
        
    def goToPhoto(self):
        self.browser.get('https://www.facebook.com/photo.php?fbid=2193040064331951&set=a.1377214452581187&type=3&theater')
        # see likers
        delay(2)
        likeNumber1 = self.browser.find_elements_by_class_name("_3dlf")[1]
        likeNumber1.click()
        delay(5)
        
        #get primary likers
        samples =  self.browser.find_elements_by_class_name("_5i_s")
        sampleUrls = []
        for sample in samples:
            sampleUrl = sample.get_attribute('href')
            sampleUrls.append(sampleUrl)
            
            
        mainData = []
        for url in sampleUrls:
            
            #visit one of the liker
            # self.browser.get(url)
            
            #get username of liker
            sampleId = urlparse.urlparse(url).path
            samplePhotoData = {}
            
            #visit all photos of liker
            print('Visiting all photos of', sampleId)
            if sampleId == '/luminousbhuwan' or sampleId == '/profile.php' or sampleId == '/photo.php': continue
            self.browser.get('https://www.facebook.com'+sampleId+'/photos_all')
            
            #visit one photo of liker
            photosOfLiker =  self.browser.find_elements_by_class_name("uiMediaThumbMedium")
            if  len(photosOfLiker) < 2 : continue
            photoOfLiker = photosOfLiker[1]
            # photoOfLiker.click()
            self.browser.get(photoOfLiker.get_attribute('href'))
            print('Visiting a single photo of', sampleId)
            
            
            #visit to the list of secondary likers
            clickButtons = self.browser.find_elements_by_class_name("_3dlf")
            if len(clickButtons) < 2: continue
            print('lenght of buttons is', len(clickButtons))
            likeNumber2= clickButtons[1]
            # likeNumber2.click()
            
            

            actions = ActionChains(self.browser)

            actions.move_to_element(likeNumber2).click().perform()
            
            
            print('Seeing Likers of a photo of', sampleId)
            delay(2)
            
            #get all secondary likers
            likers = self.browser.find_elements_by_class_name("_5i_s")
            
            
            likersUrl =[]
            likersId =[]
            
            for liker in likers:
                likerUrl = liker.get_attribute('href')
                likerId = urlparse.urlparse(likerUrl).path
                print('secondary liker is', likerId)
                likersUrl.append(likerUrl)
                likersId.append(likerId)
        
            # make sample photo data ready
            
            
            samplePhotoData['photoOf'] = sampleId
            # samplePhotoData['likersUrl'] = likersUrl
            samplePhotoData['likersId'] = likersId
            
            # add sample photo data to main data
            mainData.append(samplePhotoData)
            with open('mainData.json', 'w') as f:
                json.dump(mainData, f, ensure_ascii=False, indent = 3)
            # print(json.dumps(mainData, indent = 4))
            
            























myInstaBot = instaBot('testemail@gmail.com', 'testpass')
myInstaBot.signIn()
# myInstaBot.closePopup()
# myInstaBot.goProfile()
myInstaBot.goToPhoto()
delay(1)
# webdriver.Chrome().close()