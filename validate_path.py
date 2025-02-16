import json
import re

# Load JSON file
with open("B12.json", "r") as file:
    data = json.load(file)

# Extract the regex pattern
pattern = data["parameters"]["properties"]["filepath"]["pattern"]

# Function to validate a file path
def validate_filepath(filepath):
    if re.match(pattern, filepath):
        print(f"✅ Valid filepath: {filepath}")
    else:
        print(f"❌ Invalid filepath: {filepath}. Must start with /data/")

# Test cases
validate_filepath("/data/myfile.txt")   # ✅ Valid
validate_filepath("/otherdir/myfile.txt")  # ❌ Invalid
