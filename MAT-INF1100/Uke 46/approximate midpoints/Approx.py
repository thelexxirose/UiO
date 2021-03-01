class Approx:
    def __init__(self, function, interval):
        self.f = function
        self.i = interval

    def approximate(self):
        a = self.i[0]
        b = self.i[1]
        e = 2**-6
        iterations = 0
        while abs(a - b) > e:
            m = (a+b)/2
            iterations += 1
            if self.f(a) * self.f(m) < 0:
                b = m
            elif self.f(b) * self.f(m) < 0:
                a = m
            else:
                a, b = m

        return (a + b)/2, iterations
