import os

def extract_recent_log_lines(log_dir="/data/logs", output_file="/data/logs-recent.txt", count=10):
    # List all files in the log directory that end with '.log'
    log_files = [os.path.join(log_dir, f) for f in os.listdir(log_dir) if f.endswith('.log')]
    
    # Sort the log files by modification time, newest first
    sorted_logs = sorted(log_files, key=lambda f: os.path.getmtime(f), reverse=True)
    
    # Select the 10 most recent log files (or fewer if there aren't 10)
    recent_logs = sorted_logs[:count]
    
    first_lines = []
    for log_file in recent_logs:
        try:
            with open(log_file, "r") as f:
                # Read the first line of the log file (strip removes any extra whitespace/newlines)
                line = f.readline().strip()
                first_lines.append(line)
        except Exception as e:
            print(f"Error reading {log_file}: {e}")
    
    # Write the first lines to the output file, one line per log file
    with open(output_file, "w") as f:
        for line in first_lines:
            f.write(line + "\n")
    
    print(f"Wrote first lines of {len(first_lines)} log files to {output_file}")

if __name__ == "__main__":
    extract_recent_log_lines()
