# Below is the instructor's proposed solution.

# configuration
day_prompt = 'Day (0-6)? '
day = -1  # 0 is sunday, 6 is saturday, -1 is not valid
message = 'Go to work'

# processing
day = int(raw_input(day_prompt))

is_weekend = ((day == 0) or (day == 6))

if is_weekend:
  message = 'Sleep in'
elif 0 < day < 6:
  message = 'Go to work'
else:
  message = 'Try again. %d is not valid' % day


# result
print message