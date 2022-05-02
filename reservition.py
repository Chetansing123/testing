from selenium import webdriver
from selenium.webdriver.common.by import By

# path of the chrome driver
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")
# open the url
driver.get("https://demo.guru99.com/test/newtours/reservation.php")

# locate or identify the username text box
