from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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
    


    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        delay(2)
        emailInput =  self.browser.find_element_by_name("username")
        passwordInput = self.browser.find_element_by_name("password")

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
        self.browser.get('https://www.instagram.com/asdfasdf/')
        delay(2)
        
    def goToPhoto(self):
        self.browser.get('https://www.instagram.com/p/BXXVl5dFcxC/')
        # see likers
        delay(2)
        andOthers = self.browser.find_elements_by_class_name("sqdOP")[1]
        andOthers.click()
        delay(2)
        #got to profile of one liker
        people =  self.browser.find_elements_by_class_name("_2dbep")
        likers = []
        # print(len(people))
        for person in people:
            personId = person.get_attribute('href')
            
            if personId != None and personId != 'https://www.instagram.com/asdfasdfasdf/':
                likers.append(personId)
        
        samplePhotos = []
        for liker in likers:
            self.browser.get(liker)
            























myInstaBot = instaBot('test@gmail.com', 'rapapapa234%#$asdf')
myInstaBot.signIn()
# myInstaBot.closePopup()
# myInstaBot.goProfile()
myInstaBot.goToPhoto()
delay(1)
# webdriver.Chrome().close()