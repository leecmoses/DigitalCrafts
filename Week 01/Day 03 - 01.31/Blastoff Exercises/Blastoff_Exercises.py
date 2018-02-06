# Bonus Exercises Python 105
# Below are my solutions to the exercises.

# === Blastoff ===
for i in range(10, -1, -1):
    print(i)


# === Blastoff 2 ===
for i in range(10, -1, -1):
    print(i)
    if i == 0:
        print("Blast off!")
    else:
        pass


# === Blastoff 3 ===
countdown = int(input("Enter countdown number: "))
for i in range(countdown, -1, -1):
    print(i)
    if i == 0:
        print("Blast off!")
    else:
        pass


# ===Blastoff 4 ===
from time import sleep
countdown = int(input("Enter countdown number: "))
for i in range(countdown, -1, -1):
    if countdown <= 20:
        sleep(1)
        print(i)
        if i == 0:
            print("Blast off!")
    else:
        countdown = int(input("Enter a number less than or equal to 20 and greater than 0: "))

