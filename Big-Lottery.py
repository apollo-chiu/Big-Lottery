import random

i = 1
section1 = []
while i <= 7:
    r = random.randint(1, 49)
    if r in section1:
    	continue

    section1.append(r)
    i += 1


section1.sort()

print(section1)
