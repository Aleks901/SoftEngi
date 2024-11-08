import csv

def read_from_server(filename:str):
    with open(filename, "r") as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)