from selenium import webdriver
from selenium.webdriver.common.by import By

# set path of the chrome driver
#driver=webdriver.Chrome(executable_path="C:\\Users\\ADMIN\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")

# open the url
driver.get("https://demo.guru99.com/test/newtours/")

# conditional statements
#isDisplayed() ,isEnabled() ,isSelected()

print(driver.find_element(by=By.NAME,value="userName").is_displayed())

print(driver.find_element(by=By.NAME,value="userName").is_enabled())

#print(driver.find_element(by=By.NAME,value="userName").is_selected())

# browser response values
print(driver.title)

print(driver.current_url)

print(driver.page_source)




