def binomial_coefficient(n, i):
    p = 1
    for j in range(1, i + 1):
        p *= (n - j + 1)/j
    return p


for n in range(1, 2001):
    find = False
    for i in range(1, n+1):
        if binomial_coefficient(n, i) == float("Inf"):
            print(f"{n} choose {i} gives inf")
            find = True
            break
    if find:
        break
