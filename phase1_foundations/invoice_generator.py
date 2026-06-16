# Invoice Generator
# Builds a custom invoice based on client selections

print("=== Freelance Invoice Generator ===")
print()
client_name = input("Client_name: ")
services = [
    ("Web Scraping Setup", 500),
    ("Automation Bot", 750),
    ("Data Cleanup", 300),
    ("Report Dashboard", 600),
    ("API Integration", 850)
]
selected = []
total = 0
print("Available Services:")
print()
for service, price in services:
    answer = input(f" Include {service} (${price})? (yes/no): ")
    if answer.lower() == "yes":
        selected.append(service)
        total += price
print()
print("=" * 30)
print(f" Invoice for: {client_name}")
print("=" * 30)
for item in selected:
    print(f" - {item}")
print()
print(f" Total Due: ${total}")
print("=" * 30)