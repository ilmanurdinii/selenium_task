import BaseFunction.Base_Function as functions

class datas():
    baseURL = "https://demowebshop.tricentis.com/"
    regist_firstname = functions.get_random_string(4)
    regist_lastname = functions.get_random_string(6)
    regist_email = functions.get_random_string(6)+"@gmail.com"
    regist_pass = "password123"
    regist_invalid_pass ="password"
    valid_email = "irumadesu@gmail.com"
    invalid_user = "irumadesune@gmail.com"
    valid_pass = "password123"
    invalid_pass = "salahpassword123"
