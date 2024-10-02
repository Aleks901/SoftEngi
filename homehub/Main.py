from Unit import Unit
from Heating import Heating
from Lightswitch import Lightswitch

lysbryter = Unit("Bryter1", True)
varmeovn = Heating("Varm1", True, 10)
lightswitch = Lightswitch("lysbryter", False)

print(lysbryter.unit_id)
print(varmeovn.unit_id)


def create_unit(name: str, unit_type):
    if unit_type == "Varme":
        new_unit = Heating(name)
        return new_unit
    elif unit_type == "Lys":
        new_unit = Lightswitch(name)
        return new_unit
        
    
