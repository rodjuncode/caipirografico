import json
from datetime import datetime

# Function to append timestamp to JSON file
def append_timestamp(file_path='data.json'):
    # Get current timestamp
    current_timestamp = datetime.now().isoformat()
    
    try:
        # Read existing data
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If file does not exist, start a new list
        data = []
    except json.JSONDecodeError:
        # If file is empty or not valid JSON, start a new list
        data = []

    # Append the current timestamp
    data.append({'timestamp': current_timestamp})
    
    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Call the function
append_timestamp()