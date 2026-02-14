# Installation falls nötig
# pip install clifford matplotlib numpy

import clifford.g3 as g3
from clifford.g3 import blades
import matplotlib.pyplot as plt
import numpy as np

# Basisvektoren
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# Zwei Vektoren a und b definieren
a = e1 + e2
b = e1 - e2

# Bivector c durch Außenprodukt (wedge) berechnen
c = a ^ b

# Reverse von c
c_reverse = ~c

# Ausgabe
print("Vektor a:", a)
print("Vektor b:", b)
print("Bivector c = a ^ b:", c)
print("Reverse von c:", c_reverse)

# --- Visualisierung ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Multivector zu 3D Koordinaten konvertieren
def mv_to_xyz(v):
    # Nur die Komponenten e1, e2, e3
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

ax.quiver(0, 0, 0, *mv_to_xyz(a), color='blue', label='a = e1 + e2')
ax.quiver(0, 0, 0, *mv_to_xyz(b), color='blue', label='b = e1 - e2')

# Bivector c als Ebene zeichnen (im e1-e2 Raum)
xx, yy = np.meshgrid(np.linspace(0,1,2), np.linspace(0,1,2))
zz = 0*xx
ax.plot_surface(xx, yy, zz, color='red', alpha=0.5)

ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_zlim([0,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Bivector in 3D Euclidean Space')
ax.legend()
plt.show()
