# I have used the json format in order to save the event information in json format
import json
# I used the date time library for getting input from the user while adding the event
from datetime import datetime
# Here i have created an empty calender array  for storing the events
calendar = []

# Function which will help the users to add events of their interest
def add_event():
    # It will ask the users to enter event name of their choice
    name = input("Enter event name: ")
    # It will ask the users to enter event specific time
    time_str = input("Enter event time (YYYY-MM-DD HH:MM): ")
    try:
        # Here i used the string parse time function to define the date 
        # and time acording to the specific format
        event_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        # This will verify the extra feature behaviour, if the new event is 
        #overlapping with the previous added event 
        #if yes then it will filters events in the calendar array 
        #where the event time matches the entered event time 
        #and also shows the warning message to the user 
        #otherwise print the message that event added successfully.
        overlapping_events = [event for event in calendar
                              if event['time'] == event_time] # It matches the time object in calender array stored in program memory
        if overlapping_events:
            print("Warning Message: This event overlaps with an existing event.")
        else:
            calendar.append({'name': name, 'time': event_time})
            print("Event added successfully.")
    # It shows error message if user enter incorrect time format
    except ValueError:
        print("You have Entered Invalid Time Format. Please Use This Format (YYYY-MM-DD HH:MM)")
# Function which will help the users to delete events of their choice by enterin the event name
def remove_event():
    name = input("Enter event name to remove: ")
    removed = False
    # This loop will help to find out the event which user want to delete
    for event in calendar:
        # It will compare the event name in calender array with the user enter event name
        if event['name'] == name:
            # If event name is matched in calendar array 
            #then it will delete that event by using the remove function
            calendar.remove(event)
            # If the name matched then it will set the removed variable is equal to true
            removed = True
    # if removed variable is true then it display the message that event has been removed successfully
    if removed:
        print(f"Event '{name}' has been removed successfully.")
    # If event name is not matched then it will display this message
    else:
        print(f"No Such Event '{name}' is Present within this name.")
        
# Function which will help the users to view events of their choice 
#by entering the time interval in which their events are existed
def print_calendar():
    # These inputs will ask the user to enter the specific time interval
    start_time_str = input("Enter start time (YYYY-MM-DD HH:MM): ")
    end_time_str = input("Enter end time (YYYY-MM-DD HH:MM): ")
    try:
        # It will convert the start and end time strings into a datetime object using the strptime 
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
        # It will match the events which come within the user enter time frame
        events_within_interval = [event for event in calendar
                                  if start_time <= event['time'] <= end_time]
        events_within_interval.sort(key=lambda x: x['time'])
        if events_within_interval:
            # It will print all those events within this time frame in a Chronological Order
            print("Events within the interval:")
            current_date = None
            for event in events_within_interval:
                if current_date != event['time'].date():
                    current_date = event['time'].date()
                    print(f"\n{current_date}")
                print(f"{event['time'].strftime('%H:%M')} - {event['name']}")
        else:
            print("No events are present within the specified interval.") # It will display this messae if no event is present
    except ValueError:
        print("You have Entered Invalid Time Format. Please Use This Format (YYYY-MM-DD HH:MM)")
# Function which will allow the users to save events in the specific file 
#so that when they closed the program, they will be able to view their events which they have saved earlier
# Default file name is eventsdetailfile
def save_calendar(filename='eventsdetailfile.json'):
    # It will open the specified file with write permission and the file is represented by the variable file within the indented block.
    with open(filename, 'w') as file:
        # Most importantly, it will convert the calendar event data into JSON format 
        #and also when use load that data it will help to again converti this JSON data
        json.dump(calendar, file, default=str)
    print(f"Calendar has been saved to specific {filename}.")

# Function which will allow the users to upload the saved file from their local/host machine, 
#if filename is not provide by the user it will uppload the default file which is "eventsdetailfile.json"
def load_calendar(filename='eventsdetailfile.json'):
    # Declared the global variable
    global calendar
    try:
        # It will open the specified file with read permission
        with open(filename, 'r') as file:
            # It will load the JSON data and also convert it into Python data structure 
            #and stored the resulted data into loaded data variable
            loaded_data = json.load(file)
            # It wil create a new calendar variable by iterating through each event object in the loaded data 
            #and creating a list for each event and also converted the 'time' field from string to a datetime object using datetime.strptime function
            calendar = [{'name': event['name'], 'time': datetime.strptime(event['time'], "%Y-%m-%d %H:%M:%S")}
                        for event in loaded_data]
        # It will print the success message
        print(f"Calendar has been loaded from {filename}.")
    # If no file is saved yet then it will print this message
    except FileNotFoundError:
        print("Calendar file is not found.")
    # If there is a file but error in uploading that file then it will print this message
    except ValueError as e:
        print(f"Error while loading calendar: {e}")
#It will call the main function
def main():
    # It will ask the user to enter the file name if he has created it before, 
    #otherwise he can also use the default name
    filename = input("Enter calendar filename (default: eventsdetailfile.json): ") or 'eventsdetailfile.json'
    # It will call the load calendar function and load the file
    load_calendar(filename)
    # This loop will displays a menu to the user 
    #and it will be executed until the user chooses to exit (press 6 to quit).
    while True:
        print("\nMenu:")
        print("1. Add Event")
        print("2. Remove Event")
        print("3. Print Calendar")
        print("4. Save Calendar")
        print("5. Load Calendar")
        print("6. Exit")
        # It will ask the user to enter his choice, 1- for add new event, 
        #2- for remove the added event, 3- it will print the added events, 
        #4- it will save the event file, 5- it will load the event file, 
        #6- it will exit the program
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            add_event()
        elif choice == '2':
            remove_event()
        elif choice == '3':
            print_calendar()
        elif choice == '4':
            new_filename = input("Enter filename to save (default: eventsdetailfile.json): ") or 'eventsdetailfile.json'
            save_calendar(new_filename)
        elif choice == '5':
            new_filename = input("Enter filename to load (default: eventsdetailfile.json): ") or 'eventsdetailfile.json'
            load_calendar(new_filename)
        elif choice == '6':
            save_calendar(filename)
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
# It will call the main function
if __name__ == "__main__":
    main()
