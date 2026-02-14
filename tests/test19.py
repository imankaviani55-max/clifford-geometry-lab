import clifford.g3 as g3
from clifford.g3 import blades
import matplotlib.pyplot as plt
import numpy as np

# --- Basisvektoren ---
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# --- Ursprungsvektor ---
a = e1 + e2  # blauer Vektor

# --- Rotationsachse und Normalisierung ---
achse = -3*e1 + 6*e2 - 2*e3
achse = achse / np.sqrt(float(achse | achse))

# --- Ebene dual zur Achse ---
p = ~achse  # Dual der Achse -> Ebene

# --- Rotationswinkel ---
winkel = np.pi / 3

# --- Rotor ---
R = np.cos(winkel/2) - p * np.sin(winkel/2)

# --- Rotierter Vektor ---
c = R * a * ~R  # roter Vektor

# --- Funktion zur Extraktion von Komponenten ---
def mv_to_xyz(v):
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

# --- Funktion zur Darstellung der Ebene (numerisch) ---
def plot_ebene(ax, normal, size=1.5, alpha=0.2, color='cyan'):
    # Erzeuge zwei orthogonale Vektoren zur Normalen
    n = np.array([float(normal | e1), float(normal | e2), float(normal | e3)])
    n = n / np.linalg.norm(n)
    
    # zwei beliebige Vektoren orthogonal zu n
    if abs(n[0]) < 0.9:
        v1 = np.array([1,0,0])
    else:
        v1 = np.array([0,1,0])
    v1 = v1 - np.dot(v1, n)*n
    v1 = v1 / np.linalg.norm(v1)
    v2 = np.cross(n, v1)
    
    # Gitterpunkte auf der Ebene
    s = np.linspace(-size, size, 10)
    t = np.linspace(-size, size, 10)
    S, T = np.meshgrid(s, t)
    X = S*v1[0] + T*v2[0]
    Y = S*v1[1] + T*v2[1]
    Z = S*v1[2] + T*v2[2]
    ax.plot_surface(X, Y, Z, alpha=alpha, color=color)

# --- Visualisierung ---
fig = plt.figure(figsize=(12,10))

# --- 3D Darstellung ---
ax3d = fig.add_subplot(121, projection='3d')
ax3d.quiver(0,0,0,*mv_to_xyz(a), color='blue', label='a (ursprünglich)')
ax3d.quiver(0,0,0,*mv_to_xyz(c), color='red', label='c (rotiert)')
plot_ebene(ax3d, achse, alpha=0.3, color='cyan')
ax3d.set_xlim([-1.5,1.5]); ax3d.set_ylim([-1.5,1.5]); ax3d.set_zlim([-1.5,1.5])
ax3d.set_xlabel('X'); ax3d.set_ylabel('Y'); ax3d.set_zlabel('Z')
ax3d.set_title('3D Rotation mit Rotor und Ebene p')
ax3d.legend()

# --- 2D XY Projektion ---
ax2d = fig.add_subplot(122)
for vec, color, label in [(a, 'blue', 'a'), (c, 'red', 'c')]:
    x, y, z = mv_to_xyz(vec)
    ax2d.quiver(0,0,x,y,color=color, angles='xy', scale_units='xy', scale=1, label=label)
ax2d.set_xlim([-1.5,1.5]); ax2d.set_ylim([-1.5,1.5])
ax2d.set_xlabel('X'); ax2d.set_ylabel('Y')
ax2d.set_title('XY-Projektion')
ax2d.legend()

plt.tight_layout()
plt.show()
