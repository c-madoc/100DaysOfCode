from itertools import cycle

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']



def encrypt(text: str, shift: int):
    encrypted_text = ""

    # for each letter in the given text
    for letter in text.lower():
        letter_position = alphabet.index(letter)
        new_position = letter_position + shift

        while new_position > 25:
            new_position -= 26
        encrypted_text += alphabet[new_position]

    print(f"Encrypted: {encrypted_text}")

def decrypt(text: str, shift: int):
    decrypted_text = ""

    # for each letter in the given text
    for letter in text.lower():
        letter_position = alphabet.index(letter)
        new_position = letter_position - shift

        while new_position < 0:
            new_position += 26
        decrypted_text += alphabet[new_position]

    print(f"Encrypted: {decrypted_text}")


if __name__ == "__main__":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction.lower() == "encode":
        encrypt(text, shift)

    if direction.lower() == "decode":
        decrypt(text, shift)

