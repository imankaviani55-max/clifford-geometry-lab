import numpy as np
import matplotlib.pyplot as plt
from clifford.g3c import layout, e1, e2, e3, e4, e5

# CGA Setup
ep, em = e4, e5
eo = 0.5 * (em - ep)
n_inf = em + ep

def erstelle_punkt(x, y, z):
    p = x*e1 + y*e2 + z*e3
    return p + 0.5 * (x**2 + y**2 + z**2) * n_inf + eo

# --- 1. Punkte definieren (laut CircleN3.clu) ---
a = erstelle_punkt(0, -0.5, -0.5)
b = erstelle_punkt(0, 0.5, 0.5)
c = erstelle_punkt(0.5, 0.5, 0.5)

# --- 2. Kreis berechnen (Outer Product) ---
# Das Dokument nutzt Circle = *(a ^ b ^ c)
# In der clifford-Lib ist .dual() das Äquivalent zu *
kreis_trivektor = a ^ b ^ c
kreis_bivektor = kreis_trivektor.dual()

print("Bivektor Repräsentation des Kreises:")
print(kreis_bivektor)

# --- 3. Visualisierung ---
# Wir extrahieren die euklidischen Koordinaten für den Plot
pts = np.array([[0, -0.5, -0.5], [0, 0.5, 0.5], [0.5, 0.5, 0.5]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Punkte a, b, c zeichnen
ax.scatter(pts[:,0], pts[:,1], pts[:,2], color='red', s=100, label='Punkte a, b, c')

# Kreis zeichnen (Geometrische Lösung für den Plot)
# Ein Kreis durch 3 Punkte erfordert etwas euklidische Geometrie:
v1 = pts[1] - pts[0]
v2 = pts[2] - pts[0]
normal = np.cross(v1, v2)
normal /= np.linalg.norm(normal)

# Hilfsberechnung für den Mittelpunkt (vereinfacht für die Grafik)
center = np.mean(pts, axis=0) # Grobe Annäherung für Visualisierung
radius = np.linalg.norm(pts[0] - center)

# Kreis-Punkte generieren
theta = np.linspace(0, 2*np.pi, 100)
# Basisvektoren in der Kreisebene
b1 = v1 / np.linalg.norm(v1)
b2 = np.cross(normal, b1)
kreis_pts = np.array([center + radius * (np.cos(t)*b1 + np.sin(t)*b2) for t in theta])

ax.plot(kreis_pts[:,0], kreis_pts[:,1], kreis_pts[:,2], color='green', linewidth=3, label='CGA Kreis')

ax.set_title("Visualisierung: Kreis aus 3 Punkten (a ^ b ^ c)")
ax.legend()
plt.show()