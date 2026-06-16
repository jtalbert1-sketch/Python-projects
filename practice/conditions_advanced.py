# AND - both conditions must be true
age = int(input("How old are you? "))
income = int(input("What is your monthly income? "))
if age >= 18 and income >= 1000:
    print("You qualify for the service.")
else:
    print("You do not qualify ")
    print()
    
    # OR - only one condition must be true
    experience = int(input("How many years of experience do you have? "))
    portfolio = int(input("How many projects are in your portfolio? "))
    if experience >= 2 or portfolio >= 5:
        print("You are ready to apply for freelance work!")
    else:
        print("Keep building - you're not quite ready yet.")