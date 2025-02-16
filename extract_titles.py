import os
import json

def extract_titles(docs_dir="/data/docs", output_file="/data/docs/index.json"):
    index = {}
    
    # Walk through the docs_dir recursively.
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                # Get relative path to docs_dir (e.g., "README.md" or "path/to/file.md")
                rel_path = os.path.relpath(full_path, docs_dir)
                
                title = None
                with open(full_path, "r", encoding="utf-8") as f:
                    for line in f:
                        stripped = line.lstrip()
                        if stripped.startswith("#"):
                            # Remove the leading '#' characters and whitespace to get the title.
                            title = stripped.lstrip("#").strip()
                            break
                if title:
                    index[rel_path] = title
                else:
                    # Optionally, handle files with no H1 (e.g., skip or assign a default value)
                    index[rel_path] = ""
    
    # Write the index as JSON with indentation for readability.
    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(index, out, indent=2)
    
    print(f"Created index with {len(index)} entries at {output_file}")

if __name__ == "__main__":
    extract_titles()
