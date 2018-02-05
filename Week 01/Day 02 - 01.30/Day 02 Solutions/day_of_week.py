# Below is the instructor's proposed solution.

# configuration
day_prompt = 'Day (0-6)? '
day = -1 # 0 is Sunday, 6 is Saturday, -1 is not valid
day_name = '' #setting to blank string for now

# processing
day = int(input(day_prompt))

if day == 0:
    day_name = 'Sunday'
elif day == 1:
    day_name = 'Monday'
elif day == 2:
    day_name = 'Tuesday'
elif day == 3:
    day_name = 'Wednesday'
elif day == 4:
    day_name = 'Thursday'
elif day == 5:
    day_name = 'Friday'
elif day == 6:
    day_name = 'Saturday'
else:
    day_name = 'Try again. %d is not valid' % day

# result
print(day_name)