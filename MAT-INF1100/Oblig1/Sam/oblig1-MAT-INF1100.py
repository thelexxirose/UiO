from math import sqrt
"""
Oppgave 1) Vi skal se på differensligningen:
xn+2 − 4xn+1 − xn = 0, med x0 = 1 og x1 = 1.
"""

#a) Lag et dataprogram som simulerer denne ligningen og skriver ut følgen x2, x3, . . . , x100
for n in range(2, 101):
    a = n+2
    b = n+1
    c = n
    x1 = 1

    xn = x1*a-(4*x1*b)-x1*c
    
    # print(f"{xn:5.2f}") --------------
#b) Simuler ligningen og skriv ut følgen x2, x3, . . . , x100 når startverdien x1 endres til x1 = 2−√5
print("\n\n")
for n in range(2, 101):
    a = n+2
    b = n+1
    c = n
    x1 = 2-sqrt(5)

    xn2 = a*x1-(4*b*x1)-c*x1
    
    # print(f"{xn2:10.2f}") ----------

#c) ...
"""
Vis at den generelle løsningen av ligningen xn+2 − 4xn+1 − xn = 0
er på formen xn = C(2 − √5)^n + D(2 + √5)^n og at initialverdiene x0 = 1 og x1 = 2 −√5 
bestemmer den endelige løsningen til å være xn = (2 − √5)^n.
"""

