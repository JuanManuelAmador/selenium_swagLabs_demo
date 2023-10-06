from selenium import webdriver
from selenium.webdriver.common.by import By

class homePage(object):
    #Login Locators
    userNameLocator = "//input[@id='user-name']"
    passwordLocator = "//input[@id='password']"
    loginButtonLocator = "//input[@id='login-button']"
    errorMsgWrongPwUserLocator = "//*[text()='Epic sadface: Username and password do not match any user in this service']"
    errorMsgLockedOutUserLocator = "//*[text()='Epic sadface: Sorry, this user has been locked out.']"
    errorMsgbuttonLocator = "//button[@class='error-button']"
    #Logout Locators
    burgerButtonLocator = "//button[@id='react-burger-menu-btn']"
    logoutButtonLocator = "//a[@id='logout_sidebar_link'][@class='bm-item menu-item']"
    
    
    def __init__(self,driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        
    def login(self,username,password):
        
        self.driver.find_element(By.XPATH, self.userNameLocator).send_keys(username)
        self.driver.find_element(By.XPATH, self.passwordLocator).send_keys(password)
        self.driver.find_element(By.XPATH, self.loginButtonLocator).click()
        
    def logout(self):
        self.driver.find_element(By.XPATH, self.burgerButtonLocator).click()
        self.driver.find_element(By.XPATH, self.logoutButtonLocator).click()
        
    def close_errorMsg(self):
        self.driver.find_element(By.XPATH, self.errorMsgbuttonLocator).click()
        
    
    #Not required in the document but added in case we need to test the cart
    def add_to_cart(self, item_name):
        self.driver.find_element_by_xpath(f"//div[text()='{item_name}']/following-sibling::div/button").click()
    
    #Not required in the document but added in case we need to test the cart
    def checkout(self):
        self.driver.find_element_by_id("shopping_cart_container").click()
        self.driver.find_element_by_id("checkout").click()
    
    #Not required in the document but added in case we need to test the cart
    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.driver.find_element_by_id("first-name").send_keys(first_name)
        self.driver.find_element_by_id("last-name").send_keys(last_name)
        self.driver.find_element_by_id("postal-code").send_keys(zip_code)
        self.driver.find_element_by_id("continue").click()
    
    def finish_checkout(self):
        self.driver.find_element_by_id("finish").click()
    
    
    def close(self):
        self.driver.quit()
