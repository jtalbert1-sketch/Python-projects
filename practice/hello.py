print("Hello, world!")
print("My name is Jake")
print("I am learning python")
name = "Jake"
goal = "Earn $1000/month freelancing"
print(f"My name is {name} and my goal is to {goal}")
hours_per_day = 0.75
days_per_week = 6
weeks = 16
total_hours = hours_per_day * days_per_week * weeks
print(f"Total hours in my learning plan: {total_hours}")
weeks_to_goal = 16
monthly_goal = 1000
print(f"In {weeks_to_goal} weeks I'll be earning ${monthly_goal}/month freelancing.")
monthly_goal = 1000
hours_per_month = 40
rate_per_hour = monthly_goal / hours_per_month 
print(f"To hit my goal, I need to charge ${rate_per_hour}/hour")
city = "Costa Mesa"
language = "Python"
weeks = 16
print(f"I'm learning {language} in {city} and will be freelancing in {weeks} weeks.")
savings = 0
print(f"Start savings: ${savings}")
savings = savings + 500
print(f"after client: ${savings}")
savings = savings +500
print(f"after second client: ${savings}")
user_name = input("what's your name? ")
user_city = input("what city do you live in? ")
print(f"Hello {user_name} from {user_city}!")
hours = int(input("How many hours a day do you practice? "))
days = int(input("How many days a week? "))
weeks = int(input("how many weeks? "))
total = hours * days * weeks
print(f"Total practice hours: {total}")
monthly_goal = int(input("what is your monthly income goal? "))
hours = int(input("How many hours per week can you work? "))
weeks_per_month = int(input("how many weeks per month will you work? "))
rate = monthly_goal / (hours * weeks_per_month)
print(f"To hit your goal, you need to charge ${rate:.2f}/hour")