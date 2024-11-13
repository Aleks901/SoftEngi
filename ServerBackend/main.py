from models.write import write_to_server
from models.read import read_from_server

# Dummy data
data = [
    {'device_id': 1, 'device_name': 'Varmeovn Nede', 'device_type': 'Heating', 'status': 0, 'temperature': 0}    ]
write_to_server("test_backend_text.csv", data)
print(read_from_server("test_backend_text.csv"))