import base64
from pathlib import Path

def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def encode(text, key):
    xor_result = xor_cipher(text, key)
    return base64.b64encode(xor_result.encode()).decode()

pass_phrase_file = Path("third_file.txt")

if pass_phrase_file.is_file():
    name_key = input("What is your name? ")

    with open(pass_phrase_file) as f:
        pass_phrase = f.read()
    pass_phrase = base64.b64decode(pass_phrase).decode('utf-8')
    encoded = encode(pass_phrase, name_key)

    print("Your personal pass phrase is:", encoded)
else:
    print("The pass phrase file does not yet exist. Please continue working on the course.")
