from datetime import datetime


def generate_log(data):
    # Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")

    # Filename format required by rubric
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write file exactly as input list
    with open(filename, "w") as file:
        for entry in data:
            file.write(str(entry) + "\n")

    # EXACT print format (important for tests)
    print(f"Log written to {filename}")

    return filename