# Week 5 - File Handling
# Jake Talbert
with open("notes.txt", "w") as file:
    file.write("My first file created with Python!\n")
    file.write("I am a freelancer ready for hire.")
with open("notes.txt", "r") as file:
    contents = file.read()
print(contents)