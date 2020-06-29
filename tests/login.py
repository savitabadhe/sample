import time
import unittest

import pytest
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.loginPage import LoginPage
from pages.serachPage import SearchPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    def test_Login(self):

        self.lp = LoginPage(self.driver)
        self.lp.click_signIn()
        self.lp.login("savita.badhe", "Sb@#$2020")
        self.lp.click_project_link()
        self.lp.click_nit_training_project()
        self.lp.click_on_log_time()
        self.lp.create_task("8", "Done python assignment", "Task")

