from ..decorator import hook, parameter
from ..plugin.conroyplugin import ConroyPlugin


class AutoHotkey(ConroyPlugin):

    @hook('p')
    def pastebin(self):
        return 'Share your code - https://p.ahkscript.org'

    @hook('rtfm')
    def rtfm(self):
        return 'Documentation - https://autohotkey.com/docs'

    @hook('docs')
    @parameter('query', greedy=True)
    def docs(self, query):
        query = 'site:autohotkey.com/docs {}'.format(query)

        reply = self.hooks['Google.g'](query)
        if not reply:
            reply = self.hooks['DuckDuckGo.ddg'](query)

        return reply
