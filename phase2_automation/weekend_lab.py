import csv
with open("clients.csv", "r") as infile:
    reader = csv.DictReader(infile)
    with open("high_budget_clients.csv", "w") as outfile:
        writer = csv.writer(outfile)
        for row in reader:
            if int(row["budget"]) >= 650:
                writer.writerow([row["name"], row["email"]])

