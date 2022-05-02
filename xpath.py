from selenium import webdriver
from selenium.webdriver.common.by import By

# path of the chrome driver
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")

# open the url
driver.get("https://demo.guru99.com/test/newtours/index.php")

#locate username text box  using basic xpath method
driver.find_element(by=By.xpath,value="//input[@name='username']").send_keys("robert")

# locate password using contains()
driver.find_element(by_By.XPATH,value="//*[contains(@name,'pass']").send_keys("robert")

# locate submit button using or method
driver.find_element(by=By.XPATH,value="//*[@type='submit' or @name='submit']").click()

# locate submit button using And method
driver.find_element(by=By.XPATH,value="//*[@type='submit' or @name='submit']").click()