import unittest
from selenium import webdriver
from pages.serachPage import SearchPage


class SearchTests(unittest.TestCase):

    def test_search(self):
        baseURL = "https://www.google.com/"
        # chromedriverlocation = "C:\\Users\\savita.badhe\\python_workspace\\Python_selenium_Ass\\drivers\\chromedriver.exe"
        # driver = webdriver.Chrome(chromedriverlocation)
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        sp = SearchPage(driver)
        text_to_search = sp.read_excel()
        sp.enter_text(text_to_search)
        driver.close()
