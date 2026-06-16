# Week 4 Monday/Tuesday - Functions Fundamentals
# Jake Talbert
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Jake")
say_hello("Alice")
say_hello("Bob")
def greet_print(name):
    print(f"Hi {name}")
def greet_return(name):
    return f"Hi {name}"

#Try to capture both
captured_print = greet_print("Jake")
captured_return = greet_return("Jake")

print("Captured from print version:", captured_print)
print("Captured from return version:", captured_return)