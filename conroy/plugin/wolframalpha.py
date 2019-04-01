import requests

from conroy.decorator import hook, parameter
from conroy.plugin.conroyplugin import ConroyPlugin


class WolframAlpha(ConroyPlugin):
    def __init__(self, appid):
        super().__init__()

        self.appid = appid

    @hook('wa')
    @parameter('input')
    def query(self, input):
        try:
            r = requests.get('https://api.wolframalpha.com/v1/result', {'appid': self.appid, 'i': input})
            print(r, r.text)
            if r.status_code == 200:
                return r.text
        except requests.RequestException:
            return None
