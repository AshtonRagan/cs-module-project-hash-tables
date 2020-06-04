# Your code here
import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    return v


def new_func(v):
    v %= 982451653
    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    key = (x, y)
    d = {}
    p = {}
    v = math.pow(x, y)

    if v not in d:
        d[v] = math.factorial(v)

    q = d[v]
    q //= (x+y)
    q %= 982451653
    return q

    # if key not in d:
    #     d[key] = slowfun_too_slow(x, y)
    # return d[key]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
