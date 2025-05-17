print("Hello! I am a simple chatbot. Ask me something (type 'bye' to exit).")

while True:
    user_input = input("You: ").lower()

    if "name" in user_input:
        print("Bot: My name is ChatGPT-Lite!")
    elif "your job" in user_input or "what do you do" in user_input:
        print("Bot: I answer your questions.")
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: I don't understand that. Can you ask something else?")
