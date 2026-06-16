# Week 4 Tuesday - Functions Practice 2
# Jake Talbert

def calculate_area(length, width):
    return length * width

# Test the function
def print_room_area():
    room_area = calculate_area(10, 5)
    print(f"The area of the room is {room_area} square units.")
print_room_area()

def calculate_total_with_tax(price, tax_rate):
    return price + (price * tax_rate)
final_price = calculate_total_with_tax(100, 0.08)
print(f"The total cost with tax is ${final_price:.2f}.")

def generate_quote(hours, rate, tax_rate):
    subtotal = hours * rate
    total = calculate_total_with_tax(subtotal, tax_rate)
    return total
client_quote = generate_quote(10, 75, 0.08)
print(f"The client quote is ${client_quote:.2f}.")