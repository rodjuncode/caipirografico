import os
import json
from colorthief import ColorThief

def update_json_data():
    data_file = 'data/data.json'
    covers_dir = 'data/covers/'
    properties = ['title', 'artist', 'release', 'cover', 'palette']  # Required properties

    # Load or initialize data
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            data = json.load(file)
    else:
        data = []

    # Iterate over each image in the covers directory
    for cover_file in os.listdir(covers_dir):
        cover_path = os.path.join(covers_dir, cover_file)
        # Check if there's an existing entry for the cover
        existing_entry = next((item for item in data if item.get('cover') == cover_file), None)

        if existing_entry:
            # Check if all properties exist
            if all(prop in existing_entry for prop in properties):
                continue  # Move to the next file if all properties are present

        # Process the cover file if it's new or incomplete
        artist, rest = cover_file.split('-', 1)
        title, release = rest.rsplit('(', 1)
        release = release.rstrip(').jpg').rstrip(').png').rstrip(').jpeg')  # Remove file extension and closing parenthesis
        color_thief = ColorThief(cover_path)
        palette = color_thief.get_palette(color_count=3, quality=1)

        # Create or update the entry
        new_entry = {
            'title': title,  # Update as needed
            'artist': artist,  # Update as needed
            'release': release,  # Update as needed
            'cover': cover_file,
            'palette': palette
        }

        # Replace the existing entry if it exists, otherwise append
        if existing_entry:
            data[data.index(existing_entry)] = new_entry
        else:
            data.append(new_entry)

    # Save the updated data back to the file
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    update_json_data()