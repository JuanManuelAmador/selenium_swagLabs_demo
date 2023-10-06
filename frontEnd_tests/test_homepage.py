import unittest
from selenium import webdriver
from homePage_page import homePage
from selenium.webdriver.common.by import By


class TestHomePage(unittest.TestCase):

    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.homePage = homePage(self.driver)        
        
    def test_login_positive(self):
        self.homePage.login("standard_user", "secret_sauce")
        self.assertTrue(self.driver.find_element(By.XPATH, self.homePage.burgerButtonLocator).is_displayed())
        self.homePage.logout()
        self.assertTrue(self.driver.find_element(By.XPATH, self.homePage.loginButtonLocator).is_displayed()) 
        
    def test_login_positive_slow(self):
        self.homePage.login("performance_glitch_user", "secret_sauce")
        self.assertTrue(self.driver.find_element(By.XPATH, self.homePage.burgerButtonLocator).is_displayed())
        self.homePage.logout()
        self.assertTrue(self.driver.find_element(By.XPATH, self.homePage.loginButtonLocator).is_displayed())
        
    def test_login_wrong_mail(self):
        self.homePage.login("wrongMail", "secret_sauce")
        self.assertTrue(self.driver.find_element(By.XPATH, self.homePage.errorMsgWrongPwUserLocator).is_displayed())
        self.homePage.close_errorMsg()
        
    def test_login_wrong_password(self):
        self.homePage.login("standard_user", "wrongPassword")
        self.assertTrue(self.driver.find_element(By.XPATH, self.homePage.errorMsgWrongPwUserLocator).is_displayed())
        self.homePage.close_errorMsg()
    
    def test_login_lockedUser(self):
        self.homePage.login("locked_out_user","secret_sauce")
        self.assertTrue(self.driver.find_element(By.XPATH, self.homePage.errorMsgLockedOutUserLocator).is_displayed())
        self.homePage.close_errorMsg()
                
    def tearDown(self):
        print("Cleanup of test environment")
        self.driver.close()
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()