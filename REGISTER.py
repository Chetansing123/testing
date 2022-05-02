from selenium import webdriver
from selenium.webdriver.common.by import By

# path of the chrome driver
driver=webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")
# open the url
driver.get("https://demo.guru99.com/test/newtours/register.php")


driver.find_element(by=By.NAME, value='firstName').send_keys('CHETANSING')
driver.find_element(by=By.NAME, value='lastName').send_keys('PATIL')
driver.find_element(by=By.NAME, value='phone').send_keys(7666722958)
driver.find_element(by=By.NAME, value='userName').send_keys('chetansingpatil123@gmail.com')
driver.find_element(by=By.NAME, value='address1').send_keys('1st main  ')
driver.find_element(by=By.NAME, value='city').send_keys('nashik')
driver.find_element(by=By.NAME, value='state').send_keys('maharashtra')
driver.find_element(by=By.NAME, value='postalCode').send_keys(422009)
driver.find_element(by=By.NAME, value='country').send_keys('INDIA')
driver.find_element(by=By.NAME, value='email').send_keys('chetan1323')
driver.find_element(by=By.NAME, value='password').send_keys(1233)
driver.find_element(by=By.NAME, value='confirmPassword').send_keys(1233)
#driver.find_element(by=By.NAME, value='submit').click()