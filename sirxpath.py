from selenium import webdriver
from selenium.webdriver.common.by import By

# path of the chrome driver
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")

# open the url
driver.get("https://demo.guru99.com/test/newtours/index.php")
# locate username text box using Basic xpath mathod
driver.find_element(by=By.XPATH,value="//input[@name='userName']").send_keys("robert")

# locate password using contains()
driver.find_element(by=By.XPATH,value="//*[contains(@name,'pass')]").send_keys("Robert")

# locate submit button using OR method
#driver.find_element(by=By.XPATH,value="//*[@type='submit1' or @name='submit']").click()

# locate submit button using AND method
driver.find_element(by=By.XPATH,value="//input[@type='submit' and @name='submit']")
