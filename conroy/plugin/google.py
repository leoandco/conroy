import logging

from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from ..decorator import hook, parameter
from ..plugin.conroyplugin import ConroyPlugin
from ..utils import truncate_ellipses


class Google(ConroyPlugin):

    @hook('g')
    @parameter('query')
    def search(self, query):
        try:
            self.resource['Selenium.driver'].get('https://google.com/search?q={}'.format(query))

            result = self.resource['Selenium.driver'].find_element_by_css_selector('#rso > div:nth-child(1) > div > div')
            title = result.find_element_by_css_selector('div > div > div.r > a').text
            url = result.find_element_by_css_selector('div > div > div.r > a').get_attribute('href')
            description = truncate_ellipses(result.find_element_by_css_selector('div > div.s > div > span').text, 384)

            return ['{} - {}'.format(title, url), description]
        except (NoSuchElementException, InvalidSelectorException) as e:
            logging.error(e)

        return None
