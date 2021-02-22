import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# Read and store the columns of the file
file = pd.read_csv("~/Documents/UiO/STK1100/Oblig1/Python/dodssannsynlighet-felles.txt", sep="\t")

# Set each column as a vector
age = file["ald"].values
death = file["dod"].values

# Defininf q byconverting death from per mille to decimal
q = death/1000

# Using the formula in a to calculate the cdf
Fx = 1-np.cumprod(1-q[35:107])

# VAriable tmp that offset the values of q by one
tmp = np.zeros(72)
tmp[1:72] = Fx[:71]

# variable that calculates the pmf on every point
p = Fx - tmp

# Creating a bar plot and saving it in the image directory to use in the latex document
x = np.arange(0, 72)
plt.bar(x, p, 1, edgecolor="black")
plt.xlabel("Gjenstående levetid")
plt.ylabel("Sannsynlighet")
plt.savefig("/home/cory/Documents/UiO/STK1100/Oblig1/images/1c.png")

Ex = sum(x*p)

print(Ex)