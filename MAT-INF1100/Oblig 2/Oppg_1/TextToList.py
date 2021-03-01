import matplotlib.pyplot as plt
import numpy as np


class TextToList:
    def __init__(self, textfile):
        self.textfile = textfile
        self.x = []
        self.y = []

    def ret_list(self):
        with open(self.textfile, "r") as f:
            a = f.readlines()
            for i in a:
                s = i.replace("\n", "").split(",")
                self.x.append(float(s[0]))
                self.y.append(float(s[1]))

        return [self.x, self.y]
