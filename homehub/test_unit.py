from unit import Unit
from heating import Heating
from lightswitch import Lightswitch
from main import create_unit

# Her testes de forskjellige metodene fra klassene våre

lysbryter = Unit("Bryter1", True)
varmeovn = Heating("Varm1", True, 10)
lightswitch = Lightswitch("lysbryter", False)

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
    
def test_unit_exists():
    assert isinstance(lightswitch, Unit) == True
    
def test_create_unit():
    lys_test = create_unit("Lysbryternn", "Lys")
    assert isinstance(lys_test, Lightswitch) == True
    assert isinstance(lys_test, Heating) == False
    