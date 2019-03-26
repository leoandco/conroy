import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..decorator import resource
from ..plugin.conroyplugin import ConroyPlugin


class Selenium(ConroyPlugin):
    logger = logging.getLogger()

    def __init__(self):
        super().__init__()
        self._chrome_options = None
        self._driver = None

    def load(self):
        self._driver = webdriver.Chrome(options=self._chrome_options)

    def unload(self):
        self._driver.close()

    @resource()
    def driver(self):
        self._chrome_options = Options()
        self._chrome_options.add_argument('--disable-gpu')
        self._chrome_options.add_experimental_option('prefs', {
            'profile.managed_default_content_settings.javascript': 2,  # disable js
            'profile.default_content_setting_values.images': 2  # disable loading images
        })

        return self._driver
