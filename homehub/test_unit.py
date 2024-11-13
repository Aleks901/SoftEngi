from models.Alarm import Alarm
from models.Blinds import Blinds
from models.Heating import Heating
from models.Lightswitch import Lightswitch
from models.Unit import Unit
from models import *
from tkinter import *
from models.Unit import Unit
from models.Doorbell import Doorbell


lysbryter = Unit("Bryter1", True)
varmeovn = Heating("Varm1", True, 10)
lightswitch = Lightswitch("lysbryter", False)
alarm = Alarm("Test Alarm")
blinds = Blinds("Test_blinds")


def test_set_name():
    lysbryter.setName("Aleks")
    assert lysbryter.name == "Aleks"


def test_setStatus_lysbryter_False():
    assert lysbryter.setStatus() == False


def test_set_unit_id():
    lysbryter.setUnit_id(4)
    assert lysbryter.unit_id == 4


def test_heater_can_set_temperature():
    varmeovn.setTemperature(20.5)
    assert varmeovn.temperature == 20.5


def test_setStatus_lightswitch_True():
    assert lightswitch.setStatus() == True


def test_unit_exists():
    assert isinstance(lightswitch, Unit) == True


def test_unit_wrong_unit():
    assert isinstance(lightswitch, Heating) == False


def test_blinds_super_setter():
    blinds.setName("Test_correct")
    assert blinds.getName() == "Test_correct"

def test_alarm():
    pass


def test_doorbell_creation():
    doorbell = Doorbell(name="Front Door")
    assert doorbell.name == "Front Door"
    assert isinstance(doorbell.unit_id, str)
    assert doorbell.unit_id != ""

def test_doorbell_notify_user():
    doorbell = Doorbell(name="Front Door")
    assert callable(doorbell.notifyUser)
    
def test_blinds_open():
    fun_blinds = Blinds("Gardina mi")
    fun_blinds.open_blinds()
    assert fun_blinds.status == True
    
def test_blinds_close():
    fun_blinds = Blinds("Gardina mi")
    fun_blinds.close_blinds()
    assert fun_blinds.status == False





