from selenium.webdriver.common.by import By

class element():
    goto_regist_btn = By.XPATH, "//a[@class='ico-register']"
    regist_gender = By.XPATH, "//input[@id='gender-male']"
    regist_firstname = By.XPATH, "//input[@id='FirstName']"
    regist_lastname = By.XPATH, "//input[@id='LastName']"
    regist_email = By.XPATH, "//input[@id='Email']"
    regist_pass = By.XPATH, "//input[@id='Password']"
    regist_confirm_pass = By.XPATH, "//input[@id='ConfirmPassword']"
    regist_btn = By.XPATH, "//input[@id='register-button']"

    no_firstname_validation = By.XPATH, "//span[@for='FirstName']"
    no_lastname_validation = By.XPATH, "//span[@for='LastName']"

    continue_after_register = By.XPATH, "//input[@value='Continue']"
    no_city = By.XPATH, "//span[normalize-space()='City is required']"

    goto_login_btn = By.XPATH, "//a[@class='ico-login']"
    login_email = By.XPATH, "//input[@id='Email']"
    login_pass = By.XPATH, "//input[@id='Password']"
    login_check_remember = By.XPATH, "//input[@id='RememberMe']"
    login_forgot_pass = By.XPATH, "//a[normalize-space()='Forgot password?']"
    login_btn = By.XPATH, "//input[@value='Log in']"
    failed_login = By.XPATH, "//span[contains(text(),'Login was unsuccessful. Please correct the errors ')]"
    
    assert_email = By.XPATH, "//a[@class='account']"

    addtocart_btn = By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[3]/div/div/div[3]/div[3]/div/div[2]/div[3]/div[2]/input"
    recipient_name = By.XPATH, "//input[@id='giftcard_2_RecipientName']"
    recipient_email = By.XPATH, "//input[@id='giftcard_2_RecipientEmail']"
    message = By.XPATH, "//textarea[@id='giftcard_2_Message']"
    qty = By.XPATH,"//input[@id='addtocart_2_EnteredQuantity']"
    add_to_cart = By.XPATH, "//input[@id='add-to-cart-button-2']"

    cart_btn = By.XPATH, "//*[@id='topcartlink']/a/span[2]"

    agree_checkout = By.XPATH, "//input[@id='termsofservice']"
    checkout_btn = By.XPATH, "//button[@id='checkout']"
    select_country = By.CSS_SELECTOR, "#BillingNewAddress_CountryId"
    country = By.XPATH, '//*[@id="BillingNewAddress_CountryId"]/option[2]'
    city = By.XPATH, "//input[@id='BillingNewAddress_City']"
    address = By.XPATH, "//input[@id='BillingNewAddress_Address1']"
    zipcode = By.CSS_SELECTOR, "#BillingNewAddress_ZipPostalCode"
    phone = By.CSS_SELECTOR, "#BillingNewAddress_PhoneNumber"

    continue_btn = By.XPATH, "//input[@onclick='Billing.save()']"
    continue_btn_2 = By.XPATH, "//input[@onclick='Shipping.save()']"
    continue_btn_3 = By.XPATH, "//input[@class='button-1 shipping-method-next-step-button']"
    continue_btn_4 = By.XPATH, "//input[@class='button-1 payment-method-next-step-button']"
    continue_btn_5 = By.XPATH, "//input[@class='button-1 payment-info-next-step-button']"
    confirm_btn = By.XPATH, "//input[@value='Confirm']"

    assert_checkout = By.XPATH, "//strong[normalize-space()='Your order has been successfully processed!']"
    

