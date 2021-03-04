import matplotlib.pyplot as plt


class Accel:
    def __init__(self, x_arr, y_arr):
        self.x_arr = x_arr
        self.y_arr = y_arr
        self.a_arr = []

    def plot(self, img_name):
        for idx in range(len(self.x_arr)-1):
            self.a_arr.append((self.y_arr[idx + 1] - self.y_arr[idx]) /
                              (self.x_arr[idx + 1] - self.x_arr[idx]))

        fig = plt.figure()
        fig.patch.set_facecolor('#cccccc')
        plt.plot(self.x_arr[:-1], self.a_arr)
        plt.xlabel("time(s)")
        plt.ylabel("acceleration(m/s^2)")
        plt.title("Acceleration")
        plt.savefig(img_name, facecolor=fig.get_facecolor(), edgecolor='none')
        # plt.show()
