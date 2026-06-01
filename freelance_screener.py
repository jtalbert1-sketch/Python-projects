# AND - Both conditions must be true
budget = int(input("What is your budget? "))
timeline = int(input("How many weeks do you have for this project? "))
if budget >= 1000 and timeline >= 2:
    print("✅ This project is a good fit for our services.")
elif budget >= 500 and timeline >= 1:
    print("⚠️ Ask for more details. ")
else:
    print("❌ Politely decline.")