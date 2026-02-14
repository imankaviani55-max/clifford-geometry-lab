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

# Rotor aus zwei Vektoren
R = b * a
c = R * a * ~R

# Exponential rotor
i = e1 ^ e2
theta = np.pi/4
R_exp = np.cos(theta/2) - i*np.sin(theta/2)
b_rot = R_exp * a * ~R_exp

# Funktion zur Extraktion von Komponenten
def mv_to_xyz(v):
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

# --- Plane aus a und b --- 
def plot_plane(ax, a, b, alpha=0.2, color='cyan'):
    # Erzeuge Gitter auf dem Plan
    s = np.linspace(-1, 1, 10)
    t = np.linspace(-1, 1, 10)
    S, T = np.meshgrid(s, t)
    # Punkte auf dem Plan
    X = S * float(a | e1) + T * float(b | e1)
    Y = S * float(a | e2) + T * float(b | e2)
    Z = S * float(a | e3) + T * float(b | e3)
    ax.plot_surface(X, Y, Z, alpha=alpha, color=color)

# --- Visualisierung ---
fig = plt.figure(figsize=(12,6))

# Linker subplot: Rotor aus zwei Vektoren
ax1 = fig.add_subplot(121, projection='3d')
ax1.quiver(0,0,0,*mv_to_xyz(a), color='blue', label='a (original)')
ax1.quiver(0,0,0,*mv_to_xyz(b), color='green', label='b')
ax1.quiver(0,0,0,*mv_to_xyz(c), color='red', label='c = R*a*~R')
plot_plane(ax1, a, b, alpha=0.3, color='cyan')  # Plane hinzugefügt
ax1.set_title('Rotation with R = b*a')
ax1.set_xlim([-1,1]); ax1.set_ylim([-1,1]); ax1.set_zlim([-1,1])
ax1.set_xlabel('X'); ax1.set_ylabel('Y'); ax1.set_zlabel('Z')
ax1.legend()

# Rechter subplot: Rotor aus exponential
ax2 = fig.add_subplot(122, projection='3d')
ax2.quiver(0,0,0,*mv_to_xyz(a), color='blue', label='a (original)')
ax2.quiver(0,0,0,*mv_to_xyz(b_rot), color='magenta', label='b_rot (exp)')
plot_plane(ax2, a, b, alpha=0.3, color='cyan')  # Plane nochmal hinzugefügt
ax2.set_title('Rotation with R = exp(-i*theta/2)')
ax2.set_xlim([-1,1]); ax2.set_ylim([-1,1]); ax2.set_zlim([-1,1])
ax2.set_xlabel('X'); ax2.set_ylabel('Y'); ax2.set_zlabel('Z')
ax2.legend()

plt.show()
