import art
from caesar import caesar

# Main program execution
if __name__ == "__main__":

    print(art.logo)

    is_running = True

    while is_running:
        dir = input("Type 'encrypt (e)' to encrypt, type 'decrypt (d)' to decrypt:\n")
        txt = input("Type your message:\n")
        shft = int(input("Type the shift number:\n"))

        caesar(dir, txt, shft)

        print("\nDo you want to go again?")
        user_choice = input("Type 'no (n)' to stop, any other input will be interpreted as 'yes'.\n").lower()
        if user_choice == 'no' or user_choice == 'n':
            is_running = False
            print("\nGoodbye!")

        print() # Print a newline for better readability between runs
