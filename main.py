from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ngăn không cho web tự động tắt
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# 1 driver tương ứng với 1 session trên browser
# khai báo biến này là global để các function có thể thao tác cùng trên 1 session web đó
driver = webdriver.Chrome(options=options)

# tạo đối tượng chờ với thời gian chờ tối đa là 10s
wait = WebDriverWait(driver, 10)

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
    
def click_button(id):
    driver.find_element(By.ID, id).click()

while(True):
    
    open_web(driver)

    account, email = input_account()
    
    put_input(account, email)
    
    # click enter
    click_button('submitmail')
    
    wait.until(
        EC.visibility_of_element_located((By.ID, "lbMessage"))
    )
    
    print('end')
    