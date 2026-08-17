import csv
with open("clients.csv", "r") as infile:
    reader = csv.reader(infile)
    next(reader)
    with open("clean_clients_v2.csv", "w") as outfile:
        writer = csv.writer(outfile)
        for row in reader:
             writer.writerow([row[0], row[1]])
    

    