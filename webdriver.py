import ExcelUtil
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://webapps.tekstac.com/Agent_Registration/")
#path = ("C:\\Users\\cheta\\Downloads\\activity2.xlsx")

rows=ExcelUtil.getRowCount(path,"Sheet1")

#perform the read
for r in range(2,rows+1):
   firstname = ExcelUtil.ReadData(path,"Sheet1",r,1)
   lastname = ExcelUtil.ReadData(path,"Sheet1",r,2)
   username = ExcelUtil.ReadData(path, "Sheet1", r, 3)
   password = ExcelUtil.ReadData(path, "Sheet1", r, 4)
   phonenumber = ExcelUtil.ReadData(path, "Sheet1", r, 5)
   email = ExcelUtil.ReadData(path, "Sheet1", r, 6)

   driver.find_element(by=By.NAME,value="firstname").send_keys(firstname)
   driver.find_element(by=By.NAME, value="lastname").send_keys(lastname)
   driver.find_element(by=By.NAME, value="username").send_keys(username)
   driver.find_element(by=By.NAME, value="password").send_keys(password)
   driver.find_element(by=By.NAME, value="phonenumber").send_keys(phonenumber)
   driver.find_element(by=By.NAME, value="email").send_keys("")
   driver.find_element(by=By.ID, value="submit").click()

   if driver.title == "webapps tekstac com":
        print("PASS")
        ExcelUtil.WriteData(path, "Sheet1", r, 7, "Pass")
   else:
        print("Fail")
        ExcelUtil.WriteData(path, "Sheet1", r, 7, "The error message for 'Email cannot be blank'should be displayed ")
   driver.find_element(by=By.XPATH,value="//body/div[@id='wrapper']/main[@id='middle']/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]").click()

   # time.sleep(120)
#driver.switch_to.alert.accept()