import requests

from conroy.decorator import hook, parameter
from conroy.plugin.conroyplugin import ConroyPlugin
from conroy.utils import truncate_ellipses, truncate_newline


class Wikipedia(ConroyPlugin):

    @hook('wiki')
    @parameter('query')
    def search(self, query):
        results = requests.get('https://en.wikipedia.org/w/api.php?action=opensearch&search={}'.format(query)).json()
        _, suggestions, summaries, links = results

        if not (suggestions and summaries and links):
            return 'No results found.'

        return ['{} - {}'.format(truncate_newline(suggestions[0]), links[0]), truncate_ellipses(truncate_newline(summaries[0]), 384)]
