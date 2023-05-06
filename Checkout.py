
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.elements import element 
from PageObject.data import datas
import BaseFunction.Base_Function as action 

class demoweb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #checkout dengan data yg belum ada 
    def test_success_new_checkout(self):
        driver = self.driver
        action.register(driver, datas.baseURL, datas.regist_firstname, datas.regist_lastname, datas.regist_email+"m", datas.regist_pass, datas.regist_pass)
        driver.find_element(*element.continue_after_register).click()
        action.add_to_cart(driver)
        action.newcheckout(driver, "Pasuruan", "Pecalukan Timur", "67157", "082111410042")
        action.continue_checkout(driver)
        asser_success = driver.find_element(*element.assert_checkout).text
        self.assertIn("Your order has been successfully processed!", asser_success)
        driver.quit()

    def test_failed_new_checkout(self):
        driver = self.driver
        action.register(driver, datas.baseURL, datas.regist_firstname, datas.regist_lastname, datas.regist_email, datas.regist_pass, datas.regist_pass)
        driver.find_element(*element.continue_after_register).click()
        action.add_to_cart(driver)
        action.newcheckout(driver, "", "Pecalukan Timur", "67157", "082111410042")
        assert(driver.find_element(*element.no_city))
        driver.quit()
    
    #checkout dengan data yang sudah ada 
    def test_success_existing_checkout_data(self):
        driver = self.driver
        action.login(driver, datas.baseURL, datas.valid_email, datas.valid_pass)
        action.add_to_cart(driver)
        action.checkout(driver)
        action.continue_checkout(driver)
        asser_success = driver.find_element(*element.assert_checkout).text
        self.assertIn("Your order has been successfully processed!", asser_success)
        driver.quit()


if __name__ == "__main__":
    unittest.main()