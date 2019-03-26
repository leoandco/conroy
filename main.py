import logging
import sys

import conroy
from conroy.plugin import Google, Selenium, DuckDuckGo, AutoHotkey, Wikipedia

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

c = conroy.Conroy()
c.register_plugin(Selenium(), Google(), DuckDuckGo(), AutoHotkey(), Wikipedia())
c.recv_msg('g ahk')
