import requests

from conroy.decorator import hook, parameter
from conroy.plugin.conroyplugin import ConroyPlugin


class Wikipedia(ConroyPlugin):

    @hook('wiki')
    @parameter('query')
    def search(self, query):
        results = requests.get('https://en.wikipedia.org/w/api.php?action=opensearch&search={}'.format(query)).json()
        _, suggestions, summaries, links = results

        if not (suggestions and summaries and links):
            return 'No results found.'

        return ['{} - {}'.format(suggestions[0], links[0]), summaries[0]]
