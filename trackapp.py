import trackdatabase

MENU = """
Please choose an option:

1) add a time into the database
2) see all times in the database
3) see best time for an event
4) exit

your selection:
"""


connection = trackdatabase.connect()

trackdatabase.create_table(connection)


def menu():
    user_input = input(MENU)
    while user_input != "4":

        if user_input == "1":

            name = input("enter name:")
            event = input("enter event")
            time = input("enter time")

            trackdatabase.add_time(connection,name,time,event)

        if user_input == "2":

            print(trackdatabase.get_times(connection))

        if user_input == "3":

            event = input("enter an event")
            print(trackdatabase.get_best_time(connection, event))

        if int(user_input) > 4:
            print("please choose a number in the menu")
            
        user_input = input(MENU)
menu()