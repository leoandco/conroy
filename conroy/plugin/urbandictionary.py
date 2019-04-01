import requests

from conroy.decorator import hook, parameter
from conroy.plugin.conroyplugin import ConroyPlugin
from conroy.utils import truncate_ellipses, truncate_newline


class UrbanDictionary(ConroyPlugin):

    @hook('ud')
    @parameter('term')
    def define(self, term):
        try:
            result = requests.get('https://api.urbandictionary.com/v0/define', {'term': term}).json().get('list')
            if result:
                definition = sorted(result, key=lambda d: d['thumbs_up'], reverse=True)[0]
                return '{} - {}'.format(truncate_ellipses(truncate_newline(definition['definition']), 384), definition['permalink'])
        except requests.RequestException:
            return None
