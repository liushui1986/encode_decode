from flask import Flask, render_template, request
from art import logo

app = Flask(__name__)

alphabet = [alph for alph in 'abcdefghijklmnopqrstuvwxyz']
numbers = [num for num in '0123456789']
punctuations = [punc for punc in ' !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~']

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
    return output_text

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        direction = request.form.get("direction").lower()
        text = request.form.get("text").lower()
        shift = int(request.form.get("shift"))
        result = caesar(text, shift, direction)
        return render_template("index.html", logo=logo, result=result, direction=direction)
    return render_template("index.html", logo=logo, result=None)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
