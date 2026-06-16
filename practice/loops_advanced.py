# Counting by 2's
for i in range(10, 0, -1):
    print(i)
print()
teams = ["Team A", "Team B"]
tasks = ["Research", "Design", "Build"]
for team in teams:
    for task in tasks:
        print(f"{team} is working on: {task}")
clients = ["Jake", "Blake"]
services = [("Web Scraping", 500), ("Automation Bot", 750), ("Data Cleanup", 300)]
for client in clients:
    print(f"Client: {client}")
    for service, price in services:
        print(f"  Service: {service} - Price: ${price}")
    print()
