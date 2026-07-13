import csv
with open("clients.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(f"{row[0]} - {row[1]} - budget: ${row[2]}")