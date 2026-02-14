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

# --- Vektor definieren ---
v = e1 + 2*e3
print("Original vector v =", v)

# --- Ebene definieren ---
M = e1 ^ e2  # Bivector plane
print("Plane M =", M)

# --- Reflection berechnen ---
vrefl = M * v * M
print("Reflected vector vrefl =", vrefl)

# --- Visualisierung ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Funktion zur Extraktion der e1,e2,e3 Komponenten
def mv_to_xyz(v):
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

# Original vector v in Blau
ax.quiver(0,0,0,*mv_to_xyz(v), color='blue', label='v (original)')

# Plane M als grünes Rechteck
xx, yy = np.meshgrid([0,1],[0,1])
zz = 0*xx
ax.plot_surface(xx, yy, zz, color='green', alpha=0.3, label='Plane M')

# Reflektierter vector vrefl in Rot
ax.quiver(0,0,0,*mv_to_xyz(vrefl), color='red', label='vrefl (reflected)')

ax.set_xlim([-2,2])
ax.set_ylim([-2,2])
ax.set_zlim([-2,2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Reflection of a Vector from a Plane')
ax.legend()
plt.show()
