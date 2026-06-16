# FOR loops - repeat a specific number of times
for i in range(5):
    print(f"Rep {i+1} of 5")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day in days:
    print(f"{day}: 45 minutes of Python practice")
# WHILE loops - repeat until a condition becomes false
count = 1
while count <= 5:
    print(f"Count is {count}")
    count = count +1
# WHILE loop with user input
answer = ""
while answer != "quit":
    answer = input("Type something (or 'quit' to stop): ")
    print(f"You typed: {answer}")
print("Thanks for playing!")
