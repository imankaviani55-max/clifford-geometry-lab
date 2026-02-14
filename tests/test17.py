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
    s = np.linspace(-1, 1, 10)
    t = np.linspace(-1, 1, 10)
    S, T = np.meshgrid(s, t)
    X = S * float(a | e1) + T * float(b | e1)
    Y = S * float(a | e2) + T * float(b | e2)
    Z = S * float(a | e3) + T * float(b | e3)
    ax.plot_surface(X, Y, Z, alpha=alpha, color=color)

# --- Visualisierung ---
fig = plt.figure(figsize=(12,10))

# --- Linkes Diagramm: Rotor aus zwei Vektoren ---
ax1_3d = fig.add_subplot(221, projection='3d')
ax1_3d.quiver(0,0,0,*mv_to_xyz(a), color='blue', label='a (original)')
ax1_3d.quiver(0,0,0,*mv_to_xyz(b), color='green', label='b')
ax1_3d.quiver(0,0,0,*mv_to_xyz(c), color='red', label='c = R*a*~R')
plot_plane(ax1_3d, a, b, alpha=0.3, color='cyan')
ax1_3d.set_title('3D Rotation: R = b*a')
ax1_3d.set_xlim([-1,1]); ax1_3d.set_ylim([-1,1]); ax1_3d.set_zlim([-1,1])
ax1_3d.set_xlabel('X'); ax1_3d.set_ylabel('Y'); ax1_3d.set_zlabel('Z')
ax1_3d.legend()

# --- Unteres 2D-Projektionsdiagramm ---
ax1_2d = fig.add_subplot(223)
for vec, color, label in [(a, 'blue', 'a'), (b, 'green', 'b'), (c, 'red', 'c')]:
    x, y, z = mv_to_xyz(vec)
    ax1_2d.quiver(0, 0, x, y, color=color, angles='xy', scale_units='xy', scale=1, label=label)
ax1_2d.set_xlim([-1,1]); ax1_2d.set_ylim([-1,1])
ax1_2d.set_xlabel('X'); ax1_2d.set_ylabel('Y')
ax1_2d.set_title('2D Projection XY')
ax1_2d.legend()

# --- Rechtes Diagramm: Exponential Rotor ---
ax2_3d = fig.add_subplot(222, projection='3d')
ax2_3d.quiver(0,0,0,*mv_to_xyz(a), color='blue', label='a (original)')
ax2_3d.quiver(0,0,0,*mv_to_xyz(b_rot), color='magenta', label='b_rot (exp)')
plot_plane(ax2_3d, a, b, alpha=0.3, color='cyan')
ax2_3d.set_title('3D Rotation: exp(-i*theta/2)')
ax2_3d.set_xlim([-1,1]); ax2_3d.set_ylim([-1,1]); ax2_3d.set_zlim([-1,1])
ax2_3d.set_xlabel('X'); ax2_3d.set_ylabel('Y'); ax2_3d.set_zlabel('Z')
ax2_3d.legend()

# --- Unteres 2D-Projektionsdiagramm ---
ax2_2d = fig.add_subplot(224)
for vec, color, label in [(a, 'blue', 'a'), (b_rot, 'magenta', 'b_rot')]:
    x, y, z = mv_to_xyz(vec)
    ax2_2d.quiver(0, 0, x, y, color=color, angles='xy', scale_units='xy', scale=1, label=label)
ax2_2d.set_xlim([-1,1]); ax2_2d.set_ylim([-1,1])
ax2_2d.set_xlabel('X'); ax2_2d.set_ylabel('Y')
ax2_2d.set_title('2D Projection XY')
ax2_2d.legend()

plt.tight_layout()
plt.show()
