import csv


def createCsvFromDict(file_name, dict):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(list(dict.keys()))
        writer.writerow(list(dict.values()))
