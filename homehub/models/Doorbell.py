from models.Unit import Unit
from uuid import uuid1


class Doorbell(Unit):

    def __init__(self, name: str, volume=5, status=False) -> None:
        """Tiltenkt f.eks Ring doorbell

        Args:
            name (str): Navnet til enheten
            status (bool): Kamera kontroll av eller på.
        """
        super().__init__(name, status)
        self.unit_id = uuid1().hex
        self.volume = volume

    def notifyUser(self) -> str:
        if self.status == True:
            return "Det er bevegelse ved døren din"
        
    def change_volume(self, new_volume):
        self.volume = new_volume
        
        
