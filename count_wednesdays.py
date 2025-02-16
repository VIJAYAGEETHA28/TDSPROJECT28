from datetime import datetime 

def parse_date(date_str):
    """Try multiple date formats and return a valid datetime object."""
    formats = ["%Y-%m-%d", "%b %d, %Y", "%d-%m-%Y", "%m/%d/%Y", "%d-%b-%Y", "%Y/%m/%d %H:%M:%S"]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Unknown date format: {date_str}")

def count_wednesdays(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            dates = f.read().splitlines()

        # Count Wednesdays
        wednesday_count = sum(1 for date in dates if parse_date(date).weekday() == 2)

        # ✅ Write **only** the number to the file (no extra spaces or newlines)
        with open(output_file, "w") as f:
            f.write(str(wednesday_count))

        print(f"Successfully counted Wednesdays: {wednesday_count}")
    except Exception as e:
        print(f"Error: {e}")

# File paths
input_file = "/data/dates.txt"
output_file = "/data/dates-wednesdays.txt"

# Run the function
count_wednesdays(input_file, output_file)
