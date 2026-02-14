# Installation falls nötig
# pip install clifford numpy matplotlib

import clifford.g3 as g3
from clifford.g3 import blades
import matplotlib.pyplot as plt
import numpy as np

# Basisvektoren
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# Pseudoscalar
I = e1 ^ e2 ^ e3

# --- Plane definieren ---
A = e2 ^ (e1 + e3)  # Bivector
print("Plane A =", A)

# --- Dual berechnen ---
b = A / I  # Dual von A
print("Dual b = A/I =", b)

# --- Überprüfung: b ist normal zur Ebene A ---
# Inner product zwischen b und A sollte 0 für jeden Vektor in A sein
v1 = e2
v2 = e1 + e3
print("b·v1 =", float(b | v1))
print("b·v2 =", float(b | v2))

# --- Visualisierung ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Funktion zur Extraktion von e1,e2,e3 Komponenten
def mv_to_xyz(v):
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

# Plane A (Bivector) als rotes Rechteck
xx, yy = np.meshgrid([0,1],[0,1])
zz = 0*xx
ax.plot_surface(xx, yy, zz, color='red', alpha=0.3, label='Plane A')

# Dualvektor b in grün
ax.quiver(0,0,0,*mv_to_xyz(b), color='green', label='Dual b = A/I')

# Zwei Vektoren in der Ebene zur Kontrolle
ax.quiver(0,0,0,*mv_to_xyz(v1), color='blue', label='v1 in A')
ax.quiver(0,0,0,*mv_to_xyz(v2), color='blue', label='v2 in A')

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Dual of a Plane in 3D GA')
ax.legend()
plt.show()
