# Bibliothek installieren falls nötig
# pip install clifford

import clifford as cf
from clifford.g3 import layout, blades
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Definition des 3D euklidischen Raums
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# 0-Blade (Skalar)
skalar = 1.0

# 1-Blades (Basisvektoren)
v1 = e1
v2 = e2
v3 = e3

# 2-Blade (Flächenelement)
ebene = e1 ^ e2  # Keilprodukt zur Erstellung eines 2-Blades

# Ausgabe der Blade-Werte
print("Skalar (0-Blade):", skalar)
print("1-Blades: e1 =", v1, ", e2 =", v2, ", e3 =", v3)
print("2-Blade (Fläche e1^e2):", ebene)

# --- Zeichnen der 1-Blades und 2-Blades ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Basisvektoren zeichnen
ax.quiver(0, 0, 0, 1, 0, 0, color='blue', label='e1')
ax.quiver(0, 0, 0, 0, 1, 0, color='blue', label='e2')
ax.quiver(0, 0, 0, 0, 0, 1, color='blue', label='e3')

# Fläche e1^e2 zeichnen
xx, yy = np.meshgrid(np.linspace(0,1,2), np.linspace(0,1,2))
zz = 0*xx
ax.plot_surface(xx, yy, zz, color='red', alpha=0.5)

ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_zlim([0,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Blades im 3D euklidischen Raum')
plt.show()
