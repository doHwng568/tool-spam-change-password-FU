from selenium import webdriver
from selenium.webdriver.common.by import By

# ngăn không cho web tự động tắt
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# 1 driver tương ứng với 1 session trên browser
# khai báo biến này là global để các function có thể thao tác cùng trên 1 session web đó
driver = webdriver.Chrome()

def open_web(x):
    
        x.get("https://chgpwd.fpt.edu.vn")
        print('open web success')

            
def input_account():
    
    account = input('account: ')
    email = input('email: ')
    
    return account, email
    
    
def put_input(account, email):
    
    driver.find_element(By.ID, 'txt_Username_mail').send_keys(account)
    driver.find_element(By.ID, 'txt_mail').send_keys(email)

if __name__ == "__main__":
    
    open_web(driver)

    account, email = input_account()
    
    put_input(account, email)
    
    