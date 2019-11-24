from random import random


pi = 0
for i in range(1000000):
    if random() ** 2 + random() ** 2 <= 1:
        pi += 1
print(pi / 1000000 * 4)
