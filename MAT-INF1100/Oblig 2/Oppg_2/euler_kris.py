import matplotlib.pyplot as plt


def dydx(x, y):
    return 0.01*(y**2)-9.81


def euler(x, y, deltaX, N):
    xListe = [x]
    yListe = [y]

    for i in range(N):
        y = y + dydx(x, y)*deltaX
        x = x + deltaX
        xListe.append(x)
        yListe.append(y)

    a = [xListe, yListe]
    return a


m = euler(0, 0, 0.1, 1000)
plt.plot(m[0], m[1])
plt.show()
