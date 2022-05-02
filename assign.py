from selenium import webdriver
from selenium.webdriver.common.by import By

# set path of the chrome driver
#driver=webdriver.Chrome(executable_path="C:\\Users\\ADMIN\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")
# open url
driver.get("https://demo.guru99.com/test/newtours/reservation.php")

# locate or identify the radio button
driver.find_element(by=By.XPATH,value="//tbody/tr[2]/td[2]/b[1]/font[1]/input[2]").click()