from models.Unit import Unit

class Blinds(Unit):
    
    
    def __init__(self, name: str, status = False):
        super().__init__(name, status)
        self.name = name
        self.status = status
        
        
    def open_blinds(self):
        """Åpner gardinen
        """
        self.status = True
    
    def close_blinds(self):
        """Stenger gardinen
        """
        self.status = False
    
