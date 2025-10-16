import json

# Open and read JSON file
with open("data.json", "r") as f:
    data = json.load(f)

# Access values
print(data)
