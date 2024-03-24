#messing with os module
import os

FILENAME = "messingwithfiles.py"

if os.path.exists(FILENAME):
    with open(FILENAME, 'r') as f:
       for line in f:
           print(line)
else:
    print(FILENAME,"File does not exist")

os.remove("data2.txt") #removes the file data2.txt