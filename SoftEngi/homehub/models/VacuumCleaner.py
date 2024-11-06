from models.Unit import Unit

class VacuumCleaner(Unit):

    def __init__(self, name: str, status=False) -> None:
        super().__init__(name, status)


"""
Støvsugeren kjører til den ikke kan kjøre lenger også snur den
"""
def runRoute():
    canMove = False
    Turn = ["N","E","S","W"]

    if (canMove == False):
        i = (i + 1) % len(Turn)
        print("Turning to:", Turn[i])
            

