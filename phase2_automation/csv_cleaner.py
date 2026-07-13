import csv
with open("clients.csv", "r") as infile:
    reader = csv.reader(infile)
    next(reader)
    with open("clean_clients.csv", "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["name", "email"])
        for row in reader:
            writer.writerow([row[0], row[1]])