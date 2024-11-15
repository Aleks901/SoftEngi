from models.Unit import Unit
from uuid import uuid1

class Heating(Unit):
    
    def __init__(self, name: str, temperature, status = False) -> None:
        super().__init__(name, status)
        self.unit_id = uuid1().hex
        self.temperature = temperature
    
    def setTemperature(self, temp: float):
        """Setter ny temperatur til enheten

        Args:
            temp (Any): Den nye temperaturen
        """
        self.temperature = temp
        
    def getTemperature(self):
        return self.temperature