budget = int(input("What is your budget?"))
if budget >= 5000:
    print("This client is a premium lead- prioritize them")
elif budget >= 1500:
    print("This client is a great opportunity- follow up with them")
elif budget >= 500:
    print("This client is a solid mid-tier project")
else:
    print("This client is a small job - good for quick wins.")

