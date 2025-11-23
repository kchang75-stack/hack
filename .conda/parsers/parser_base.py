from abc import ABC

class ParserBase(ABC):
    def __init__ (self, session=None):
        self.session = session
    
    def get_list(self, driver, query):
        raise NotImplementedError