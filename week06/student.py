'''What would you like to do?
 (a) Add new student
 (v) View students
 (q) Quit
Type one letter (a/v/q):d
you chose d
'''

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice
choice = displayMenu()
print(f"You chose {choice}")