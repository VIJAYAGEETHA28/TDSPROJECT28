import requests
datagen_url = "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py"
response = requests.get(datagen_url)
if response.status_code != 200:
    raise Exception(f"Failed to download datagen.py, status code: {response.status_code}")
    
datagen_filename = "datagen.py"
with open(datagen_filename, "w") as f:
    f.write(response.text)