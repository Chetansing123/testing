from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# set path of the chrome drivert(by=By.NAME,value="fromPort"))
#
# # select the drop down values using Select Class
# Select.select_by_index(3)
#
# #Select.select_by_value("New York")
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")

# open the url
driver.get("https://demo.guru99.com/test/newtours/reservation.php")

# identify the drop down
Select=Select(driver.find_elemen



