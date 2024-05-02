schedule_dict = {
    "Flight 1": {"Departure": "New York", "Destination": "Los Angeles", "Departure Time": "08:00", "Arrival Time": "11:00"},
    "Flight 2": {"Departure": "Los Angeles", "Destination": "New York", "Departure Time": "12:00", "Arrival Time": "15:00"},
    "Flight 3": {"Departure": "Chicago", "Destination": "Miami", "Departure Time": "10:30", "Arrival Time": "14:00"},
    "Flight 4": {"Departure": "Miami", "Destination": "Chicago", "Departure Time": "15:30", "Arrival Time": "19:00"},
    "Flight 5": {"Departure": "San Francisco", "Destination": "Seattle", "Departure Time": "09:45", "Arrival Time": "11:30"},
    "Flight 6": {"Departure": "Seattle", "Destination": "San Francisco", "Departure Time": "13:00", "Arrival Time": "14:45"}
}

# Define a function to handle user requests
def handle_request(user_input):
    if user_input.lower() == "exit":
        return "Goodbye!", True  # Signal to exit the loop
    elif user_input in schedule_dict:
        flight_info = schedule_dict[user_input]
        return f"Flight {user_input}: Departure from {flight_info['Departure']} at {flight_info['Departure Time']} to {flight_info['Destination']}, arriving at {flight_info['Arrival Time']}", False
    else:
        return "I'm sorry, that flight is not in the schedule.", False

# Main loop to prompt user for input
exit_loop = False
while not exit_loop:
    user_input = input("Which flight would you like to check? Type 'exit' to quit. ")
    response, exit_loop = handle_request(user_input)
    print(response)
