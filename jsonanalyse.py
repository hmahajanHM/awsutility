import json
import argparse
import sys
import os
import platform

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

# Example usage:
# print("This will be cleared...")
# input("Press Enter to clear the screen...")
# clear_screen()
# print("Screen cleared!")
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
    clear_screen()
    json_data = main()
    record_count= recordcount(json_data)
