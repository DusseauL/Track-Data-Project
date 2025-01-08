import trackdatabase

MENU = """
Please choose an option:

1) add a time into the database
2) see all times in the database
3) see best time for an event
4) sort times based on an event
5) see all times for an event
6) see average time for an event
7) exit

your selection:
"""

trackdatabase.create_table()

def menu():
    user_input = input(MENU)
    while user_input != "7":
        if user_input == "1":

            name = input("enter name:")
            event = input("enter event")
            time = input("enter time")

            trackdatabase.add_time(name,time,event)

        elif user_input == "2":

            print(trackdatabase.get_times())

        elif user_input == "3":

            event = input("enter an event:")
            print(trackdatabase.get_best_time(event))


        elif user_input == "4":

            event = input("enter an event:")
            print(f"times for {event}:")
            print(trackdatabase.get_sorted_times_by_event(event))

        elif user_input == "5":
            event = input("enter an event:")
            print(f"times for {event}:")
            print(trackdatabase.get_times_per_event(event))
        elif user_input == "6":
            event = input("enter an event")
            print(f"average time of event")
            print(trackdatabase.get_average_time(event))
        else:
            print("please choose a number in the menu")

        user_input = input(MENU)
menu()