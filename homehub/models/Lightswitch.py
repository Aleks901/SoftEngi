from models.Unit import Unit
from uuid import uuid1

from homehub.models import Alarm


class Lightswitch(Unit):
    
    def __init__(self, name: str, status = False) -> None:
        super().__init__(name, status)
        self.unit_id = uuid1().hex
    def dayNightCycle(self, hourM, minuteM, secondM, hourN, minuteN, secondN):
        morning = Alarm.Alarm("day", False)
        night = Alarm.Alarm("day", False)
        if morning.run(hourM, minuteM, secondM):
            print("good morning")
        if night.run(hourN, minuteN, secondN):
            print("good night")

    