import keyboard
from datetime import datetime
import os

# Directory for logs
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

typed = ""

print("Start typing. Press Enter to log. Ctrl+C to exit.")

while True:
    event = keyboard.read_event()  # Read each key event

    if event.event_type != "down":
        continue  # Ignore key releases

    if event.name == "enter":
        if typed.strip():  # Avoid logging empty lines
            # Daily log file
            today = datetime.now().strftime("%Y-%m-%d")
            file_path = os.path.join(log_dir, f"logs_{today}.txt")

            # Timestamp
            timestamp = datetime.now().strftime("%H:%M:%S")
            log_entry = f"[{timestamp}] {typed}\n"

            # Write to file
            with open(file_path, "a") as f:
                f.write(log_entry)

            # Print logged line once
            print(f"\nLogged: {log_entry.strip()}")

        typed = ""  # Reset for next line

    elif event.name == "space":
        typed += " "
    elif len(event.name) == 1:  # letters, numbers, punctuation
        typed += event.name