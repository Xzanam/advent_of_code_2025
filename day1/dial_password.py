import sys
import math

count = 0
total = 50

for line in sys.stdin:
    line = line.rstrip("\n")
    if not line:
        continue

    if line[0] == 'R':
        num = int(line[1:])
        t = (100 - total) % 100
        if t == 0:
            t = 100

        if t <= num:
            count += 1 + (num - t)//100

        total = (total + num) % 100

    elif line[0] == 'L':
        num = int(line[1:])

        t = total % 100
        if t == 0:
            t = 100

        if t <= num:
            count += 1 + (num - t)//100

        total = (total - num) % 100

print(count)
