import clifford.g3 as g3
from clifford.g3 import blades
import matplotlib.pyplot as plt
import numpy as np

# Basisvektoren
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# Original vector a und Ziel-vektor b
a = e1
b = (1/np.sqrt(2))*(e1 + e2)

# --- Rotor aus zwei Vektoren ---
R = b * a
c = R * a * ~R

# --- Rotor aus exponential ---
i = e1 ^ e2
theta = np.pi/4
R_exp = np.cos(theta/2) - i*np.sin(theta/2)
b_rot = R_exp * a * ~R_exp

# --- Funktion zur Extraktion von Komponenten ---
def mv_to_xyz(v):
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

# --- Visualisierung mit zwei Subplots ---
fig = plt.figure(figsize=(12,6))

# Linker subplot: Rotor aus zwei Vektoren
ax1 = fig.add_subplot(121, projection='3d')
ax1.quiver(0,0,0,*mv_to_xyz(a), color='blue', label='a (original)')
ax1.quiver(0,0,0,*mv_to_xyz(b), color='green', label='b')
ax1.quiver(0,0,0,*mv_to_xyz(c), color='red', label='c = R*a*~R')
ax1.set_title('Rotation with R = b*a')
ax1.set_xlim([-1,1]); ax1.set_ylim([-1,1]); ax1.set_zlim([-1,1])
ax1.set_xlabel('X'); ax1.set_ylabel('Y'); ax1.set_zlabel('Z')
ax1.legend()

# Rechter subplot: Rotor aus exponential
ax2 = fig.add_subplot(122, projection='3d')
ax2.quiver(0,0,0,*mv_to_xyz(a), color='blue', label='a (original)')
ax2.quiver(0,0,0,*mv_to_xyz(b_rot), color='magenta', label='b_rot (exp)')
ax2.set_title('Rotation with R = exp(-i*theta/2)')
ax2.set_xlim([-1,1]); ax2.set_ylim([-1,1]); ax2.set_zlim([-1,1])
ax2.set_xlabel('X'); ax2.set_ylabel('Y'); ax2.set_zlabel('Z')
ax2.legend()

plt.show()
