import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# set path of the chrome driver
#driver=webdriver.Chrome(executable_path="C:\\Users\\ADMIN\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")

# open the url
driver.get("https://demo.guru99.com/test/newtours/")

# add pageloadtimeout
driver.set_page_load_timeout(300)


# add implicit wait
#driver.implicitly_wait(40)
driver.find_element(by=By.NAME,value="userName").send_keys("admin")

# add time sleep
time.sleep(40)
driver.find_element(by=By.NAME,value="password").send_keys("admin")
# add explicit wait statement
element = webdriver(driver,50).until(EC.presence_of_element_located(By.NAME,"submit"))



driver.find_element(by=By.NAME,value="submit").click()


def webdriver():
    return None


def webdriver():
    return None


def webdriver():
    return None


def webdriver():
    return None


def webdriver():
    return None


def webdriver():
    return None


def webdriver():
    return None


def webdriver():
    return None


def webdriver():
    return None