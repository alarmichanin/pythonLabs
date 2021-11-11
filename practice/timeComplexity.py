import os
import random
from timeit import timeit

path = "./text2.txt"
with open("text2.txt", "w") as file:
    while os.path.getsize(path) < 52428800:
        file.write(str(random.randint(0, 999999999)) + "\n")

k = """
with open("text2.txt") as file:
    s = 0
    lines = file.readlines()
    for line in lines:
        if line.strip().isdigit():
            s += int(line.strip())
"""
print(timeit(k, number=20) / 20)

k = """
with open("text2.txt") as file:
    s = 0
    for line in file:
        if line.strip().isdigit():
            s += int(line.strip())
"""

print(timeit(k, number=20) / 20)

k = """
with open("text2.txt") as file:
    s = 0
    n = (int(i.strip()) for i in file if i.strip().isdigit())
    s = sum(n)
"""
print(timeit(k, number=20) / 20)
