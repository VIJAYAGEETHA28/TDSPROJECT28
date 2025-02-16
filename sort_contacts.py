import json

def sort_contacts(input_file="/data/contacts.json", output_file="/data/contacts-sorted.json"):
    # Read contacts from the input file
    with open(input_file, "r") as infile:
        contacts = json.load(infile)
    
    # Sort contacts by last_name then first_name (case-insensitive)
    sorted_contacts = sorted(
        contacts,
        key=lambda c: (c.get("last_name", "").lower(), c.get("first_name", "").lower())
    )
    
    # Write the sorted contacts to the output file with indent for readability
    with open(output_file, "w") as outfile:
        json.dump(sorted_contacts, outfile, indent=2)
    
    print(f"Sorted contacts have been written to {output_file}")

if __name__ == "__main__":
    sort_contacts()
