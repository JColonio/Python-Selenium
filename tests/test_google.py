import time
import pytest

from selenium.webdriver.common.keys import Keys
from tests.base import BaseTest


class TestGoogle(BaseTest):

    @pytest.mark.usefixtures("driver_init")
    def test_google_search(self):
        self.driver.get('http://www.google.com/')
        element = self.driver.find_element_by_id('lst-ib')
        element.click()
        element.send_keys('saucelabs')
        element.send_keys(Keys.RETURN)
        time.sleep(10)