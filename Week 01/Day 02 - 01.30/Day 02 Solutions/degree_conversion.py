# Below is the instructor's proposed solution.

celsius_prompt = 'Temperature in C? '
f_temp = 0
c_temp = 0

c_temp = float(input(celsius_prompt))
f_temp = c_temp * 1.8 + 32

print("%.1f F" % f_temp)