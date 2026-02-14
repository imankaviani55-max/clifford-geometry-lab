import numpy as np
import matplotlib.pyplot as plt
from clifford.g3c import layout, e1, e2, e3, e4, e5

# CGA Setup
ep, em = e4, e5
eo = 0.5 * (em - ep)
n_inf = em + ep  # Dies ist das 'n' aus deinem Dokument

def erstelle_punkt(x, y, z):
    p = x*e1 + y*e2 + z*e3
    return p + 0.5 * (x**2 + y**2 + z**2) * n_inf + eo

# --- 1. Punkte definieren (laut LineN3.clu) ---
a = erstelle_punkt(0, -0.5, -0.5)
b = erstelle_punkt(0, 0.5, 0.5)

# --- 2. Gerade berechnen (Outer Product mit n_inf) ---
# Formel aus dem Text: line = *(a ^ b ^ n)
line_trivektor = a ^ b ^ n_inf
line_bivektor = line_trivektor.dual()

print("="*50)
print("CGA GERADEN-FORMEL (BIVEKTOR):")
print(line_bivektor)
print("="*50)

# --- 3. 3D-Visualisierung ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Punkte a und b zeichnen
ax.scatter([0, 0], [-0.5, 0.5], [-0.5, 0.5], color='red', s=100, label='Punkte a, b')

# Gerade zeichnen
# Wir verlängern die Verbindung zwischen a und b für die Darstellung
t = np.linspace(-2, 2, 100)
lx = np.zeros_like(t)
ly = -0.5 + t * (0.5 - (-0.5))
lz = -0.5 + t * (0.5 - (-0.5))

ax.plot(lx, ly, lz, color='green', linewidth=3, label='CGA Gerade (Kreis durch Unendlich)')

ax.set_title("Visualisierung: Gerade als degenerierter Kreis (a ^ b ^ n_inf)")
ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
ax.legend()
plt.show()