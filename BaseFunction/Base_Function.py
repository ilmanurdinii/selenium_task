from PageObject.elements import element
import string
import random 


"""def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())"""

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def login(driver, URL, email, password):
    driver.get(URL)
    driver.maximize_window()
    driver.find_element(*element.goto_login_btn).click()
    driver.find_element(*element.login_email).send_keys(email)
    driver.find_element(*element.login_pass).send_keys(password)
    driver.find_element(*element.login_btn).click()

def register(driver, URL, firstname, lastname, email, password, confirm_password):
    driver.get(URL)
    driver.maximize_window()
    driver.find_element(*element.goto_regist_btn).click()
    driver.find_element(*element.regist_gender).click()
    driver.find_element(*element.regist_firstname).send_keys(firstname)
    driver.find_element(*element.regist_lastname).send_keys(lastname)
    driver.find_element(*element.regist_email).send_keys(email)
    driver.find_element(*element.regist_pass).send_keys(password)
    driver.find_element(*element.regist_confirm_pass).send_keys(confirm_password)
    driver.find_element(*element.regist_btn).click()
    driver.implicitly_wait(5)

def add_to_cart(driver):
    driver.find_element(*element.addtocart_btn).click()

#checkout dengan data yang sudah pernah diinput 
def checkout (driver):
    driver.find_element(*element.cart_btn).click()
    driver.find_element(*element.agree_checkout).click()
    driver.find_element(*element.checkout_btn).click()
    #data insert nanti aja 
    driver.find_element(*element.continue_btn).click()
    driver.implicitly_wait(5)

#checkout dengan data yang sudah pernah diinput 
def newcheckout (driver, city, address, zipcode, phone):
    driver.find_element(*element.cart_btn).click()
    driver.find_element(*element.agree_checkout).click()
    driver.find_element(*element.checkout_btn).click()
    #data insert 
    driver.find_element(*element.select_country).click()
    driver.find_element(*element.country).click()
    driver.find_element(*element.city).send_keys(city)
    driver.find_element(*element.address).send_keys(address)
    driver.find_element(*element.zipcode).send_keys(zipcode)
    driver.find_element(*element.phone).send_keys(phone)
    #continue 
    driver.find_element(*element.continue_btn).click()

def continue_checkout(driver):
    driver.implicitly_wait(5)
    driver.find_element(*element.continue_btn_2).click()
    driver.find_element(*element.continue_btn_3).click()
    driver.find_element(*element.continue_btn_4).click()
    driver.find_element(*element.continue_btn_5).click()
    driver.find_element(*element.confirm_btn).click()
