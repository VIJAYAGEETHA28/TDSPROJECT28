import json
import re
import requests

# Load JSON file
with open("B3.json", "r") as file:
    data = json.load(file)

# Extract validation patterns
url_pattern = data["parameters"]["properties"]["url"]["pattern"]
save_path_pattern = data["parameters"]["properties"]["save_path"]["pattern"]

# Function to download data
def fetch_and_save(url, save_path):
    # Validate URL and Save Path
    if not re.match(url_pattern, url):
        print("❌ Invalid URL format.")
        return
    if not re.match(save_path_pattern, save_path):
        print("❌ Invalid save path. Must be inside /data/.")
        return

    # Fetch data from the API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for failed requests

        # Save the content
        with open(save_path, "wb") as file:
            file.write(response.content)
        
        print(f"✅ Data saved successfully to {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")

# Example usage
fetch_and_save("https://jsonplaceholder.typicode.com/todos/1", "/data/todo.json")
