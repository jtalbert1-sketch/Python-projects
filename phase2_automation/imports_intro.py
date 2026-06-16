# Week 5 - Imports & Modules
# Jake Talbert
import random
number = random.randint(1, 100)
print(f"Your random number is: {number}")
services = ["Web Scraping", "Data Entry", "Automation", "API Integration"]
random_service = random.choice(services)
print(f"Your random service is: {random_service}")
import datetime
now = datetime.datetime.now()
print(f"This script ran at: {now}")
with open("activity_log.txt", "a") as log:
    log.write(f"Script ran at: {now}\n")
print("Logged to activity_log.txt")