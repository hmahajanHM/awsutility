import json
import argparse
import sys
import os
import platform
import json

def count_null_property(json_data, property_name):
    """
    Counts the number of records where the specified property has a null value.

    Args:
        json_data (str): The JSON string containing a list of records.
        property_name (str): The name of the property (key) to check for null values.

    Returns:
        int: The total count of records where the property is null.
    """

    null_count = 0

    for record in json_data:
        # 1. Check if the dictionary contains the key (the property_name)
        # 2. Check if the value associated with that key is None (JSON null)
        if isinstance(record, dict) and property_name in record and record[property_name] is None:
            null_count += 1
            
    return null_count

def clear_screen():
    """
    Clears the console screen based on the operating system.
    """
    # Check the operating system
    if platform.system() == "Windows":
        # Command for Windows
        os.system('cls')
    else:
        # Command for Linux and macOS (uses 'clear' command)
        os.system('clear')

def jsonrecordpropertycount(data):
    for index, record in enumerate(data):
        if isinstance(record, dict):
            # The keys of the dictionary are the top-level properties (roots) of that record
            root_keys = list(record.keys())
        else:
            print(f"Record {index + 1}: Not a dictionary/object, type is {type(record).__name__}")
    return len(root_keys)
    
def recordcount(data):
    # The JSON string provided by the user
    try:
        # Load the JSON string into a Python object (a list)
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
    return record_count
    
    
def readconfig():
    try:
    # Open and read JSON file
        with open("config", "r") as f:
            configdata = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        sys.exit(1)
    
    return configdata

def main():    
    # 1. Create the parser
    parser = argparse.ArgumentParser(
        description="A script to process a specified file.",
        # Example usage message for the help screen
        epilog="Example: python your_script.py -f data.txt"
    )

    # 2. Define the argument: -f or --filename
    parser.add_argument(
        '-f',                     # Short form
        '--filename',             # Long form
        type=str,                 # Expected data type (a string for the filename)
        required=True,            # Makes the argument mandatory
        help='The path to the input file to be processed.'
    )

    # 3. Parse the arguments from the command line
    args = parser.parse_args()

    # 4. Access the value using the argument name ('filename')
    input_filename = args.filename
    print(f"Input file to be processed: {input_filename}")
    try:
    # Open and read JSON file
        with open(input_filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        sys.exit(1)
    
    return data
    # Access values

if __name__ == "__main__":
    clear_screen()
    json_data = main()
    
    record_count= recordcount(json_data)
    property_count= jsonrecordpropertycount(json_data)
    count_x = count_null_property(json_data, 'x')
    print(f"Count of records where 'x' is null: {count_x}")
