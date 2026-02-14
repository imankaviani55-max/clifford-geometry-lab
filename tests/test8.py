# Installation falls nötig
# pip install clifford numpy

import clifford.g3 as g3
from clifford.g3 import blades
import numpy as np

# Basisvektoren
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# --- Geometric Product (uv = u·v + u^v) ---

def geometric_product(u, v):
    """Berechnet den geometrischen Produkts uv"""
    return u * v  # In clifford, * ist der geometrische Produktsoperator

def inner_product(u, v):
    """Inner Product aus geometrischem Produkt"""
    return 0.5 * (u*v + v*u)

def outer_product(u, v):
    """Outer Product aus geometrischem Produkt"""
    return 0.5 * (u*v - v*u)

# Beispiele:

# Example 1: Quadrat eines Vektors
a = e1
a_squared = geometric_product(a, a)
print("a^2 =", a_squared, "  (Nur Skalar, da a^a = 0)")

# Example 2: (e1 + e2)^2
v = e1 + e2
v_squared = geometric_product(v, v)
print("(e1+e2)^2 =", v_squared)
print("Inner Product =", inner_product(v,v))
print("Outer Product =", outer_product(v,v))

# Example 3: e1*e2
prod_e1e2 = geometric_product(e1, e2)
print("e1*e2 =", prod_e1e2)
print("Inner Product e1·e2 =", inner_product(e1,e2))
print("Outer Product e1^e2 =", outer_product(e1,e2))

# Example 4: e1*(e1+e2)
prod_example4 = geometric_product(e1, e1+e2)
print("e1*(e1+e2) =", prod_example4)
print("Inner Product =", inner_product(e1, e1+e2))
print("Outer Product =", outer_product(e1, e1+e2))

# --- Optional: Visualisierung ---
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Funktion zur Extraktion von e1,e2,e3 Komponenten aus Multivector
def mv_to_xyz(v):
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

# Vektoren e1 und e2 zeichnen
ax.quiver(0,0,0,*mv_to_xyz(e1), color='blue', label='e1')
ax.quiver(0,0,0,*mv_to_xyz(e2), color='green', label='e2')

# Outer product (Plane) e1^e2
xx, yy = np.meshgrid([0,1],[0,1])
zz = 0*xx
ax.plot_surface(xx, yy, zz, color='red', alpha=0.3, label='e1^e2')

ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_zlim([0,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Geometric Product in 3D GA')
ax.legend()
plt.show()
