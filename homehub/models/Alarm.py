from Unit import Unit
from uuid import uuid1
import datetime
import time
import winsound

class Alarm(Unit):

    def __init__(self, name: str, status=False) -> None:
        super().__init__(name, status)
        self.unit_id = uuid1().hex
        self.time= time

    def run(self, hour, minute, second):
        while True:
            set_alarm = f"{hour}:{minute}:{second}"
            time.sleep(1)
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            print(set_alarm)
            if current_time == set_alarm:
                print("Time to Wake up")
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                break

vekkeklokke = Alarm("vekkeklokke", True)
vekkeklokke.run(11, 49, "50")
