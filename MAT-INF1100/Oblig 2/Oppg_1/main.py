from TextToList import TextToList
from Accel import Accel
from Distance import Distance

f = TextToList("Oppg_1/running.txt")

l = f.ret_list()

a = Accel(l[0], l[1])
a.plot("images/Accel.png")

d = Distance(l[0], l[1])
d.plot_trapezoid("images/Distance.png")
