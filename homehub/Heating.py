from unit import Unit


class Heating(Unit):
    
    def __init__(self, unit_id, name, status, temperature: float) -> None:
        super().__init__(unit_id, name, status)
        self.temperature = temperature
    
    def setTemperature(self, temp):
        self.temperature = temp