from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://demo.guru99.com/test/newtours/")

# taking screenshot
driver.save_screenshot("c\\users\\cheta\\desktop\\screenshot\\homepage.png")