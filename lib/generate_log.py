from datetime import datetime


def generate_log(data):
    # Validate input type
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")

    # Generate filename in required format
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write file (exact match of list items)
    with open(filename, "w") as file:
        for entry in data:
            file.write(str(entry) + "\n")

    # Confirmation message
    print(f"Log written to {filename}")

    return filename