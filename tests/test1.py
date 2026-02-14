import matplotlib.pyplot as plt
import numpy as np

# Definition der Basisvektoren im 3D-Raum
e1 = np.array([1, 0, 0])
e2 = np.array([0, 1, 0])
e3 = np.array([0, 0, 1])

# Figur und weißen Hintergrund einstellen
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', facecolor='white')

# Vektoren vom Ursprung (0,0,0) zeichnen
ursprung = np.array([0, 0, 0])
ax.quiver(*ursprung, *e1, color='red', label='e1')
ax.quiver(*ursprung, *e2, color='green', label='e2')
ax.quiver(*ursprung, *e3, color='blue', label='e3')

# Achsenlimits einstellen
ax.set_xlim([0, 1.2])
ax.set_ylim([0, 1.2])
ax.set_zlim([0, 1.2])

# Achsen beschriften
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Legende anzeigen
ax.legend()
plt.show()
