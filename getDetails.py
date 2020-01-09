from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import time
from datetime import datetime
import json
import urlparse


def delay( timeValue):
    time.sleep(timeValue)
        

myId = 'asdfasdf'
myEmail = 'asdfasd@gmail.com'
myPassword = 'asdfasdf'

class detailsBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
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
    
    def crawl(self):
        # with open('wrcians.json') as f11:
        #     allSamples = json.load(f11)
        
        self.browser.get('https://www.facebook.com/'+'asdfasdfasdfasdfasdfasdfasdf')
        # self.browser.send_keys(Keys.CONTROL + 'r')
        fullName = self.browser.title.split('|')[0]
        
        # photoElement = self.browser.find_elements_by_xpath("//*[@class='_11kf']")[0]
        photoElement = self.browser.find_elements_by_class_name("_11kf")[0]
        photoSrc = photoElement.get_attribute('src')
        print (fullName)
        print(photoSrc)
        self.browser.get(photoSrc)
        
            

myBot = detailsBot(myEmail, myPassword)
myBot.signIn()
myBot.crawl()
