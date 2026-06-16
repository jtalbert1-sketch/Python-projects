# Functions - reusable blocks of code
def greet():
    print("Hello! Welcome to my freelance services.")
    print("Let's find the right solution for you.")
greet()
greet()
greet()
def greet_client(name):
    print(f"Hello, {name}! Welcome to my freelance services.")
    print("Let's find the right solution for you.")
greet_client("Jake")
greet_client("Blake")
greet_client("Susan")
def calculate_rate(hours, rate):
    total = hours * rate
    return total
earnings = calculate_rate(20, 65)
print(f"Total earnings: ${earnings} this week!")

print(f"Part time earnings: ${calculate_rate(10, 65)}")
print(f"Full time earnings: ${calculate_rate(40, 65)}")
def qualify_client(budget, timeline):
    if budget >= 1000 and timeline >= 2:
        return "✅ Great fit- send a proposal!"
    elif budget >= 500 and timeline >= 1:
        return "⚠️ Potential fit- follow up for more details."
    else:
        return "❌ Not a good fit- move on to the next client."

print(qualify_client(1500, 3))
print(qualify_client(750, 2))
print(qualify_client(250, 1))
def calculate_project_total(services):
    total = 0
    for service, price in services:
        total += price
    return total
services = [("Web Scraping", 500), ("Automation Bot", 750), ("Data Cleanup", 300)]
project_total = calculate_project_total(services)
print(f"Total project cost: ${project_total}")
def analyze_client(name, budget, timeline):
    greeting = greet_client(name)
    qualification = qualify_client(budget, timeline)
    earnings = calculate_rate(timeline, budget / timeline)
    print(f"\n--- Client Report: {name} ---")
    print(f"Budget: ${budget}, Timeline: {timeline} days")
    print(f"Fit: {qualification}")
    print(f"Expected Earnings: ${earnings}")
    print("--- End Report ---")
    print()
analyze_client("Jake", 1500, 3)
analyze_client("Blake", 400, 1)
analyze_client("Susan", 450, 2)