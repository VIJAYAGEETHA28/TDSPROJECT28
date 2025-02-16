import os
import json
import re

docs_dir = "/data/docs/"
index_file = "/data/docs/index.json"

index = {}

for root, _, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("# "):  # Find first H1
                        relative_path = os.path.relpath(file_path, docs_dir)
                        normalized_path = relative_path.replace("\\", "/")  # Fix Windows paths
                        index[normalized_path] = line.strip("# ").strip()
                        break

with open(index_file, "w", encoding="utf-8") as f:
    json.dump(index, f, indent=4)
