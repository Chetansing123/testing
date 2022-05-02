import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")
#driver = webdriver.Chrome(executable_path="C:\\Users\\hp\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://webapps.tekstac.com/Agent_Registration/")

driver.find_element(by=By.NAME,value="firstname").send_keys("John")
driver.find_element(by=By.NAME,value="lastname").send_keys("Smith")
driver.find_element(by=By.NAME,value="username").send_keys("Johnsmith")
driver.find_element(by=By.NAME,value="password").send_keys("pass123")
driver.find_element(by=By.NAME,value="phonenumber").send_keys(9876543210)
driver.find_element(by=By.NAME,value="email").send_keys(" ")
driver.find_element(by=By.ID,value="submit").click()

time.sleep(10)
driver.back()
