# Freelance Rate Calculator
# Calculates the hourly rate needed to hit a monthly income goal
print("=== Freelance Rate Calculator ===")
print()
name = input("What's your name? ")
print(f"Hello {name}! Let's calculate your freelance hourly rate.")
monthly_goal = int(input("what is your monthly income goal? $"))
hours_per_week = int(input("How many hours per week can you work? "))
weeks_per_month = int(input("how many weeks per month will you work?"))
rate = monthly_goal / (hours_per_week * weeks_per_month)
print()
print(f"To earn ${monthly_goal}/month, you need to charge ${rate:.2f}/hour")
annual_income = monthly_goal * 12
print(f"That would be an annual income of ${annual_income:.2f}")