from models.Unit import Unit
from uuid import uuid1

class Lightswitch(Unit):
    
    def __init__(self, name: str, status = False) -> None:
        super().__init__(name, status)
        self.unit_id = uuid1().hex
    