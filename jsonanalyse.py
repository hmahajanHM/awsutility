import json


def recordcount(data):
    # The JSON string provided by the user
    json_string = '[{},{},{}]'
    try:
        # Load the JSON string into a Python object (a list)
        data = json.loads(json_string)
    
        # Count the number of elements in the list
        if isinstance(data, list):
            record_count = len(data)
            # The result is 3
        else:
            # Handle cases where the JSON is not a list
            record_count = 0
    except json.JSONDecodeError:
        # Handle invalid JSON
        record_count = "Error decoding JSON"
    print(record_count)
    return record_count

def main():    
    # Open and read JSON file
    with open("data.json", "r") as f:
        data = json.load(f)
    print(data)
    return data
    # Access values
    
if __name__ == "__main__":
    json_data = main()
    record_count= recordcount(json_data)
