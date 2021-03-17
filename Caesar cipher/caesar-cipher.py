import chars
import art

print(art.logo)

alphabet = chars.alphabet

def encrypt(text, shift):
    shift = shift % 26
    encrypted_message = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position >= len(alphabet):
            # We are making another loop with the same range:
            new_position_out_of_range = alphabet.index('a') + (new_position - len(alphabet))
            new_letter = alphabet[new_position_out_of_range]
        else:
            new_letter = alphabet[new_position]
        encrypted_message += new_letter
    print(f'Encoded text is: {encrypted_message}')


def decrypt(text, shift):
    shift = shift % 26
    decrypted_message = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        if new_position < 0:
            new_letter = alphabet[new_position + len(alphabet)]
        else:
            new_letter = alphabet[new_position]
        decrypted_message += new_letter
    print(f'Decrypted text is: {decrypted_message}')


game_end = False

while not game_end:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt or 'exit' for exit:\n")
    if direction == 'encode':
        encrypt(text=input("Type your message:\n").lower(), shift=int(input("Type the shift number:\n")))
    elif direction == 'decode':
        decrypt(text=input("Type your message:\n").lower(), shift=int(input("Type the shift number:\n")))
    elif direction == 'exit':
        game_end = True
        print("Good bye!")
    else:
        print('Please, try to choose again.')


