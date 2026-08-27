from selenium import webdriver
from selenium.webdriver.common.by import By

# ngăn không cho web tự động tắt
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# 1 driver tương ứng với 1 session trên browser
# khai báo biến này là global để các function có thể thao tác cùng trên 1 session web đó
driver = webdriver.Chrome()

real_inputs = []

def open_web(x):
    
        x.get("https://chgpwd.fpt.edu.vn")
        print('open web success')


def find_input(x):
    
    inputs = x.find_elements(By.TAG_NAME, "input")

    for element in inputs:
        if element.get_attribute('id') == 'txt_Username_mail' or element.get_attribute('id') == 'txt_mail':
            real_inputs.append(element)
            
def input_account():
    
    account = input('account: ')
    email = input('email: ')
    
    return account, email
    
    
def put_input(account, email):
    real_inputs[0] = account
    real_inputs[1] = email


if __name__ == "__main__":
    
    open_web(driver)

    find_input(driver)

    account, email = input_account()
    
    put_input(account, email)
    
    print(real_inputs[0])
    print(real_inputs[1])
    