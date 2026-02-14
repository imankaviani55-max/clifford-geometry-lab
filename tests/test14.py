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

# --- Beispiel 1: Rotor aus zwei Vektoren ---
a = e1
b = (1/np.sqrt(2))*(e1 + e2)

# Rotor
R = b * a
R_rev = ~R  # Reverse von R

# Rotierte Vektor
c = R * a * R_rev

print("Vector a =", a)
print("Vector b =", b)
print("Rotor R = b*a =", R)
print("Rotated vector c = R*a*~R =", c)

# --- Beispiel 2: Rotor aus exponentieller Funktion ---
i = e1 ^ e2  # Ebene
theta = np.pi/4  # Rotationswinkel Pi/4

# Exponentielle Darstellung: R = exp(-i*theta/2)
R_exp = np.cos(theta/2) - i*np.sin(theta/2)
R_exp_rev = ~R_exp

# Rotierte Vektor
b_rot = R_exp * a * R_exp_rev

print("Rotor (exp) R_exp =", R_exp)
print("Rotated vector (exp) b_rot =", b_rot)

# --- Visualisierung ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def mv_to_xyz(v):
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

# Original vector a in Blau
ax.quiver(0,0,0,*mv_to_xyz(a), color='blue', label='a (original)')

# Vector b in Grün
ax.quiver(0,0,0,*mv_to_xyz(b), color='green', label='b')

# Rotated vector c in Rot
ax.quiver(0,0,0,*mv_to_xyz(c), color='red', label='c = R*a*~R')

# Rotated vector with exp in Magenta
ax.quiver(0,0,0,*mv_to_xyz(b_rot), color='magenta', label='b_rot (exp)')

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('2D Rotation with Rotors in Geometric Algebra')
ax.legend()
plt.show()
