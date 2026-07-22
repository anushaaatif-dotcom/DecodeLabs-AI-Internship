# ============================================
# Rule-Based AI Chatbot
# Project 1 - DecodeLabs AI Internship
# Created by: Syeda Anusha Aatif
# ============================================

print("=" * 60)
print("        Welcome to the Rule-Based AI Chatbot")
print("=" * 60)
print("Hello! I am your chatbot.")
print("Type 'bye', 'exit', or 'quit' anytime to end the chat.")
print()

# Continuous loop
while True:

    # Take user input
    user = input("You: ").strip().lower()

    # Greetings
    if user in ["hi", "hello", "hey", "good morning", "good evening"]:
        print("Bot: Hello! Nice to meet you.")

    # Asking chatbot name
    elif user in ["what is your name", "who are you", "your name"]:
        print("Bot: My name is RuleBot. I am a Rule-Based AI Chatbot.")

    # Asking how are you
    elif user == "how are you":
        print("Bot: I am doing great. Thank you for asking!")

    # Asking creator
    elif user in ["who made you", "who created you"]:
        print("Bot: I was created by Syeda Anusha Aatif using Python.")

    # Help
    elif user == "help":
        print("Bot: I can respond to the following commands:")
        print("     - hello")
        print("     - how are you")
        print("     - what is your name")
        print("     - who made you")
        print("     - tell me a joke")
        print("     - what can you do")
        print("     - thank you")
        print("     - bye")

    # Joke
    elif user == "tell me a joke":
        print("Bot: Why do programmers prefer Python?")
        print("     Because it's easy to understand and has fewer bugs!")

    # Favourite color
    elif user == "what is your favorite color":
        print("Bot: My favorite color is Blue.")

    # Weather
    elif user == "weather":
        print("Bot: Sorry, I cannot check live weather yet.")

    # Thank you
    elif user in ["thanks", "thank you"]:
        print("Bot: You're welcome!")

    # What can you do
    elif user == "what can you do":
        print("Bot: I can chat with you using predefined rules.")
        print("     I answer greetings and simple questions.")

    # AI meaning
    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")
        print("     It enables machines to perform tasks that normally require human intelligence.")

    # Time
    elif user == "time":
        print("Bot: Sorry, I cannot tell the current time in this version.")

    # Date
    elif user == "date":
        print("Bot: Sorry, I cannot tell today's date in this version.")

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day.")
        break

    # Empty input
    elif user == "":
        print("Bot: Please type something.")

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")
        print("     Type 'help' to see the available commands.")

print("\nChat ended successfully.")