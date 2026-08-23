from selenium import webdriver

def open_web():
    driver = webdriver.Chrome()

    try:
        driver.get("https://chgpwd.fpt.edu.vn")

    finally:
        print('ok')


open_web()