# Week 4 Thursday - Functions Deep Dive
# Jake Talbert
def greet_client(name):
    message = f"Hello {name}, Welcome to my freelance services!"
    return message
result = greet_client("Sarah")
print(result)
print(greet_client("Marcus"))
print(greet_client("Lisa"))
def calculate_project_fee(hours, rate):
    total = hours * rate
    return total
fee = calculate_project_fee(10, 75)
print(f"Project fee: ${fee}")
def calculate_project_fee(hours, rate, revision_rounds):
    base_fee = hours * rate
    revision_fee = revision_rounds * 50
    total = base_fee + revision_fee
    return total
fee = calculate_project_fee(10, 75, 3)
print(f"Project fee: ${fee}")
print(calculate_project_fee(10, 75, 3))
def apply_discount(fee, discount_percent):
    discount = fee * (discount_percent / 100)
    discounted_fee = fee - discount
    return discounted_fee
def get_final_quote(hours, rate, revision_rounds, discount_percent):
    base_fee = calculate_project_fee(hours, rate, revision_rounds)
    final_fee = apply_discount(base_fee, discount_percent)
    return final_fee
quote = get_final_quote(10, 75, 3, 10)
print(f"Final quote after discount: ${quote:.2f}")