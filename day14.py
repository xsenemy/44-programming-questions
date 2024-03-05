#44 Programming questions Code
#Very easy questions:
#14) You are given an integer in the range of 0-10000, representing time in seconds. Convert it to time in the format of "HH:mm:ss".

import random


time = int(input("Insert seconds (0-10000): "))
# time = random.randint(0, 10000)
seconds = 0
minutes = 0
hours = 0
for i in range(time):
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
print(f"Time in seconds: {time}")
print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
