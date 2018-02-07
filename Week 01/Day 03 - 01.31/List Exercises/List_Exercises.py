# List Exercises
# Below are my solutions to the exercises.

# === Sum the Numbers ===
import math
numbers = [-100, 1, 3, math.pi, 5, 10, 30, 50.75]

sum = 0
for number in numbers:
    sum += number

print(sum)


# === Largest Number ===
import math
numbers = [-100, 1, 3, math.pi, 5, 10, 30, 50.75]

largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number

print(largest)


# === Smallest Number ===
import math
numbers = [-100, 1, 3, math.pi, 5, 10, 30, 50.75]

smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number

print(smallest)


# === Even Numbers ===
import math
numbers = [-100, 1, 3, math.pi, 5, 10, 30, 50.75]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)


# === Positive Numbers ===
import math
numbers = [-100, 1, 3, math.pi, 5, 10, 30, 50.75]

positives = []
for number in numbers:
    if number > 0:
        print(number)


# === Positive Numbers II ===
import math
numbers = [-100, 1, 3, math.pi, 5, 10, 30, 50.75]

positives = []
for number in numbers:
    if number > 0:
        positives.append(number)

print(positives)


# === Multiply a List ===
import math
numbers = [-100, 1, 3, math.pi, 5, 10, 30, 50.75]
factor = 2

product = []
for number in numbers:
    product.append(number * factor)

print(product)


# === Multiply Vectors ===
vector1 = [4, -1, 0, -5]
vector2 = [8, 3, 3, -2]

product = []
for i in range(len(vector1)):
    product.append(vector1[i] * vector2[i])

print(product)


# === Matrix Addition ===
matrix1 = [
    [2, -2],
    [5, 3]
]
matrix2 = [
    [5, 2],
    [1, 0]
]

height = len(matrix1)
width = len(matrix1[0])

result = []

for i in range(0, height):
    result.append([])
    for j in range(0, width):
        result[i].append(None)

for i in range(0, height):
    for j in range(0, width):
        cell1 = matrix1[i][j]
        cell2 = matrix2[i][j]

        result[i][j] = cell1 + cell2

print(result)


# === Matrix Addition II ===
matrix1 = [
    [2, -2, 4],
    [5, 3, 7]
]
matrix2 = [
    [5, 2, -1],
    [1, 0, 9]
]

height = len(matrix1)
width = len(matrix1[0])

result = []

for i in range(0, height):
    result.append([])
    for j in range(0, width):
        result[i].append(None)

for i in range(0, height):
    for j in range(0, width):
        cell1 = matrix1[i][j]
        cell2 = matrix2[i][j]

        result[i][j] = cell1 + cell2

print(result)


# === De-dup ===
items = ['desk', 'paper', 'pen', 'pencil', 'desk', 'paperclip', 'paper', 'notepad']

deduped = []
for item in items:
    if item not in deduped:
        deduped.append(item)

print(deduped)


# === Bonus: Matrix Multiplication ===

