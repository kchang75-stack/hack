from abc import ABC

class ParserBase(ABC):
    def __init__ (self, session=None):
        self.session = session

    def get_name(self, html):
        raise NotImplementedError

    
    def get_price(self, html):
        raise NotImplementedError