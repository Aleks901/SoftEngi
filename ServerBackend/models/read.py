import csv

def read_from_server(filename:str):
    fileText = []
    with open(filename, "r") as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            fileText.append(lines)
    return fileText