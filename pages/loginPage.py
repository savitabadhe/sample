import xlrd
from selenium.webdriver.support.select import Select

from base.basepage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.signIn_link = "//a[@class='login']"
        self.username = "username"
        self.password = "password"
        self.login_button = "login-submit"
        self.project_link = "//div[@id='top-menu']/ul//a[@href='/projects']"
        self.nit_training_project = "//a[contains(text(),'NIT Training')]"
        self.plus_icon = "//a[@onclick]"
        self.log_time = "//a[@class='new-timelog']"
        self.hours_textbox = "time_entry_hours"
        self.comments_textbox = "time_entry_comments"
        self.activity_entry = "time_entry_activity_id"
        self.create_button = "//form[@id='new_time_entry']/input[@name='commit']"

    def click_signIn(self):
        self.driver.find_element_by_xpath(self.signIn_link).click()

    def login(self, username, password):
        self.driver.find_element_by_id(self.username).clear()
        self.driver.find_element_by_id(self.username).send_keys(username)
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(password)
        self.driver.find_element_by_id(self.login_button).click()

    def click_project_link(self):
        self.driver.find_element_by_xpath(self.project_link).click()

    def click_nit_training_project(self):
        self.driver.find_element_by_xpath(self.nit_training_project).click()

    def click_on_log_time(self):
        self.driver.find_element_by_xpath(self.plus_icon).click()
        self.driver.find_element_by_xpath(self.log_time).click()

    def create_task(self, hours_textbox, comments_textbox, text):
        self.driver.find_element_by_id(self.hours_textbox).send_keys(hours_textbox)
        self.driver.find_element_by_id(self.comments_textbox).send_keys(comments_textbox)
        self.driver.find_element_by_id(self.activity_entry).click()
        element = self.driver.find_element_by_id(self.activity_entry)
        sel = Select(element)
        sel.select_by_visible_text(text)
        # self.driver.find_element_by_xpath(self.create_button).click()
