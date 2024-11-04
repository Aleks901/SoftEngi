from homehub.models.Alarm import Alarm
from homehub.models.Blinds import Blinds
from homehub.models.Heating import Heating
from homehub.models.Lightswitch import Lightswitch
from homehub.models.Unit import Unit
from models import *
from tkinter import Tk
from tkinter import *
from models.Unit import Unit
from uuid import uuid1
from models import DraggableUnit
from models.Doorbell import Doorbell


lysbryter = Unit("Bryter1", True)
varmeovn = Heating("Varm1", True, 10)
lightswitch = Lightswitch("lysbryter", False)
alarm = Alarm("Test Alarm")
blinds = Blinds("Test_blinds")


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
    assert isinstance(lightswitch, Heating) == False


def test_blinds_super_setter():
    blinds.setName("Test_correct")
    assert blinds.getName() == "Test_correct"

def test_alarm():
    pass

def test_create_draggable_button():
    root = Tk()
    button = DraggableUnit.create_draggable_button(root, "Lysbryter", 100, 100)
    assert button.winfo_x() == 100 and button.winfo_y() == 100
    assert button.cget("text") == "Lysbryter"
    root.destroy()

def test_doorbell_creation():
    doorbell = Doorbell(name="Front Door")
    assert doorbell.name == "Front Door"
    assert isinstance(doorbell.unit_id, str)
    assert doorbell.unit_id != ""

def test_doorbell_notify_user():
    doorbell = Doorbell(name="Front Door")
    assert callable(doorbell.notifyUser)





