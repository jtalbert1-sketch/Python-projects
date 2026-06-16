projects = ["rate_calculator.py" , "tip_calculator.py" , "client_qualifier.py" , "freelance_screener.py" , "savings_calculator.py"]
for project in projects:
    print(f"Project: {project}")
print ()
goal = 1000
for week in range(1,5):
    earned = week * 250
    print(f"Week {week}: ${earned} earned - goal is ${goal}")
    if earned >= goal:
        print("🎉 Goal reached! Time to celebrate!")

print()
target = int(input("Enter a number to count down from: "))
while target > 0:
    print(f"{target}...")
    target -= 1
print("Blast off! 🚀")

print()
numbers = [4, 17, 3, 22, 8, 15, 11, 6]

for num in numbers:
    if num > 10:
        print(f"{num} is greater than 10.")
    else:
        print(f"{num} is 10 or under")