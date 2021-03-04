import math


def recursiveForm(n, current, previous):
    if n == 0:
        return previous
    elif n == 1:
        return current
    else:
        newCurrent = 4*current + previous
        newPrevious = current
        # print(f"n {n:<3}: newCurrent = {newCurrent}, newPrevious = {newPrevious}")
        return recursiveForm(n-1, newCurrent, newPrevious)


def analyticForm(n):
    return (2-math.sqrt(5))**n


def bruteForceForm(n, multiplier):
    product = 1
    for i in range(0, n):
        product = product*multiplier
    return product


n = 100
x0 = 1
x1 = 2-math.sqrt(5)
print("*************************\n")
print("recursive versus analytic\n")
print("*************************\n")
while(n >= 0):
    recursive = recursiveForm(n, x1, x0)
    analytic = analyticForm(n)
    print(f"{n:<3}: {recursive:>65} <=> {analytic:>25}: delta = {(recursive - analytic):>25}")
    n = n-1

n = 100
print("*************************\n")
print("brute force versus analytic\n")
print("***************************\n")
while(n >= 0):
    bruteForce = bruteForceForm(n, x1)
    analytic = analyticForm(n)
    print(f"{n:<3}: {bruteForce:>65} <=> {analytic:>25}: delta = {(bruteForce - analytic):>25}")
    n = n-1
