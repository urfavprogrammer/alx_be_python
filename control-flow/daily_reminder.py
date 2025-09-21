task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Reminder: {task} is a high priority task with no immediate attention!")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: {task} is a medium priority task that requires attention today!")
        elif time_bound == 'no':
            print(f"Reminder: {task} is a medium priority task with no immediate attention!")
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: {task} is a low priority task that should be completed during time frame")
        elif time_bound == 'no':
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")