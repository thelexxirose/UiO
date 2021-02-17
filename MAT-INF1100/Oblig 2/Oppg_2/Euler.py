import matplotlib.pyplot as plt

class Euler:
    def __init__(self, x, y, y_prime):
        self.x = x
        self.y = y
        self.y_prime = y_prime

    def plot(self, method, interval, steps, return_arr=False):
        if method == "forward euler":
            arr = self.forward_euler(interval, steps)
        elif method == "midpoint euler":
            arr = self.midpoint_euler(interval, steps)
        else:
            raise Exception(f"{method} is not a valid method")
        plt.plot(arr[0], arr[1], label=method)
        if return_arr:
            return arr


    def forward_euler(self, interval, steps):
        plot_arr = [
            [self.x],
            [self.y]
        ]
        h = (interval[1]-interval[0])/steps
        for i in range(0, steps):
            plot_arr[0].append((i+1)*h)
            plot_arr[1].append(plot_arr[1][i] + self.y_prime(plot_arr[0][i], plot_arr[1][i])*h)

        return plot_arr

    def midpoint_euler(self, interval, steps):
        plot_arr = [
            [self.x],
            [self.y]
        ]
        h = (interval[1]-interval[0])/steps
        for i in range(0, steps):
            k_1 = self.y_prime(plot_arr[0][i], plot_arr[1][i])
            k_2 = self.y_prime(plot_arr[0][i] + (h/2), plot_arr[1][i] + (h/2)*k_1)
            plot_arr[1].append(plot_arr[1][i] + k_2*h)
            plot_arr[0].append((i+1)*h)

        return plot_arr
        
