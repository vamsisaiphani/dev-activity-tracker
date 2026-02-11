import datetime

def add_log():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    activity = input("What did you code today? ")
    time_spent = input("Time spent (in hours): ")
    errors = input("Errors faced (if any): ")
    learning = input("What did you learn today? ")

    log = f"{timestamp},{activity},{time_spent},{errors},{learning}\n"

    with open("data/logs.csv", "a") as file:
        file.write(log)

    print("✅ Activity logged successfully")

def view_logs():
    try:
        with open("data/logs.csv", "r") as file:
            print("\n--- Activity Logs ---")
            print(file.read())
    except FileNotFoundError:
        print("No logs found.")

def weekly_summary():
    try:
        with open("data/logs.csv", "r") as file:
            lines = file.readlines()

        last_7_days = datetime.datetime.now() - datetime.timedelta(days=7)
        total_hours = 0
        entries = 0

        for line in lines:
            parts = line.strip().split(",")
            timestamp = datetime.datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
            hours = float(parts[2])

            if timestamp >= last_7_days:
                total_hours += hours
                entries += 1

        print("\n--- Weekly Summary ---")
        print(f"Entries logged: {entries}")
        print(f"Total hours coded: {total_hours}")

    except FileNotFoundError:
        print("No logs found.")

def main():
    print("Developer Activity Tracker")
    print("1. Add today's log")
    print("2. View logs")
    print("3. Weekly summary")
    choice = input("Enter choice: ")


    if choice == "1":
        add_log()
    elif choice == "3":
        weekly_summary()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
