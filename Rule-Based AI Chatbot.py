def chatbot():
    print("🤖 Chatbot Started (type 'bye' to exit)")

    while True:
        user = input("You: ").lower()

        if "hello" in user:
            print("Bot: Hello Shiv!")
        elif "cyber security" in user:
            print("Bot: Cybersecurity protects systems from attacks.")
        elif "blockchain" in user:
            print("Bot: Blockchain is a decentralized ledger.")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()