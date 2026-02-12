import datetime

DATA_FILE = "data/logs.csv"


def read_logs():
    try:
        with open(DATA_FILE, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def write_log(entry):
    with open(DATA_FILE, "a") as file:
        file.write(entry)


def add_log():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    activity = input("What did you code today? ").strip()
    if not activity:
        print("Activity cannot be empty.")
        return

    try:
        time_spent = float(input("Time spent (in hours): "))
        if time_spent <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid number greater than 0.")
        return

    errors = input("Errors faced (if any): ").strip()
    learning = input("What did you learn today? ").strip()

    entry = f"{timestamp},{activity},{time_spent},{errors},{learning}\n"
    write_log(entry)

    print("✅ Activity logged successfully")


def view_logs():
    logs = read_logs()
    if not logs:
        print("No logs found.")
        return

    print("\n--- Activity Logs ---")
    for log in logs:
        print(log.strip())


def weekly_summary():
    logs = read_logs()
    if not logs:
        print("No logs found.")
        return

    last_7_days = datetime.datetime.now() - datetime.timedelta(days=7)
    total_hours = 0
    entries = 0

    for log in logs:
        parts = log.strip().split(",")

        # Handle both old and new timestamp formats
        try:
            timestamp = datetime.datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            timestamp = datetime.datetime.strptime(parts[0], "%Y-%m-%d")

        try:
            hours = float(parts[2])
        except ValueError:
            continue

        if timestamp >= last_7_days:
            total_hours += hours
            entries += 1

    print("\n--- Weekly Summary ---")
    print(f"Entries logged: {entries}")
    print(f"Total hours coded: {total_hours}")



def main():
    print("\nDeveloper Activity Tracker")
    print("1. Add today's log")
    print("2. View logs")
    print("3. Weekly summary")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        add_log()
    elif choice == "2":
        view_logs()
    elif choice == "3":
        weekly_summary()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
