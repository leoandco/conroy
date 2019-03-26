import logging

from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from ..decorator import hook, parameter
from ..plugin.conroyplugin import ConroyPlugin


class DuckDuckGo(ConroyPlugin):

    @hook('ddg')
    @parameter('query')
    def search(self, query):
        try:
            self.resource['Selenium.driver'].get('https://duckduckgo.com/?q={}'.format(query))

            result = self.resource['Selenium.driver'].find_element_by_css_selector('#r1-0')
            title = result.find_element_by_css_selector('div > h2 > a.result__a').text
            url = result.find_element_by_css_selector('div > h2 > a.result__a').get_attribute('href')
            description = result.find_element_by_css_selector('div > div.result__snippet.js-result-snippet').text

            return ['{} - {}'.format(title, url), description]
        except (NoSuchElementException, InvalidSelectorException) as e:
            logging.error(e)
