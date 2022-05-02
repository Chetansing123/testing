from selenium import webdriver
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Guru99Demo(unittest.TestCase):
    def setUp(self):
        global driver
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")

        self.driver.get("https://demo.guru99.com/test/newtours/index.php")
        self.driver.maximize_window()

    def test(self):  //body[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[5]/td[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]
        self.driver.find_element(By.XPATH,"//body[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[2]").click()
        self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]").send_keys("chetansing")
        self.driver.find_element(By.XPATH, "// tbody / tr[3] / td[2] / input[1]").send_keys("patil")
        self.driver.find_element(By.XPATH, "//tbody/tr[4]/td[2]/input[1]").send_keys("7666722958")
        self.driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("chetansingpatil123@gmail.com")
        self.driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]").send_keys("Athani")
        self.driver.find_element(By.XPATH, " //tbody/tr[8]/td[2]/input[1]").send_keys("nashik")
        self.driver.find_element(By.XPATH, " //tbody/tr[9]/td[2]/input[1]").send_keys("mahrashtra")
        self.driver.find_element(By.XPATH, " //tbody/tr[10]/td[2]/input[1]").send_keys("591304")
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/select[1]").send_keys("India")
        self.driver.find_element(By.XPATH, " //input[@id='email']").send_keys("Basavaraj_98")
        self.driver.find_element(By.XPATH, "//tbody/tr[14]/td[2]/input[1]").send_keys("12121998")
        self.driver.find_element(By.XPATH, "//tbody/tr[15]/td[2]/input[1]").send_keys("12121998")
        self.driver.find_element(By.XPATH, "//tbody/tr[17]/td[1]/input[1]").click()

    def tearDown(self):
       self.driver.close()

if _name=="main_":
    unittest.main()