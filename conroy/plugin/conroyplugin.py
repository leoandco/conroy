from abc import ABC


class ConroyPlugin(ABC):
    def __init__(self):
        self.resource = None
        self.hooks = None

    def load(self):
        pass

    def unload(self):
        pass
