from abc import ABC

class ParserBase(ABC):
    def __init__ (self, session=None):
        self.session = session

    def get_name(driver):
        raise NotImplementedError

    
    def get_price(driver):
        raise NotImplementedError