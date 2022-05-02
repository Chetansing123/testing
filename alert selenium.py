import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# path of the chrome driver
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")

# open the url
driver.get("http://demo.automationtesting.in/Alerts.html")

# click on the alert button
driver.find_element(by=By.XPATH,value="//button[contains(text(),'alert box:')]").click()

time.sleep(40)
# handling alert using accept()
driver.switch_to.alert.accept()

# locate an button with ok & cancel
driver.find_element(by=By.XPATH,value="//a[contains(text(),'Alert with OK & Cancel')]").click()

#locate or click on the alert button
driver.find_element(by=By.XPATH,value="//button[contains(text(),'click the button to display a confirm box')]").click()

time.sleep(40)

# get the alert message


# handle the alert using dismiss()
driver.switch_to.alert.dismiss()

