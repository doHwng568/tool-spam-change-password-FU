from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ngăn không cho web tự động tắt
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# log-level quyết định mức độ ghi log của Chrome
# chỉ giữ lại log ở level 3 (FATAL), còn các log ở level 0 (INFO), 1 (WARNING), 2 (ERROR) thì sẽ bỏ qua -> giảm mức độ ghi log của Chrome
options.add_argument('--log-level=3')

# luồng điều khiển làL: python -> selenium -> chrome driver -> chrome
# Chrome driver khởi động Chrome với rất nhiều tham số (args), trong đó có 'enable-logging' để ghi log các thành phần bên trong Chrome
# dòng config dưới đây giúp chrome driver không khởi tạo tham số 'enable logging' của trình duyệt nữa
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Disables DevTools logging

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
    
    # đợi đến khi có message với id 'lbMessage' xuất hiện
    wait.until(
        EC.visibility_of_element_located((By.ID, "lbMessage"))
    )
    
    print('end')
    