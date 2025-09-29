from datetime import datetime, timedelta

current_date = datetime.now()

formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted datetime:", formatted_datetime)

# future_time =  current_date + timedelta(days=7, hours=5)
# past_time = current_date - timedelta(days=3, hours=2)

def display_current_datetime():
    current_date = formatted_datetime
    print("Current date and time:", current_date)

def calculate_future_date(days):
    future_time = current_date + timedelta(days=days)
    print("Future date:", future_time.strftime("%Y-%m-%d"))
    return future_time

display_current_datetime()
days = int(input("Enter the number of days to add to the current date: "))

calculate_future_date(days)



# print("Past time (3 days ago):", past_time)
# print("Future time (7 days later):", future_time)