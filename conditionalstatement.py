from selenium import webdriver
from selenium.webdriver.common.by import By

# set path of the chrome dri
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")

# open the url
driver.get("https://demo.guru99.com/test/newtours/")

#conditional statement
#isDisplayed() ,
print(driver.find_element(by=By.NAME,value="username").is_displayed())
print(driver.find_element(by=By.NAME,value="username").is_enable())

print(driver.title)
print(driver.current_url)
print(driver.page_source)