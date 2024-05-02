import random

def greet():
    responses = ["Hello! How can I assist you today?",
                "Hi! How can I help you?",
                 "Welcome! How may I assist you with your flight?"]
    return random.choice(responses)

def get_flight_status(flight):
    if flight == "ABC123":
        return "The flight ABC is on time"
    elif flight == "XYZ789":
        return "The flight XYZ is delayed by 30 minutes"
    else:
        return "I am sorry couldn't find info for that flight."

def handle_message(message):
    if message.lower() == "hi" or message.lower() == "hello":
        return greet()
    elif "flight status" in message.lower():
        words = message.split()
        for word in words:
            if word.isalnum() and word.isupper() and len(word) == 6:
                return get_flight_status(word)
        return "Please provide a valid flight number"
    else:
        return "I am sorry, I cannot understand your query, please repeat?"


print(greet())
while True:
    user_input = input("You:")
    if user_input.lower() == "exit":
        print("Ciao!")
        break
    response = handle_message(user_input)
    print("Bot:", response)
