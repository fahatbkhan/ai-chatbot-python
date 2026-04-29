import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r"hi|hello|hey", user_input):
        return "Hello! How can I help you today?"
    
    elif re.search(r"your name", user_input):
        return "I am a simple AI chatbot created using Python."
    
    elif re.search(r"how are you", user_input):
        return "I'm doing great! Thanks for asking."
    
    elif re.search(r"bye|exit|quit", user_input):
        return "Goodbye! Have a nice day."
    
    elif re.search(r"python", user_input):
        return "Python is a powerful programming language used in AI, web development, and automation."
    
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

print("Chatbot: Hello! Type 'exit' to end the chat.")

while True:
    user = input("You: ")
    
    if user.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    
    response = chatbot_response(user)
    print("Chatbot:", response)