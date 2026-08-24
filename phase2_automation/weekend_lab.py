import csv
with open("clients_v2.csv", "r") as infile:
    reader = csv.DictReader(infile)
    with open("high_budget_clients_v2.csv", "w") as outfile:
        writer = csv.writer(outfile)
        for row in reader:
            if int(row["budget"]) >= 650:
                writer.writerow([row["name"], row["email"]])

