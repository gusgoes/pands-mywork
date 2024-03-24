import json

electricity = {
    'name' : 'Andrew',
    'amount' : 100
    }
with open("electricity.json", "w") as f:
    json.dump(electricity, f)