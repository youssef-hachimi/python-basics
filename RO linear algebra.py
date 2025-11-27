import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from numpy.linalg import solve

x1 = int(input("Entrer la valeur de x1 :"))
y1 = int(input("Entrer la valeur de x1 :"))
z1 = int(input("Entrer la valeur de x1 :"))

x2 = int(input("Entrer la valeur de x1 :"))
y2= int(input("Entrer la valeur de x1 :"))
z2 = int(input("Entrer la valeur de x1 :"))

constraints = [
    (x1, y1, z1),
    (x2, y2, z2)
]

x_max = 50
y_max = 50
x = np.linspace(0, x_max, 400)

lines = []
for a, b, c in constraints:
    if b != 0:
        y = (c - a *x)/b
    else:
        y = np.full_like(x, np.nan)
    lines.append((x, y))

#calculer intersections de paires de droites
def intersection(line1, line2):
    #line is (a,b,c) for ax + by = c
    a1, b1, c1 = line1
    a2, b2, c2 = line2
    A = np.array([[a1, b1], [a2, b2]], dtype = float)
    B = np.array([c1, c2], dtype = float)
    return np.linalg.solve(A, B)
#trouver toute les intersections entre contraites et axes
points = []
# axes intersections
for a, b, c, in constraints:
    #with x=0 -> y = c/b if b != 0
    if b != 0:
        points.append((0, c/b))
    #with y=0 -> x = c/a if a != 0
    if a != 0:
        points.append((c/a, 0))

points.append(tuple(intersection(constraints[0],constraints[1])))

feasible = []
for px, py in points:
    if px >= -1e-6 and py >= -1e-6:
        ok = True
        for a,b,c in constraints:
            if a*px + b*py -c > 1e-6:
                ok = False
                break
        if ok :
            feasible.append((round(px,6), round(py,6)))
#unique
feasible = sorted(set(feasible))
print("sommets realisable : ", feasible)

#calcul Z
def Z(p):
    return 3*p[0] + 5*p[1]

values = [(p, Z(p)) for p in feasible]
print("valeurs de Z en Sommets:", values)

#tracer la figure
plt.figure(figsize=(6,6))
for xi, yi in lines:
    plt.plot(xi, yi)

#shading feasible region by testing grid points
xx = np.linspace(0, x_max, 300)
yy = np.linspace(0, y_max, 300)
XX, YY = np.meshgrid(xx, yy)
mask = np.ones_like(XX, dtype=bool)
for a, b, c in constraints:
    mask = mask & (a*XX + b*YY <= c + 1e-6)