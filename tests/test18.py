import clifford.g3 as g3
from clifford.g3 import blades
import matplotlib.pyplot as plt
import numpy as np

# Basisvektoren
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# Ursprungsvektor
a = e1 + e2  # blauer Vektor

# Rotationsachse und Normalisierung
achse = -3*e1 + 6*e2 - 2*e3
achse = achse / np.sqrt(float(achse | achse))

# Ebene, die zur Achse dual ist
p = ~achse  # Dual der Achse -> Ebene

# Rotationswinkel
winkel = np.pi / 3

# Rotor
R = np.cos(winkel/2) - p * np.sin(winkel/2)

# Rotierter Vektor
c = R * a * ~R  # roter Vektor

# Funktion zur Extraktion von Komponenten
def mv_to_xyz(v):
    x = float(v | e1)
    y = float(v | e2)
    z = float(v | e3)
    return x, y, z

# 3D Visualisierung
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0,0,0,*mv_to_xyz(a), color='blue', label='a (ursprünglich)')
ax.quiver(0,0,0,*mv_to_xyz(c), color='red', label='c (rotiert)')
ax.set_xlim([-1,1]); ax.set_ylim([-1,1]); ax.set_zlim([-1,1])
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title('3D Rotation mit Rotor')
ax.legend()
plt.show()
