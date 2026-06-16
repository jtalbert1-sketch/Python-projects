# FOR loops- repeat a specific number of times
savings_goal = 2000
month = 1
while month <= 12:
    monthly_savings = float(input(f"How much did you save in month {month}? "))
    savings_goal -= monthly_savings
    if savings_goal <= 0:
        print(f" 🎉 ! You've reached your savings goal in {month} months!")
        break
    month += 1