import sys

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice

students= []
def readModules():
    modules = []
    moduleName = input("\tEnter the first module name: ").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\tEnter grade: "))
        modules.append(module)
        moduleName = input("\tEnter the next module name: ".strip())
    return modules
def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)
    print(students)
   
def displayModules(modules):
    print("\tName \tGrade")
    for module in modules:
        print(f"\t{ module['name']} \t{ module['grade']}")
def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])
    
def doNothing(dumby):
    pass

choiceMap = {
'a': doAdd,
'v': doView,
'q': doNothing 
}

students = []
selection = displayMenu()
while(selection != 'q'):
    if selection in choiceMap:
        choiceMap[selection](students)
    else:
        print("\n\nPlease select either a, v or q")
    selection = displayMenu()

'''

while(selection != 'q'):
    if selection == 'a':
        doAdd()
    elif selection =='v':
        doView()
    elif selection != 'q':
        print("\n\nPlease select either a, v or q")
    selection = displayMenu()       

#print(f"You chose {selection}")

'''


