from models.Unit import Unit
from uuid import uuid1

class Heating(Unit):
    
    def __init__(self, name: str, temperature = 20.5, status = False) -> None:
        super().__init__(name, status)
        self.unit_id = uuid1().hex
        self.temperature = temperature
    
    def setTemperature(self, temp: float) -> None:
        """Setter ny temperatur til enheten

        Args:
            temp (float): Den nye temperaturen
        """
        self.temperature = temp