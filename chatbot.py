print("================================")
print("       WELCOME TO CHAT BOX      ")
print("================================")
print("Type 'hello', 'how are you', or 'bye' to chat.")
print("Type 'bye' to exit the chat.\n")

while True:
    message = input("You: ").lower().strip()

    if message == "hello":
        print("Bot: Hi!")

    elif message == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif message == "how are you":
        print("Bot: I'm fine, thanks!")

    elif message == "what is your name":
        print("Bot: I'm Smart Buddy, your chatbot!")

    elif message == "how is your day":
        print("Bot: My day is going great! Thanks for asking.")

    elif message == "help":
        print("Bot: You can say hello, ask how I am,")
        print("     ask my name, or say bye.")

    elif message == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that message.")

    