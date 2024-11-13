from models.Alarm import Alarm
from models.Blinds import Blinds
from models.Heating import Heating
from models.Lightswitch import Lightswitch
from models.Unit import Unit
from models.Bluetooth import BluetoothDevice
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

def test_pair_device():
    device = BluetoothDevice(name="TestDevice")
    result = device.pair("00:11:22:33:44:55")
    assert result == "TestDevice paired with device 00:11:22:33:44:55."
    assert device.is_paired is True

def test_pair_device_already_paired():
    device = BluetoothDevice(name="TestDevice")
    device.pair("00:11:22:33:44:55")
    result = device.pair("00:11:22:33:44:55")
    assert result == "TestDevice is already paired with 00:11:22:33:44:55."

def test_unpair_device():
    device = BluetoothDevice(name="TestDevice")
    device.pair("00:11:22:33:44:55")
    result = device.unpair()
    assert result == "TestDevice unpaired from device 00:11:22:33:44:55."
    assert device.is_paired is False

def test_unpair_device_not_paired():
    device = BluetoothDevice(name="TestDevice")
    result = device.unpair()
    assert result == "TestDevice is not paired with any device."

def test_connect_device():
    device = BluetoothDevice(name="TestDevice")
    device.pair("00:11:22:33:44:55")
    result = device.connect()
    assert result == "TestDevice connected to 00:11:22:33:44:55."
    assert device.is_connected is True

def test_connect_device_not_paired():
    device = BluetoothDevice(name="TestDevice")
    result = device.connect()
    assert result == "TestDevice is not paired with any device."

def test_connect_device_already_connected():
    device = BluetoothDevice(name="TestDevice")
    device.pair("00:11:22:33:44:55")
    device.connect()
    result = device.connect()
    assert result == "TestDevice is already connected to 00:11:22:33:44:55."

def test_disconnect_device():
    device = BluetoothDevice(name="TestDevice")
    device.pair("00:11:22:33:44:55")
    device.connect()
    result = device.disconnect()
    assert result == "TestDevice disconnected from 00:11:22:33:44:55."
    assert device.is_connected is False

def test_disconnect_device_not_connected():
    device = BluetoothDevice(name="TestDevice")
    result = device.disconnect()
    assert result == "TestDevice is not connected to any device."

def test_send_data_connected():
    device = BluetoothDevice(name="TestDevice")
    device.pair("00:11:22:33:44:55")
    device.connect()
    result = device.send_data("Hello World")
    assert result == "Sending data to 00:11:22:33:44:55: Hello World"

def test_send_data_not_connected():
    device = BluetoothDevice(name="TestDevice")
    result = device.send_data("Hello World")
    assert result == "TestDevice is not connected. Cannot send data."

def test_receive_data_connected():
    device = BluetoothDevice(name="TestDevice")
    device.pair("00:11:22:33:44:55")
    device.connect()
    result = device.receive_data()
    assert result == "Data received from 00:11:22:33:44:55: Sample received data"

def test_receive_data_not_connected():
    device = BluetoothDevice(name="TestDevice")
    result = device.receive_data()
    assert result == "TestDevice is not connected. Cannot receive data."

def test_get_battery_level():
    device = BluetoothDevice(name="TestDevice")
    result = device.get_battery_level()
    assert result == "TestDevice battery level: 100%"

def test_rename_device():
    device = BluetoothDevice(name="TestDevice")
    result = device.rename_device("NewDevice")
    assert result == "Device renamed from 'TestDevice' to 'NewDevice'"
    assert device.name == "NewDevice"




