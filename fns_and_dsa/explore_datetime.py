from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format: YYYY-MM-DD HH:MM:SS
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted)

def calculate_future_date():
    try:
        days = int(input("Enter number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
