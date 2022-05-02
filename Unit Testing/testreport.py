import unittest

import HtmlTestRunner
import pythonProject as pythonProject

from selenium import webdriver
from selenium.webdriver.common.by import By


# creating an class extracted from unit test
class searchengine(unittest.TestCase):

    # creating user defined methods
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("http://www.google.com")
        print("The Title of the page is:" + self.driver.title)
        self.driver.close()

    def test_binge(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\cheta\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.binge.com")
        print("The Title of the page is:" + self.driver.title)
        self.driver.close()


# to run the test methods we need to create main method
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\cheta\\pythonProject\\selenium\\Unit Testing'\\'HtmlReports'))
#'C:\\Users\\ADMIN\\PycharmProjects\\SeleniumTesting''\\Reports'))
#'C:\\Users\\cheta\\pythonProject\\selenium\\Unit Testing'\\'HtmlReports'
#HtmlReports
#Unit Testing//HtmlReports
    C:\\Users\cheta\pythonProject\selenium\Unit
    Testing\HtmlReports
# to Run go to terminal and type python Tescase1.py