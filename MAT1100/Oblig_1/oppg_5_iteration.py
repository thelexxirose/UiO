def equation(n):
    if (n <= 1):
        return 1
    else:
        return 2 + (3/4)*equation(n-1)


for i in range(100):
    print(f"n = {i} : {equation(i)}")
