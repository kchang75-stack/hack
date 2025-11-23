from abc import ABC

class ParserBase(ABC):
    def __init__ (self, session=None):
        self.session = session

    def get_name(html):
        raise NotImplementedError


    
    def get_price(html):
        raise NotImplementedError