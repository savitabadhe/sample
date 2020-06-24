import time
import unittest

import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.loginPage import LoginPage
from pages.serachPage import SearchPage


class LoginTests(unittest.TestCase):

    def test_Login(self):
        baseURL = "https://timesheet.nitorinfotech.net/"
        # chromedriverlocation = "C:\\Users\\savita.badhe\\python_workspace\\Python_selenium_Ass\\drivers\\chromedriver.exe"
        # driver = webdriver.Chrome(chromedriverlocation)
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.click_signIn()
        lp.login("username", "password")
        lp.click_project_link()
        lp.click_nit_training_project()
        lp.click_on_log_time()
        lp.create_task("8", "Done python assignment", "Task")
        driver.close()
