import random

responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?"],
    "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
    "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?"]
}

class Samble_Chatbot:
    def __init__(self, user_input=""):
        self.user_input = user_input.lower()  
        
    def get_response(self):
        for key in responses:
            if key in self.user_input:
                return random.choice(responses[key])
        return random.choice(responses["default"])
    
    
    def chatbot(self):
        print("Chatbot: Hi! How can I assist you today?")
        
        while True:
            self.user_input = input("User: ").lower() 
            response = self.get_response()  
            print("Chatbot:", response)
            
            if "goodbye" in self.user_input:  
                break


c = Samble_Chatbot()
c.chatbot()

