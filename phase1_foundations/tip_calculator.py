bill_total = float(input("What was the bill total? $"))
tip_percentage = float(input("What percentage tip would you like to leave? "))
individuals = int(input("How many people are splitting the bill? "))
tip_amount = bill_total * (tip_percentage / 100)
print(f"Tip amount: ${tip_amount:.2f}")
total = bill_total + tip_amount
print(f"Total bill with tip: ${total:.2f}")
each_person_pays = (bill_total + tip_amount) / individuals
print(f"Each person should pay: ${each_person_pays:.2f}")
