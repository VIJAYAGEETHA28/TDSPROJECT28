def extract_sender_email(filename='/data/email.txt', output_file='/data/email-sender.txt'):
    try:
        # Read the email file
        with open(filename, 'r', encoding='utf-8') as file:
            email_content = file.readlines()

        sender_email = None

        # Extract sender's email
        for line in email_content:
            if line.lower().startswith("from:"):  # Ensure case-insensitive check
                sender_email = line.strip().split(" ")[-1].replace("<", "").replace(">", "")
                break  # Stop after finding the first occurrence

        # If no email found, set a default message
        if not sender_email:
            sender_email = "No sender email found"

        # Write the extracted email to output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(sender_email + "\n")

        print(f"✅ Extracted sender email: {sender_email}")

    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Run the function if the script is executed directly
if __name__ == "__main__":
    extract_sender_email()
