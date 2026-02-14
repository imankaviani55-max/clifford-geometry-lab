# Installation falls nötig
# pip install clifford numpy

import clifford.g3 as g3
from clifford.g3 import blades
import numpy as np

# Basisvektoren
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# --- Inner Product zwischen zwei Bivektoren ---
B = e1 ^ e2  # Bivector
B_squared = float(B | B)  # Inner product von B mit sich selbst
print("Bivector B =", B)
print("Inneres Produkt B · B =", B_squared)  # Erwartet -1
# Erklärung: In 3D GA kann das Quadrat eines Bivektors negativ sein

# --- Inner Product zwischen Vektor und Bivector ---
x = e1 + e3
xiB = x | B  # Resultierender Vektor in der Ebene von B, senkrecht zu x
print("Vektor x =", x)
print("Inneres Produkt x · B =", xiB)

# Überprüfen der Grade
print("Grade von B:", B.grades())         # 2
print("Grade von x:", x.grades())         # 1
print("Grade von xiB:", xiB.grades())     # 1 (grade-1 Element)

# --- Optionale Visualisierung ---
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Funktion zur Extraktion von e1,e2,e3 Komponenten aus Multivector
def mv_to_xyz(v):
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

# Vektor x in Blau
ax.quiver(0,0,0,*mv_to_xyz(x), color='blue', label='x = e1 + e3')

# xiB in Grün
ax.quiver(0,0,0,*mv_to_xyz(xiB), color='green', label='xiB = x | B')

# Die Ebene des Bivektors B (e1^e2) als rotes Rechteck
xx, yy = np.meshgrid([0,1],[0,1])
zz = 0*xx
ax.plot_surface(xx, yy, zz, color='red', alpha=0.3)

ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_zlim([0,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Inner Product in Geometric Algebra')
ax.legend()
plt.show()
