import art
from caesar import caesar

# Main program execution
if __name__ == "__main__":

    print(art.logo)
    dir = input("Type 'encrypt (e)' to encrypt, type 'decrypt (d)' to decrypt:\n")
    txt = input("Type your message:\n")
    shft = int(input("Type the shift number:\n"))

    caesar(dir, txt, shft)
