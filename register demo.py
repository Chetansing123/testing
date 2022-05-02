from selenium import webdriver
from selenium.webdriver.common.by import By

# path of the chrome driver
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")
# open the url
driver.get("https://demo.guru99.com/test/newtours/register.php")

# locate or identify the username text box
driver.find_element(by= By.NAME,value="FirstName").send_keys("KIRA")

# locate or identify password text box
driver.find_element(by=By.NAME,value="LastName").send_keys("admin")

# identify the drop down
select=Select(driver.find_element(by=By.NAME,value="fromPort"))
# locate or identify submit button
#driver.find_element(by=By.NAME,value="submit").click()