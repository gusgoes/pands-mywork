rawString = input("Please enter a string: ") 
normalisedString = rawString.strip().lower() 
lenghtOfRawString = len(rawString) 
lenghtOfNormalised = len(normalisedString) 
print(f"That String normalised is :\"{normalisedString}\"") 
print(f"We reduced the input string from {lenghtOfRawString} to {lenghtOfNormalised} characters")