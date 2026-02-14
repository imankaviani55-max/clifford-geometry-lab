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

# Drei Vektoren definieren
a = e1 + e2
b = e1 - e2
c = e3

# Trivector d durch Außenprodukt (wedge) berechnen
d = a ^ b ^ c

# Ausgabe
print("Vektor a:", a)
print("Vektor b:", b)
print("Vektor c:", c)
print("Trivector d = a ^ b ^ c:", d)

# Reverse von d
d_reverse = ~d
print("Reverse von d:", d_reverse)

# --- Visualisierung ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Funktion zur Extraktion der e1, e2, e3 Komponenten aus MultiVector
def mv_to_xyz(v):
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

# Vektoren a, b, c in Blau zeichnen
ax.quiver(0, 0, 0, *mv_to_xyz(a), color='blue', label='a = e1 + e2')
ax.quiver(0, 0, 0, *mv_to_xyz(b), color='blue', label='b = e1 - e2')
ax.quiver(0, 0, 0, *mv_to_xyz(c), color='blue', label='c = e3')

# Trivector d als Volumenelement (Pseudoskalar) visualisieren
# Wir zeichnen ein transparentes rotes Quader-Volumen, das den Raum aufspannt
xx, yy = np.meshgrid([0,1], [0,1])
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, color='red', alpha=0.3)        # Boden
ax.plot_surface(xx, yy, zz+1, color='red', alpha=0.3)      # Decke
ax.plot_surface(xx, zz, yy, color='red', alpha=0.3)        # Seitenflächen
ax.plot_surface(zz, xx, yy, color='red', alpha=0.3)
ax.plot_surface(yy, xx, zz, color='red', alpha=0.3)
ax.plot_surface(yy, xx, zz+1, color='red', alpha=0.3)

ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_zlim([0,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Trivector in 3D Euclidean Space')
ax.legend()
plt.show()
