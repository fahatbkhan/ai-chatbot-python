import re
import random
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["Hello!", "Hi there!", "Hey! How can I help you?"]
    how_are_you = ["I'm doing great!", "All good here!", "I'm fine, thanks!"]

    if re.search(r"hi|hello|hey", user_input):
        return random.choice(greetings)
    
    elif "time" in user_input:
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}"
    
    elif "date" in user_input:
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"
    
    elif "your name" in user_input:
        return "I am a Python chatbot created by Fahat."
    
    elif "how are you" in user_input:
        return random.choice(how_are_you)
    
    elif "python" in user_input:
        return "Python is widely used in AI, web development, and automation."
    
    elif "project" in user_input:
        return "I can help explain your projects like AI Drone, ESP32 IoT, and RPA automation."
    
    elif re.search(r"bye|exit|quit", user_input):
        return "Goodbye! Have a great day!"
    
    else:
        return "Sorry, I didn't understand that. Try asking something else."

print("Chatbot: Hello! Type 'exit' to end the chat.")

while True:
    user = input("You: ")
    
    if user.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    
    response = chatbot_response(user)
    print("Chatbot:", response)