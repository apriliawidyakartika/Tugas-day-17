import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Tugas_Day_17_Aprilia(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # LOGIN TEST CASE
    def testLogin_failed(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi email
        driver.find_element(By.ID, "user-name").send_keys("inisalah")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "password").send_keys("123456")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    def testLogin_failed_blank(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi email
        driver.find_element(By.ID, "user-name").send_keys("")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "password").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    def testLogin_success(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka websitenya
        driver.maximize_window()
        time.sleep(1)
        # isi email
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()