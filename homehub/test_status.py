import pytest
from Unit import *

lysbryter = Unit(1, "Bryter1", True)


def test_name():
    lysbryter.setName("Aleks")
    assert lysbryter.name == "Aleks"

def test_status():
    assert lysbryter.setStatus() == False
    
def test_id():
    lysbryter.setUnit_id(4)
    assert lysbryter.unit_id == 4