import unittest
from selenium import webdriver
from login_page import loginPage
from selenium.webdriver.common.by import By
import time
from home_page import homePage

class TestHomePage(unittest.TestCase):

    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.loginPage = loginPage(self.driver)  
        self.homePage = homePage(self.driver)       
        
    def test_login_positive(self):
        self.loginPage.login("frontend_qa+dev-company@shipwell.com", "QA_password@123")
        time.sleep(10)
        self.assertTrue(self.driver.find_element(By.XPATH, self.homePage.logoLocator).is_displayed())
             
    def tearDown(self):
        print("Cleanup of test environment")
        self.driver.close()
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()