import unittest

from driver.driver import *


class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
