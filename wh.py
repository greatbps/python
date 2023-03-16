import time
number = 0
t_tick = time.time() + 5
while time.time() < t_tick:
    number += 1

print(number)