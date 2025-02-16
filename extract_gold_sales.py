import sqlite3

def A10(filename='/data/ticket-sales.db', output_filename='/data/ticket-sales-gold.txt', 
        query="SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'"):
    # Connect to the SQLite database
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    # Calculate the total sales for the "Gold" ticket type
    cursor.execute(query)
    total_sales = cursor.fetchone()[0]

    # If there are no sales, set total_sales to 0
    total_sales = total_sales if total_sales else 0

    # Write the total sales to the file
    with open(output_filename, 'w') as file:
        file.write(str(total_sales))

    # Close the database connection
    conn.close()

    # Print the result for verification
    print(f"✅ Total Gold ticket sales saved to {output_filename}: {total_sales}")

# Run the function
A10()
