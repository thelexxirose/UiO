def f(x,y):
    func_1 = lambda x,y: 4*x**3*y - 2*x*y
    func_2 = lambda x,y: 4*x**3*y + 2*x*y

    l = []
    for i in y:
        if i <= 0:
            l.append(func_1(x,y))
        else:
            l.append(func_2(x,y))

    return l