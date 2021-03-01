import matplotlib.pyplot as plt


class Distance:
    def __init__(self, x_arr, y_arr):
        self.x_arr = x_arr
        self.y_arr = y_arr
        self.d_arr = []

    def plot_trapezoid(self, img_name, s_0=0):
        s = s_0
        for i in range(len(self.x_arr)-1):
            s += (self.x_arr[i+1] - self.x_arr[i]) * ((self.y_arr[i+1] + self.y_arr[i])/2)
            self.d_arr.append(s)

        fig = plt.figure()
        fig.patch.set_facecolor('#cccccc')
        plt.plot(self.x_arr[:-1], self.d_arr)
        plt.xlabel("time(s)")
        plt.ylabel("distance(m)")
        plt.title("Distance")
        plt.savefig(img_name, facecolor=fig.get_facecolor(), edgecolor='none')
        # plt.show()
