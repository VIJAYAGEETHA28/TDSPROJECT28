import json

def read_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
    
import os

def write_file(file_path, content):
    # Ensure the directory exists before writing the file
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "w") as file:
        file.write(content)
