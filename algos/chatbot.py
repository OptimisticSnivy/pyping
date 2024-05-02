import random

def greet():
    responses = ["Hello! How can I assist you today?",
                 "Hi there! What can I help you with?",
                 "Welcome! How may I assist you with your flight?"]
    return random.choice(responses)

def get_flight_status(flight_number):
    if flight_number == "ABC123":
        return "The flight ABC123 is on time."
    elif flight_number == "XYZ789":
        return "The flight XYZ789 is delayed by 1 hour."
    else:
        return "I'm sorry, I couldn't find information for that flight."

def handle_message(message):
    if message.lower() == "hi" or message.lower() == "hello":
        return greet()
    elif "flight status" in message.lower():
        words = message.split()
        for word in words:
            if word.isalnum() and word.isupper() and len(word) == 6:
                return get_flight_status(word)
        return "Please provide a valid flight number."
    else:
        return "I'm sorry, I didn't understand that. Could you please repeat or specify your query?"

# Main loop
print(greet())
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = handle_message(user_input)
    print("Bot:", response)
