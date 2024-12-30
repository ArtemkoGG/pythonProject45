import random

def random_num(min, max, n: int):
    for i in range(n):
        yield int(min + (max - min) * random.random())

for number in random_num(3, 10, 21):
    print(number)
