def binomial_coefficient(n, i):
    p = 1
    i = min(i, n-i)
    for j in range(1, i + 1):
        p *= (n - j + 1)/j
    return p


print(f"n =   5000, i =     4 ==> {binomial_coefficient(5000, 4)}")
print(f"n =   1000, i =  5000 ==> {binomial_coefficient(1000, 500)}")
print(f"n = 100000, i = 99940 ==> {binomial_coefficient(100000, 99940)}")
