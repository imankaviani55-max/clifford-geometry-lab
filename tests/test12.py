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

# --- Plane B definieren ---
B = e1 ^ (e1 + e2)   # Bivector
print("Plane B =", B)

# --- Vektor v definieren ---
v = 1.5*e1 + e2/3 + e3
print("Original vector v =", v)

# --- Projection und Rejection ---
vpar = (v | B) / B    # projection auf die Ebene
vperp = (v ^ B) / B   # rejection (orthogonal zur Ebene)
sum_v = vpar + vperp

print("Projection vpar =", vpar)
print("Rejection vperp =", vperp)
print("Sum vpar + vperp =", sum_v)  # sollte v ergeben

# --- Visualisierung ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Funktion zur Extraktion der e1,e2,e3 Komponenten
def mv_to_xyz(v):
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

# Plane B als rotes Rechteck
xx, yy = np.meshgrid([0,1],[0,1])
zz = 0*xx
ax.plot_surface(xx, yy, zz, color='red', alpha=0.3, label='Plane B')

# Projection vpar in Blau
ax.quiver(0,0,0,*mv_to_xyz(vpar), color='blue', label='vpar (projection)')

# Rejection vperp in Gelb
ax.quiver(0,0,0,*mv_to_xyz(vperp), color='yellow', label='vperp (rejection)')

# Original vector v in Magenta
ax.quiver(0,0,0,*mv_to_xyz(v), color='magenta', label='v (original)')

ax.set_xlim([0,2])
ax.set_ylim([0,2])
ax.set_zlim([0,2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Projection and Rejection of a Vector onto a Plane')
ax.legend()
plt.show()
