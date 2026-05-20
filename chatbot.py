while True:
    user_input = input("You: ")

    if "hello" in user_input:
        print("Bot: Hi there!")

    elif "how are you" in user_input:
        print("Bot: I am fine, thank you!")

    elif "your name" in user_input:
        print("Bot: My name is RuleBot!")

    elif "joke" in user_input:
        print("Bot: Why do programmers hate nature? Too many bugs!")

    elif "bye" in user_input:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I did not understand that.")
