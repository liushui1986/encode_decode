# Import and print the logo from art.py when the program starts.
import string
from art import logo
print(logo)

alphabet = [alph for alph in string.ascii_lowercase]
numbers = [num for num in string.digits]
punctuations = [punc for punc in string.punctuation]


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for char in original_text:
        if char in alphabet:
            output_text += alphabet[(alphabet.index(char) + shift_amount) % len(alphabet)]
        elif char in numbers:
            output_text += numbers[(numbers.index(char) - shift_amount) % len(numbers)]
        elif char in punctuations:
            output_text += punctuations[(punctuations.index(char) - shift_amount) % len(punctuations)]
        else:
            output_text += char
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
restart = 'y'
while restart == 'y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Do you want to restart? ('Y/N')").lower()
    if restart == 'n':
        print('Goodbye!')
