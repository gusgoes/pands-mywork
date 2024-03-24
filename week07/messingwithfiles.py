# Messing with files
#Author: Gustavo Fernandes

FILENAME = "data.txt"

'''with open(FILENAME, 'r') as f:
    data = f.read()
    #print(data.strip(), end="")
    print(data.strip())'''

with open("data2.txt", "w+") as f:
    f.write("how now\n")
    f.write("brwon cow\n")
    f.seek(0)
    data = f.read()
print(data)