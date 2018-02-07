# String Exercises
# Below are my solutions to the exercises.

# === Uppercase a String ===
string = "ThIS is A sTrINg."
print(string.upper())


# === Capitalize a String ===
string = "ThIS is A sTrINg."
print(string.capitalize())


# === Reverse a String ===
# ':' is used to skip needed values e.g. begin and end values.
string = "ThIS is A sTrINg."
print(string[::-1])


# === Leetspeak ===
leetspeak = {
    "A" : "4",
    "E" : "3",
    "G" : "6",
    "I" : "1",
    "O" : "0",
    "S" : "5",
    "T" : "7"
}

input_string = input("Enter string: ").upper()
output_string = ""

for i in range(0, len(input_string)):
    if input_string[i] in leetspeak:
        output_string += leetspeak[input_string[i]]
    else:
        output_string += input_string[i]
print(output_string)


# === Caesar Cipher ===
import string
alphabet = list(string.ascii_lowercase)

def prompt_message():
    message = input("Enter the message to be encrypted: ").lower()
    return message

def prompt_key():
    key = abs(int(input("Enter number to shift by: ")))
    key = key % len(alphabet)
    return key

def caesar_encrypt(msg, key):
    msg_list = list(msg)
    new_list = []
    for letter in msg_list:
        if letter == ' ':
            new_list.append(letter)
        else:
            new_char = alphabet[alphabet.index(letter) - key]
            new_list.append(new_char)
    new_message = ''.join(new_list)
    return new_message

print("Welcome to the Caesar Cypher, you will be prompted for a message and a key.")
msg = prompt_message()
key = prompt_key()
print(caesar_encrypt(msg, key))