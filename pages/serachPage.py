import xlrd
from selenium.webdriver.common.keys import Keys


class SearchPage():

    def __init__(self, driver):
        self.driver = driver
        self.search_field = "//input[@name='q']"
        self.google_search_button = "//input[@data-ved='0ahUKEwiFm5Ps3Y3qAhV7yDgGHXjKC1oQ4dUDCAc']"

    def read_excel(self):
        file_path = "C:\\Users\\savita.badhe\\python_workspace\\Python_selenium_Ass\\tests\\sample.xls"
        book = xlrd.open_workbook(file_path)
        print("The number of worksheets is", book.nsheets)
        print("Worksheet name(s):", book.sheet_names())
        sh = book.sheet_by_index(0)
        text = sh.cell_value(0, 0)
        print(text)
        return text

    def enter_text(self, text):
        self.driver.find_element_by_xpath(self.search_field).click()
        self.driver.find_element_by_xpath(self.search_field).send_keys(text)
        self.driver.find_element_by_xpath(self.search_field).send_keys(Keys.RETURN)
