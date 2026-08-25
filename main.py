from selenium import webdriver
from selenium.webdriver.common.by import By

# 1 driver tương ứng với 1 session trên browser
# khai báo biến này là global để các function có thể thao tác cùng trên 1 session web đó
driver = webdriver.Chrome()

def open_web(x):
        x.get("https://chgpwd.fpt.edu.vn")
        print('open web success')


def find_input(x):
    
    inputs = x.find_elements(By.TAG_NAME, "input")
    
    print('Amount of input: ', len(inputs))

    for element in inputs:
        print(
            "id =", element.get_attribute("id"),
            "| name =", element.get_attribute("name"),
            "| type =", element.get_attribute("type"),
            "| placeholder =", element.get_attribute("placeholder")
        )

open_web(driver)

find_input(driver)