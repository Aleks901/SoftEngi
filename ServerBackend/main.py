from models.write import write_to_server
from models.read import read_from_server

# Dummy data
data = [
    {'device_id': 1, 'device_name': 'Varmeovn Nede', 'device_type': 'Heating', 'status': 0, 'temperature': 0},
    {'device_id': 2, 'device_name': 'Lysbryter Nede', 'device_type': 'Lightswitch', 'status': 1, 'temperature': 0},
    {'device_id': 3, 'device_name': 'Varmeovn Oppe', 'device_type': 'Heating', 'status': 1, 'temperature': 22},
    {'device_id': 4, 'device_name': 'Lysbryter Oppe', 'device_type': 'Lightswitch', 'status': 0, 'temperature': 0},
    {'device_id': 5, 'device_name': 'Varmeovn2 Nede', 'device_type': 'Heating', 'status': 1, 'temperature': 20} 
    ]

read_from_server("Test.csv")