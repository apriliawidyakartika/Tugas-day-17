import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Tugas_Day_17_Aprilia(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_remove_cart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # buka websitenya
        driver.maximize_window()
        time.sleep(2)
        # isi email
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        time.sleep(1)
        # isi Password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()