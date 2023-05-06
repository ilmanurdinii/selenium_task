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

    def test_success_register(self):
        driver = self.driver
        action.register(driver, datas.baseURL, datas.regist_firstname, datas.regist_lastname, datas.regist_email, datas.regist_pass, datas.regist_pass)
        email = driver.find_element(*element.assert_email).text
        url_current = driver.current_url
        self.assertIn(url_current, 'https://demowebshop.tricentis.com/registerresult/1')
        self.assertIn(datas.regist_email, email)
        driver.quit()

    #tidak input firstname 
    def test_failed_register(self):
        driver = self.driver
        action.register(driver, datas.baseURL, "", datas.regist_lastname, datas.regist_email, datas.regist_pass, datas.regist_pass)
        test_validasi = driver.find_element(*element.no_firstname_validation).text
        self.assertIn(test_validasi, "First name is required.")
        driver.quit()

    def test_failed_register_no_firstandlasname(self):
        driver = self.driver
        action.register(driver, datas.baseURL, "", "", datas.regist_email, datas.regist_pass, datas.regist_pass)
        test_validasi = driver.find_element(*element.no_firstname_validation).text
        test_validasi2 = driver.find_element(*element.no_lastname_validation).text
        self.assertIn(test_validasi, "First name is required.")
        self.assertIn(test_validasi2, "Last name is required.")
        driver.quit()


if __name__ == "__main__":
    unittest.main()