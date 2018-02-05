# Below is the instructor's proposed solution.

# configuration
day_prompt = 'Day (0-6)? '
day = -1 # 0 is Sunday, 6 is Saturday, -1 is not valid
message = 'Go to work'
day_name = '' # setting to blank string for now

# processing
day = int(input(day_prompt))

debug_bool = ((day == 0) or (day == 6))
print(debug_bool)
if debug_bool:
    message = 'sleep in'
elif 0 < day < 6:
    message = 'Go to work'
else:
    message = 'Try again. %d is not valid' % day

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

# result
print("It's %s you should %s" % (day_name, message))