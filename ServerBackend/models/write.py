import csv


def write_to_server(filename:str, data:dict):
    with open(filename, "w", newline='') as csvfile:
        kolonne_navn = ['device_id', 
                        'device_name', 
                        'device_type', 
                        'status',
                        'temperature']
        writer = csv.DictWriter(csvfile, fieldnames=kolonne_navn)
        writer.writeheader()
        writer.writerows(data)