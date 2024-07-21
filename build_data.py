import json
import os
from datetime import datetime

def create_json_data(folder_path='data/covers', file_path='data/data.json'):
    # Initialize data list
    data = []

    # Try to load existing data
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass  # If no file or invalid JSON, start with an empty list

    # List of existing covers to avoid duplicates
    existing_covers = [entry['cover'] for entry in data if 'cover' in entry]

    # List image files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.png', '.jpg', '.jpeg')) and file_name not in existing_covers:
            # Parse file name
            artist, rest = file_name.split('-', 1)
            title, release = rest.rsplit('(', 1)
            release = release.rstrip(').jpg').rstrip(').png').rstrip(').jpeg')  # Remove file extension and closing parenthesis

            # Trim content
            artist = artist.strip()
            title = title.strip()
            release = release.strip()

            # Append new entry
            data.append({
                'title': title,
                'artist': artist,
                'release': release,
                'cover': file_name
            })

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Call the function
create_json_data()