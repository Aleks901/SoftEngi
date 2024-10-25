from models import *


# Her testes de forskjellige metodene fra klassene våre

lysbryter = Unit("Bryter1", True)
varmeovn = Heating("Varm1", True, 10)
lightswitch = Lightswitch("lysbryter", False)
alarm = Alarm("Test Alarm")

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

def test_unit_wrong_unit():
    """
    Sjekker om enheten oppdages som feil type
    """
    assert isinstance(lightswitch, Heating) == False

def test_alarm():
    """Sjekker egentlig bare om alarm loopen runner,
    breaker og så returnerer status True som vil si at enheten
    er skrudd på.
    Ettersom testen må baseres på tid så må den justeres for hver test
    dermed er den kommentert ut når den ikke brukes."""
    
    # assert alarm.run(12, 45, 50) == True