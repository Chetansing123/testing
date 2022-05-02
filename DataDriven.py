import time

import ExcelUtil
from selenium import webdriver
from selenium.webdriver.common.by import By

# set the chrome driver path
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://demo.guru99.com/test/newtours/")

#  path of the file which is data source
path =("C:\\Users\\cheta\\Downloads\\testdata.xlsx")

# access the RowCount method
rows = ExcelUtil.getRowCount(path,"Sheet1")
# perform or read the value from excel file and pass to application

for r in range(2,rows+1):
    username= ExcelUtil.ReadData(path,"Sheet1",r,1)
    password= ExcelUtil.ReadData(path,"Sheet1",r,2)

    driver.find_element(by=By.NAME,value="userName").send_keys(username)
    driver.find_element(by=By.NAME,value="password").send_keys(password)
    driver.find_element(by=By.NAME,value="submit").click()

    if driver.title == "Welcome: Mercury Tours":
      #  if driver.title == "webapps.tekstac.com":
        print("Pass")
        ExcelUtil.WriteData(path, "Sheet1", r, 3, "Pass")
    else:
        print("Fail")
        ExcelUtil.WriteData(path, "Sheet1", r, 3, "Fail")

    driver.find_element(by=By.XPATH,value="//a[contains(text(),'Home')]").click()

    time.sleep(20)

    driver.switch_to.alert.accept()