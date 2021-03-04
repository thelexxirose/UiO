import math


def recursiveForm(n, current, previous):
    if n == 0:
        return previous
    elif n == 1:
        return current
    else:
        newCurrent = 4*current + previous
        newPrevious = current
        return recursiveForm(n-1, newCurrent, newPrevious)


def analyticForm(n):
    return (2-math.sqrt(5))**n


n = 100
x0 = 1
x1 = 2-math.sqrt(5)
while(n > 0):
    recursive = recursiveForm(n, x1, x0)
    analytic = analyticForm(n)
    print(f"{n:<3}: {recursive:>65} <=> {analytic:>25}: delta = {(recursive - analytic):>25}")
    n = n-1
