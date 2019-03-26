import logging

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from ..decorator import resource
from ..plugin.conroyplugin import ConroyPlugin


class Selenium(ConroyPlugin):
    logger = logging.getLogger()

    def __init__(self):
        super().__init__()
        self._driver = None

    def load(self):
        self._driver = webdriver.Remote(command_executor='http://selenium:4444/wd/hub', desired_capabilities={
            **DesiredCapabilities.CHROME,
            'javascriptEnabled': False
        })

    @resource()
    def driver(self):
        return self._driver
