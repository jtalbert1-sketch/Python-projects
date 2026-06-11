# Week 4 Thursday - Project Estimator
# Jake Talbert
def get_client_info():
    name = input("Client name: ")
    project_type = input("Project type (e.g. Web Scraping, Automation): ")
    return name, project_type
client_name, client_project = get_client_info()
def get_project_details():
    hours = float(input("Estimated hours: "))
    rate = float(input("Your hourly rate: $"))
    revisions = int(input("Revision rounds included: "))
    return hours, rate, revisions
project_hours, project_rate, project_revisions = get_project_details()
def calculate_quote(hours, rate, revisions):
    base_fee = hours * rate
    revision_fee = revisions * 50
    total = base_fee + revision_fee
    return total
total_fee = calculate_quote(project_hours, project_rate, project_revisions)
def print_quote(name, project_type, hours, rate, revisions, total):
    print("\n--- PROJECT ESTIMATE ---")
    print(f"Client: {name}")
    print(f"Project: {project_type}")
    print(f"Hours: {hours} @ ${rate:.2f}/hr")
    print(f"Revisions: {revisions} @ $50.00/round")
    print(f"Total: ${total:.2f}")
    print("---------------------")
print_quote(client_name, client_project, project_hours, project_rate, project_revisions, total_fee)