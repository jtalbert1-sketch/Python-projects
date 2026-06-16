service_tier = int(input("What is your budget?"))
if service_tier >= 5000:
    print("This client is a premium lead- prioritize them")
elif service_tier >= 1500:
    print("This client is a great opportunity- follow up with them")
elif service_tier >= 500:
    print("This client is a solid mid-tier project")
else:
    print("This client is a small job - good for quick wins.")

