import os
import requests
import json
import shutil
import sqlite3
import pandas as pd
import subprocess
from bs4 import BeautifulSoup
from utils import read_file, write_file

DATA_DIR = "data/"

# 🚨 Security Rules: B1 & B2 🚨
def b12(file_path):
    """Ensure the path is within /data and prevent file deletions."""
    if not file_path.startswith(DATA_DIR):
        raise PermissionError("❌ Task Denied: Access to external directories is not allowed.")
    if "delete" in file_path.lower():
        raise PermissionError("❌ Task Denied: Deletion of files is not allowed.")
    return file_path

# ✅ Task B3: Fetch data from an API and save it
def fetch_api_data():
    """Fetch data from an API and save it."""
    api_url = "https://jsonplaceholder.typicode.com/posts"
    output_path = os.path.join(DATA_DIR, "api_data.json")

    response = requests.get(api_url)
    if response.status_code == 200:
        write_file(output_path, json.dumps(response.json(), indent=2))
        return f"✅ Task B3 Successful: API data saved to {output_path}."
    return f"❌ Task B3 Failed: API request error."


# ✅ Task B4: Clone a git repo and make a commit
def clone_and_commit_repo():
    """Clone a GitHub repo and make a commit."""
    repo_url = "https://github.com/user/repo.git"
    repo_dir = os.path.join(DATA_DIR, "repo")

    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir)  # Remove old repo

    subprocess.run(["git", "clone", repo_url, repo_dir], check=True)
    with open(os.path.join(repo_dir, "README.md"), "a") as f:
        f.write("\nUpdated via automation.")
    subprocess.run(["git", "add", "."], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "Automated update"], cwd=repo_dir, check=True)
    return "✅ Task B4 Successful: Git repo cloned and updated."



import json
import sqlite3
import duckdb

def run_sql_query(db_path: str, query: str, output_filename: str):
    """
    B5: Run a SQL query on a SQLite (.db) or DuckDB (.duckdb) database.

    :param db_path: Path to the database file (e.g., 'mydata.db' or 'mydata.duckdb').
    :param query:   SQL query to execute.
    :param output_filename: Path to the file where the query results should be saved.
    :return:        A dictionary with the results or a summary of what was written.
    """
    # Decide which DB engine to use based on the file extension
    if db_path.endswith('.db'):
        conn = sqlite3.connect(db_path)
    else:
        # Otherwise assume DuckDB (or refine logic if you have multiple possible extensions)
        conn = duckdb.connect(db_path)

    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()

    # Write results to the output file
    with open(output_filename, 'w', encoding='utf-8') as f:
        for row in rows:
            # Convert each row tuple to a comma-separated line (or format however you like)
            line = ', '.join(str(item) for item in row)
            f.write(line + '\n')

    return {
        "status": "success",
        "row_count": len(rows),
        "results_preview": rows[:5]  # or you can return all rows, but often a preview is enough
    }


# ✅ Task B6: Extract data from (i.e., scrape) a website
def write_file(file_path, content):
    """Helper function to write content to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

def scrape_website():
    """Scrape data from a website and save it."""
    url = "https://news.ycombinator.com/"  # Replace with a valid URL
    output_path = os.path.join(DATA_DIR, "scraped_data.txt")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.get_text()

        write_file(output_path, data)
        return f"✅ Task B6 Successful: Website data saved."
    except requests.exceptions.RequestException as e:
        return f"❌ Error: {e}"
