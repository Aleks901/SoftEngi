from models.Unit import Unit

class Blinds(Unit):
    
    
    def __init__(self, name: str, status = False):
        super().__init__(name, status)
        self.name = name
        self.status = status
        
    def get_name(self):
        """Henter navnet på enheten

        Returns:
            _type_: Navnet på enheten
        """
        return self.name
    
    def set_name(self, name):
        """Setter navnet på enheten

        Args:
            name (_type_): Navnet på enheten
        """
        self.name == name
        
    def open_blinds(self):
        """Åpner gardinen
        """
        self.status == True
    
    def close_blinds(self):
        """Stenger gardinen
        """
        self.status == False
    
