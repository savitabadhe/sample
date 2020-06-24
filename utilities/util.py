"""
@package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import time
import traceback
import random, string

import xlrd

import utilities.custom_logger as cl
import logging


class Util(object):
    log = cl.customLogger(logging.INFO)

    def read_excel(self):
        file_path = "C:\\Users\\savita.badhe\\python_workspace\\Python_selenium_Ass\\tests\\sample.xls"
        book = xlrd.open_workbook(file_path)
        print("The number of worksheets is", book.nsheets)
        print("Worksheet name(s):", book.sheet_names())
        sh = book.sheet_by_index(0)
        text = sh.cell_value(0, 0)
        print(text)
        return text

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify text match

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False
