from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class homePage(object):
    #Home Locators
    logoLocator = "//a[@class='logo']"
    
    def __init__(self,driver):
        self.driver = driver
    
    def close(self):
        self.driver.quit()