import aiml

# User Test Case
# (User Input) Enter your Name: Musa
# (User Input) Enter Message: hello
# (Bot Response) Well, hello! Musa
# (User Input) Enter Message: how are you
# (Bot Response) I am fine thank you!
# (User Input) Enter Message: what is your name
# (Bot Response) My name is Test.
# (User Input) Enter Message: what are you
# (Bot Response) I'm a bot, silly!
# (User Input) Enter Message: bye
# (Bot Response) Bye Musa, It was fun talking to you!


def python_aiml():
    # Creating aiml object and connecting it with aiml file
    kernel = aiml.Kernel()
    kernel.learn("test.aiml")

    # Take user name from user
    user_name = input("Enter your Name: ")

    # Store the user name in a variable
    # setPredicate method is equivalent to set tag of aiml
    kernel.setPredicate("username", user_name)

    # Taking user input and giving replies according to aiml file
    while True:
        # Take user input
        user_input = input("Enter Message: ")

        # Enter quit or bye to exit program
        if user_input == "quit" or user_input == "bye":
            print(kernel.respond("bye"))
            exit()
        elif user_input == "what is my name":
            # getPredicate method is equivalent to get tag of aiml
            print(kernel.getPredicate("username"))
        else:
            # respond method is a built-in method of aiml library
            # It is used to give back the template answer of the chatbot
            # according to the input pattern
            print(kernel.respond(user_input))


# Main function
def main():
    python_aiml()


# Calling main function
if __name__ == "__main__":
    main()
