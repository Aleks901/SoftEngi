from unit import Unit


class Heating(Unit):
    
    def __init__(self, unit_id: int, name: str, status: bool, temperature: float) -> None:
        super().__init__(unit_id, name, status)
        self.temperature = temperature
    
    def setTemperature(self, temp: float) -> None:
        """Setter ny temperatur til enheten

        Args:
            temp (float): Den nye temperaturen
        """
        self.temperature = temp