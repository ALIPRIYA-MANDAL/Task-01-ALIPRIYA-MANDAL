# Dictionary containing chatbot responses
print("Welcome to the chatbot!")
# Ask User for their name
name=input("Enter Your Name:")
print(f"Hello {name}!I am Chatbot.\n")
responses={
    "hello": "HI there!",
    "hi": "Hello",
    "How are you":"I am doing great",
    "what is your name":"I am a chatbot",
    "what is ai":"AI stands for Artificial Intelligence",
    "who are you":"I am a rulle-based chatbot",
    "help":"I can answer basic questions",
    "thanks":"You are welcome!"

}
#Main Chatbot Loop
while True:
    user_input=input("You: ").lower().strip()
    user_input = user_input.replace("?", "")
    user_input = user_input.replace("!", "")
    user_input = user_input.replace(".", "")
    if user_input in["bye","exit","quit"]:
        print("Bot:Goodbye!")
        break
    response=responses.get(user_input,"Sorry I dont understand that.")
    print("Bot:",response)