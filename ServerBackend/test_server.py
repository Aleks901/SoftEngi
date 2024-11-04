from ServerBackend.models.read import read_from_server
from ServerBackend.models.write import write_to_server
import random
id = random.randrange(1, 5)
data = [
    {'device_id': id, 'device_name': 'Varmeovn Nede', 'device_type': 'Heating', 'status': 0, 'temperature': 0}
    ]


f = open("test_backend_text.csv", "r+")
f.truncate(0)
def test_write_to_server():
    write_to_server("test_backend_text.csv", data)
    assert read_from_server("test_backend_text.csv") == [['device_id', 'device_name', 'device_type', 'status', 'temperature'], [str(id), 'Varmeovn Nede', 'Heating', '0', '0']]
def test_read_from_server():
    assert read_from_server("test_backend_text.csv") == [['device_id', 'device_name', 'device_type', 'status', 'temperature'], [str(id), 'Varmeovn Nede', 'Heating', '0', '0']]


