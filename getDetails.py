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


def delay( timeValue):
    time.sleep(timeValue)
        

myEmail = 'reerereerere@gmail.com'
myPassword = 'asdfawefasdf'

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
        
    def updateWrcians(self, usernameToBeRemoved):
        with open('wrcians2.json') as ff11:
            bakiWrcians = json.load(ff11)
        bakiWrcians.remove(usernameToBeRemoved)
            
        with open('wrcians2.json', 'w') as ff22:
            json.dump(bakiWrcians, ff22, ensure_ascii=False, indent = 3)
          
    
    
    
    def crawl(self):
        
        doneCounter = 0
        
        with open('wrcians2.json') as f11:
            dumbas = json.load(f11)
        
        for dumba in dumbas:
            self.browser.get('https://www.facebook.com'+dumba)
            fullName = self.browser.title.split('|')[0]
            if fullName[0] == '(':
                fullName = fullName.split(') ')[-1]
            profilePic = self.browser.find_elements_by_class_name("profilePicThumb")[0]
            profilePic.click()
            pictureUrl = ''
            alt = 'test'
            
            looper = True
            while looper:
                try:
                    picture = self.browser.find_elements_by_class_name("spotlight")[0]
                    pictureUrl = picture.get_attribute("src")
                except:
                    picture = self.browser.find_elements_by_tag_name("img")[-1]
                    pictureUrl = picture.get_attribute("src")
                
                shouldILoop = ('https://static.xx.' in pictureUrl) or \
                    ('https://scontent.fktm3-1.fna.fbcdn.net/v/t1.0-1/cp0' in pictureUrl) or \
                    ('c0.0.32.32a/p32x32' in pictureUrl) or \
                    ('p32x32' in pictureUrl) or \
                    ('p24x24' in pictureUrl) or \
                    ('https://scontent.fktm3-1.fna.fbcdn.net/v/t31.0-1/cp0' in pictureUrl)
                
                if not shouldILoop:
                    print(pictureUrl)   
                    print (fullName)
                    looper = False
                    
                    with open('dumbasData.json', encoding="utf-8") as file1:
                        dumbasData = json.load(file1)
                        
                    dumbasData.append({
                        'username': dumba,
                        'name':fullName,
                        'pictureUrl': pictureUrl
                    })
                    
                    with open('dumbasData.json', 'w', encoding="utf-8") as file2:
                        json.dump(dumbasData, file2, ensure_ascii=False, indent = 3)
                        
                    self.updateWrcians(dumba)
                    
                     
                    
                    doneCounter += 1
                    print('----------------------------------------------------------------')
                    print('----------------------------------------------------------------')                    
                    print("-----Mined Total:      ", len(dumbasData), '-----')
                    print("-----Mined Today:      ", doneCounter, '-----')
                    print("-----Left To Mine:     ", len(dumbas), '-----')
                    print("-----Total Candidates: ", 40, '-----')
                    print("-----Started Time is:  ", self.startTime, '---')
                    print('----------------------------------------------------------------')
                    print('----------------------------------------------------------------')
                    
            

myBot = detailsBot(myEmail, myPassword)
myBot.signIn()
myBot.crawl()
