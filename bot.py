from abc import ABC, abstractmethod

# Abstract class BOT
# Used as a template for BSTBUY_BOT
class BOT(ABC) : 
    @abstractmethod
    def startup(self) : 
        pass
    
    @abstractmethod
    def check_in_stock(self) :
        pass
    
    @abstractmethod
    def makeIATCLink(self) : 
        pass
    
    @abstractmethod
    def close(self) : 
        pass
    