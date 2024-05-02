schedule_dict = {
    "Flight 1": {"Departure": "New York", "Destination": "Los Angeles", "Departure Time": "08:00", "Arrival Time": "11:00"},
    "Flight 2": {"Departure": "Los Angeles", "Destination": "New York", "Departure Time": "12:00", "Arrival Time": "15:00"},
    "Flight 3": {"Departure": "Chicago", "Destination": "Miami", "Departure Time": "10:30", "Arrival Time": "14:00"},
    "Flight 4": {"Departure": "Miami", "Destination": "Chicago", "Departure Time": "15:30", "Arrival Time": "19:00"},
    "Flight 5": {"Departure": "San Francisco", "Destination": "Seattle", "Departure Time": "09:45", "Arrival Time": "11:30"},
    "Flight 6": {"Departure": "Seattle", "Destination": "San Francisco", "Departure Time": "13:00", "Arrival Time": "14:45"}
}

print("Flights' Running:")
print(schedule_dict)

def handle_request(user):
    if user.lower() == "exit":
        return "Goodbye!", True
    elif user in schedule_dict:
        flight_info = schedule_dict[user]
        return f"Flight {user}: Departure from {flight_info['Departure']} to{flight_info['Destination']} at {flight_info['Departure Time']} arriving at {flight_info['Arrival Time']}", False
    else:
        return "Sorry, that Flight is not scheduled", False

exit_loop = False
while not exit_loop:
    user = input("Which flight would you like to check? Type 'exit' to quit ")
    response , exit_loop = handle_request(user)
    print(response)
