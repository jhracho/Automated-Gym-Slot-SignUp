# Selenium-driven program that automatically completes a SignUpGenius form to sign-up for gym slots faster than anyone could possibly type

# Import Dependencies
import sys
import os
import time
import string

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Import XPATH Library
from XPathLib import *

# Globals
URL = 'https://www.signupgenius.com/go/70a0b48aaaa28aaf85-test1'
driverPATH = "chromedriver.exe"
ALPHABET = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Gym Bot Selenium Class and Functions
class gymBOT():
    # Starts Bot
    def __init__(self, buttonLIST):
        # Initialize
        self.driver = webdriver.Chrome(executable_path=driverPATH)
        URL  = input("Enter URL: ")
        CODE = input("Enter Code: ") 
        self.driver.get(URL)
        self.xpathLIST = buttonLIST

        time.sleep(0.5)
        enterCode   = self.driver.find_element_by_xpath('//*[@id="passcodeId"]').send_keys(CODE)
        submitCode  = self.driver.find_element_by_xpath('//*[@id="CFForm_1"]/div/input').click()
        time.sleep(0.5)
        gotItButton = self.driver.find_element_by_xpath('/html/body/div[3]/div/span[2]/a').click()

    # Cycles through XPATHs and clicks each button
    def reserveTimes(self):
        for xpath in self.xpathLIST:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            button = self.driver.find_element_by_xpath(xpath)
            html = button.get_attribute("innerHTML")
            soup = BeautifulSoup(html, 'html.parser')
            foundID = soup.find('input')['id']
            newXPATH = '//*[@id=\"' + foundID + '\"]'
            print("CLICKING NEW BUTTON")
            checkbox = self.driver.find_element_by_xpath(newXPATH).click() 

        submitButton = self.driver.find_element_by_xpath('//*[@id="submitfooter"]/div/input').click()
        
    # Completes sign-up by automatically adding contact info
    def FinishTheJob(self):
        time.sleep(0.5)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        firstName = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "firstname"))).send_keys('Jake')
        lastName = self.driver.find_element_by_xpath('//*[@id="lastname"]').send_keys('Hracho')
        email = self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('email@email.com')
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        Complete = self.driver.find_element_by_xpath('//*[@id="SUGContainer"]/div[2]/div/div[2]/div[1]/div[3]/div/span/span[2]/button').click()

# Main Execution
arguments = sys.argv[1:]
xpathLIST = getXPATHList(getXPATHNumbers(arguments))

# Run the Bot
bot = gymBOT(xpathLIST)
bot.reserveTimes()
bot.FinishTheJob()