import os

import irc.bot
import irc.strings

from conroy import Conroy
from conroy.plugin import Selenium, Google, DuckDuckGo, AutoHotkey, Wikipedia, UrbanDictionary, WolframAlpha


class Bot(irc.bot.SingleServerIRCBot):
    def __init__(self):
        irc.bot.SingleServerIRCBot.__init__(self, [('znc', 6667, 'conroy')], 'conroy', 'conroy', username='conroy')

        self.conroy = Conroy('!')
        self.conroy.register_plugin(
            Selenium(),
            Google(),
            DuckDuckGo(),
            AutoHotkey(),
            UrbanDictionary(),
            Wikipedia(),
            WolframAlpha(os.environ.get('CONROY_WOLFRAMALPHA_APPID', 'DEMO'))
        )

    def on_welcome(self, c, e):
        self.connection.join('#conroy')

    def on_pubmsg(self, c, e):
        reply = self.conroy.recv_msg(e.arguments[0])

        if reply:
            reply = [reply] if type(reply) is not list else reply
            for line in reply:
                self.connection.privmsg(e.target, line)


if __name__ == '__main__':
    bot = Bot()
    bot.start()
