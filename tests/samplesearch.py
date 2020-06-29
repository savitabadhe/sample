import unittest

import pytest
from selenium import webdriver
from pages.serachPage import SearchPage

@pytest.mark.usefixtures("oneTimeSetUp1", "setUp")
class SearchTests(unittest.TestCase):

    def test_search(self):

        self.sp = SearchPage(self.driver)
        text_to_search = self.sp.read_excel()
        self.sp.enter_text(text_to_search)

