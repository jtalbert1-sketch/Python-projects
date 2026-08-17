# Phase 2 Day 4 - Filtering CSV rows by condition
# Jake Talbert
# July 15th, 2026
import csv
with open("clients.csv", "r") as infile:
    reader = csv.reader(infile)
    with open("high_budget_clients.csv", "w") as outfile:
        writer = csv.writer(outfile)
        next(reader)
        for row in reader:
            if int(row[2]) >= 500:
                writer.writerow(row)
