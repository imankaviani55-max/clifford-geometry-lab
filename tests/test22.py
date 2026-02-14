import numpy as np
import matplotlib.pyplot as plt
from clifford.g3c import layout, e1, e2, e3, e4, e5

# --- CGA-Basis-Einstellungen ---
ep, em = e4, e5
# eo = Ursprung, n_inf = Unendlichkeit (im Text als e1 bezeichnet)
eo = 0.5 * (em - ep)
n_inf = em + ep

def extract_sphere_params(S):
    """Extrahiert Zentrum und Radius aus einem CGA-Kugel-Vektor."""
    # 1. Zentrum bestimmen (Euklidischer Teil des Vektors)
    center_vec = [ (S | e1)[0], (S | e2)[0], (S | e3)[0] ]
    s_sq = sum(c**2 for c in center_vec)
    
    # 2. Extraktion von s4 (der Koeffizient vor der Unendlichkeit n_inf)
    # Da S | eo = -s4 (wegen n_inf | eo = -1)
    s4 = -(S | eo)[0]
    
    # 3. Radius berechnen nach Formel: r^2 = s^2 - 2*s4
    r_sq = s_sq - 2 * s4
    return center_vec, np.sqrt(abs(r_sq))

# --- 1. Definition der Kugel nach Ihrem Text ---
# Formel: S = s + s4*n_inf + eo
# Ihr Beispiel: S = e2 + e3 - e1 + eo (Hier ist e1 = n_inf)
S = e2 + e3 - 1*n_inf + eo

center, radius = extract_sphere_params(S)
print(f"Berechnetes Zentrum: {center}")
print(f"Berechneter Radius: {radius}")

# --- 2. Geometrische Darstellung mit Matplotlib ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Erstellung der Kugeloberfläche (Sphäre)
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))

# Die Kugel zeichnen
ax.plot_surface(x, y, z, color='cyan', alpha=0.4, edgecolor='darkblue', linewidth=0.3)

# Das Zentrum der Kugel markieren (roter Punkt)
ax.scatter(center[0], center[1], center[2], color='red', s=100, label='Zentrum (s)')

# Achsenbeschriftungen und Layout
ax.set_xlabel('X-Achse (e1)')
ax.set_ylabel('Y-Achse (e2)')
ax.set_zlabel('Z-Achse (e3)')
ax.set_title(f'Visualisierung der CGA-Kugel\nZentrum: {center}, Radius: {radius}')
ax.legend()

# Achsen skalieren, damit die Kugel nicht verzerrt aussieht
max_range = radius * 2
ax.set_xlim(center[0]-max_range, center[0]+max_range)
ax.set_ylim(center[1]-max_range, center[1]+max_range)
ax.set_zlim(center[2]-max_range, center[2]+max_range)

plt.show()