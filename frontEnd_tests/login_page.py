from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class loginPage(object):
    #Login Locators
    userNameLocator = "//input[@id='email']"
    passwordLocator = "//input[@id='password']"
    loginButtonLocator = "//button[@id='btn-login']"
   
    
    
    def __init__(self,driver):
        self.driver = driver
        self.driver.get("https://dev-app.shipwell.com/")
        
    def login(self,username,password):
        
        self.driver.find_element(By.XPATH, self.userNameLocator).send_keys(username)
        self.driver.find_element(By.XPATH, self.passwordLocator).send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.loginButtonLocator).click()
    
    def close(self):
        self.driver.quit()
