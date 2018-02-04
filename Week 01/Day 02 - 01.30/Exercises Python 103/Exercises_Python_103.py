# Exercises - Python 103
# Below are my solutions to the exercises.

# # === Day of the Week ===
day = int(input('Day (0-6)? '))
list_of_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"It's {list_of_days[day]}.")


# # === Work or Sleep In? ====
day = int(input('Day (0-6)? '))
list_of_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if day == 0 or day == 6:
    print(f"It's {list_of_days[day]}, hit snooze.")
elif 0 < day < 6:
    print(f"It's {list_of_days[day]}, don't be a bum. Go to work!")


# # === Celsius to Fahrenheit ===
c = int(input("Temperature in C? "))
f = c * 1.8 + 32
print((f"Here in \'Murica, that\'s {f} F."))


# === Tip Calculator ===
total_bill = int(input("Total bill amount? "))
service_level = input("Level of service: good, fair, bad? ")
if service_level == "good":
    service_level = .20
elif service_level == "fair":
    service_level = .15
elif service_level == "bad":
    service_level = .1
tip = total_bill * service_level
total_amount = total_bill + tip
print("Tip amount: $%.2f" % tip)
print("Total amount: $%.2f" % total_amount)


# === Tip Calculator 2 ===
total_bill = int(input("Total bill amount? "))
service_level = input("Level of service: good, fair, bad? ")
split = int(input("Split how many ways? "))
if service_level == "good":
    service_level = .20
elif service_level == "fair":
    service_level = .15
elif service_level == "bad":
    service_level = .1
tip = total_bill * service_level
total_amount = total_bill + tip
per_person = total_amount / split

print("Tip amount: $%.2f" % tip)
print("Total amount: $%.2f" % total_amount)
print("Amount per person: $%.2f" % per_person)