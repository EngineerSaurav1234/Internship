def respond(user_input):
    
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input or "what's up" in user_input:
        return "I'm doing great, thanks! How about you?"
    elif "what's your name" in user_input or "who are you" in user_input:
        return "I'm Saurav's AI, your friendly chatbot!"
    elif "goodbye" in user_input or "bye" in user_input or "see you" in user_input:
        return "It was nice chatting with you! Have a great day!"
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        return "The current time is " + now.strftime("%H:%M:%S")
    elif "date" in user_input:
        from datetime import datetime
        now = datetime.now()
        return "Today's date is " + now.strftime("%d/%m/%Y")
    else:
        return "I didn't understand that. Can you please rephrase?"

while True:
    user_input = input("You: ")
    response = respond(user_input)
    print("Saurav Chatbot:", response)