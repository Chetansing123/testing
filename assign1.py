from selenium import webdriver
from selenium.webdriver.common.by import By
# set path of the chrome driver

#driver=webdriver.Chrome(executable_path="C:\\Users\\basav\\Downloads\\seleniumdriver\\chromedriver.exe")
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("http://webapps.tekstac.com/InvoiceUpdates/")
#driver.find_element(by=By.XPATH,value="//td[contains(text(),'Customer Name*')]").send_keys("chetansingpatil")
driver.find_element(by=By.XPATH,value="//input[@id='name']").send_keys("chetansing")
driver.find_element(by=By.XPATH,value="//input[@id='number']").send_keys("123")
driver.find_element(by=By.XPATH,value="//input[@id='newUser']").click()
driver.find_element(by=By.XPATH,value="//input[@value='Approved']").click()
driver.find_element(by=By.XPATH,value="//tbody//tr//td//select").send_keys("Utility Invoice")
driver.find_element(by=By.XPATH,value="//input[@name='amount']").send_keys("10000000000")
driver.find_element(by=By.XPATH,value="//input[@name='num']").send_keys("9876543210")
driver.find_element(by=By.XPATH,value="//tbody/tr[8]/td[2]/textarea[1]").send_keys("New User Invoice")
driver.find_element(by=By.XPATH,value="//input[@id='submit']").click()