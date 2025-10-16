import json
import argparse
import sys


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
    print(record_count)
    return record_count

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

    try:
    # Open and read JSON file
        with open(input_filename, "r") as f:
            data = json.load(f)
        print(data)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        sys.exit(1)
    
    return data
    # Access values

if __name__ == "__main__":
    json_data = main()
    record_count= recordcount(json_data)
