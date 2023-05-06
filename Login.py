
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PageObject.elements import element 
from PageObject.data import datas
import BaseFunction.Base_Function as action 

class demoweb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self):
        driver = self.driver
        action.login(driver, datas.baseURL, datas.valid_email, datas.valid_pass)
        email = driver.find_element(*element.assert_email).text
        self.assertIn(datas.valid_email, email)
        driver.quit()
    
    def test_failed_login(self):
        driver = self.driver
        action.login(driver, datas.baseURL, datas.invalid_user, datas.valid_pass)
        assert(driver.find_element(*element.failed_login))
        driver.quit()



if __name__ == "__main__":
    unittest.main()