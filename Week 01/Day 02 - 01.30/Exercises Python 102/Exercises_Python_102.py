# Exercises - Python 102
# Below are my solutions to the exercises. Run code by individual sections!

# === Hello, you! ===
print('What is your name?')
name = input('> ')
print('Hello, {}!'.format(name))


# === HELLO, YOU! ====
print('WHAT IS YOUR NAME?')
name = input('> ').upper()
print(f"HELLO, {name}!")
letters = len(name.replace(' ', ''))
print(f"YOUR NAME HAS {letters} IN IT! AWESOME!")


# === Madlib ===
# Solution #1
print("Please fill in the blanks below:")
print(" __(Name)__'s favorite subject in school is __(Subject)__.")
name = input("What is name? ")
subject = input("What is subject? ")
print("{}'s favorite subject in school is {}.".format(name, subject))


# Solution #2
'''
My comments:
The solution above may be shorter in length. 
However, it is important to considert the user interface, too. 
Some may prefer the solution below because it prompts the user for an answer on a new line.
'''

print("Please fill in the blanks below:")
print(" __(Name)__'s favorite subject in school is __(Subject)__.")
print("What is name?")
name = input('> ')
print("What is subject?")
subject = input('> ')
print(f"{name}'s favorite subject in school is {subject}.")