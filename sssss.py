from selenium import webdriver
from selenium.webdriver.common.by import By


# set path of the chrome driver
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")


# open the url
driver.get("https://demo.guru99.com/test/newtours/")

# taking screenshot
driver.save_screenshot("C:\\Users\\cheta\\Desktop\\nnn\\homepage.png")

# take an screenshot
#driver.get_screenshot_as_file("C:\\Users\\ADADDIKA\\AppData\\Local\\Microsoft\\WindowsApps\\homepage1.jpeg")
