def encrypt(original_text, shift_amount):
    """
    Encrypts the original_text using a Caesar cipher with the given shift_amount.
    """

    encrypted_text = ""
    # For each character in the original text, shift it by shift_amount
    for char in original_text:
        # symbols are not changed
        if char.isalpha():
            # Determine the base ASCII code for uppercase or lowercase letters
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character starting from 0 to 25 and wrap around using modulo 26
            # then add the base back to get the new character
            encrypted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    print(f"Encrypted Text: {encrypted_text}")


def decrypt(encrypted_text, shift_amount):
    """
    Decrypts the encrypted_text using a Caesar cipher with the given shift_amount.
    """

    decrypted_text = ""
    # For each character in the encrypted text, shift it back by shift_amount
    for char in encrypted_text:
        # symbols are not changed
        if char.isalpha():
            # Determine the base ASCII code for uppercase or lowercase letters
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character back starting from 0 to 25 and wrap around using modulo 26
            # then add the base back to get the new character
            decrypted_char = chr((ord(char) - base - shift_amount) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    print(f"Decrypted Text: {decrypted_text}")


def caesar(direction, text, shift):
    """
    Main function to handle encryption and decryption based on direction.
    """

    direction_lower = direction.lower()

    if direction_lower == "encrypt" or direction_lower == "e":
        encrypt(text, shift)
    elif direction_lower == "decrypt" or direction_lower == "d":
        decrypt(text, shift)
    else:
        print("Invalid direction! Use 'encrypt (e)' or 'decrypt (d)'.")