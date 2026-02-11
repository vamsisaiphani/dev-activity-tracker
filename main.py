import datetime

def add_log():
    today = datetime.date.today()
    activity = input("What did you code today? ")
    time_spent = input("Time spent (in hours): ")
    errors = input("Errors faced (if any): ")
    learning = input("What did you learn today? ")

    log = f"{today},{activity},{time_spent},{errors},{learning}\n"

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

def main():
    print("Developer Activity Tracker")
    print("1. Add today's log")
    print("2. View logs")
    choice = input("Enter choice: ")

    if choice == "1":
        add_log()
    elif choice == "2":
        view_logs()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
