from unit import Unit
from heating import Heating
from lightswitch import Lightswitch

# Her testes de forskjellige metodene fra klassene våre

lysbryter = Unit(1, "Bryter1", True)
varmeovn = Heating(2, "Varm1", True, 10)
lightswitch = Lightswitch(3, "lysbryter", False)

def test_name():
    lysbryter.setName("Aleks")
    assert lysbryter.name == "Aleks"

def test_status():
    assert lysbryter.setStatus() == False
    
def test_id():
    lysbryter.setUnit_id(4)
    assert lysbryter.unit_id == 4

def test_temp():
    varmeovn.setTemperature(20.5)
    assert varmeovn.temperature == 20.5

def test_light():
    assert lightswitch.setStatus() == True