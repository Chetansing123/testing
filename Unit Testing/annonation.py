import unittest
from selenium import webdriver

class TestAnnotations(unittest.TestCase):
    def test_test1(self):
        print("welcome to test1")

    def test_test2(self):
        print("welcome to test2")

    def test_test3(self):
        print("welcome to test3")

    # this method will be executed before each test
    @classmethod
    def setUp(self):
        print("open browser")
    # this method will be executed after each test
    @classmethod
    def tearDown(self):
        print("close the browser")


# this method will executed only once before all the test method will executed
    @classmethod
    def setUpClass(cls):
        print("connect with DB")

    # this method will executed only once finally
    @classmethod
    def tearDownClass(cls):
        print("close the DB")

