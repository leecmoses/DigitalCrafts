# Exercises - Python 105
# Below are my solutions to the exercises.

# === 1 to 10 ===
for i in range(1,11):
    print(i)


# === n to m ===
start = int(input("Start from: "))
end = int(input("End on: "))
if start < end:
    for i in range(start, end + 1):
        print(i)
else:
    print("Start number must be less than end number. ")


# === Odd Numbers ===
for i in range(1, 11):
    if i % 2 != 0:
        odd = i
        print(odd)
    else:
        even = i


# ==== How many coins? ===
coin_count = 0

print(f"You have {coin_count} coins.")
response = input("Do you want a coin? ").lower()

while True:
    if response == "yes" and coin_count < 1:
        coin_count += 1
        print(f"You have {coin_count} coin.")
        response = input("Do you want another coin? ").lower()
    elif response == "yes" and coin_count >=1:
        coin_count += 1
        print(f"You have {coin_count} coins.")
        response = input("Do you want another coin? ").lower()
    else:
        print("Farewell.")
        break


# === Print a Square ===
size = 5
for i in range(size):
    print('*' * size)


# === Print a Square II ===
size = int(input("How big is the square? "))
for i in range(size):
    print('*' * size)


# === Print a Box ===
width = int(input("Width? "))
height = int(input("Height? "))
spaces = width - 2

print('*' * width)
for i in range(0, height - 2):
    print('*' + ' ' * spaces + '*')
print('*' * width)


# === Print a Triangle ===
height = 4
for i in range(height):
    print(' ' * (height - i - 1) + '*' * (2 * i + 1))


# === Print a Triangle II ===
height = int(input("Enter height: "))
for i in range(height):
    print(' ' * (height - i - 1) + '*' * (2 * i + 1))


# === Multiplication Table ===
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")


=== Bonus: Print a Banner ===
message = input("Message: ")
width = len(message) + 2

print('*' * width)
print('*' + message + '*')
print('*' * width)


# === Bonus: Triangle Numbers ===
for num in range(1, 101):
    result = num * (num + 1) // 2
    print(result)


# === Bonus: Factor a Number ===
num = int(input("Number: "))
i = 1

print(f"==== Factors of {num} =====")
while i <= num:
    if num % i == 0:
        print(i)
    i += 1 