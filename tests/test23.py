import numpy as np
import matplotlib.pyplot as plt
from clifford.g3c import layout, e1, e2, e3, e4, e5

# Basis-Konfiguration
ep, em = e4, e5
eo = 0.5 * (em - ep)
n_inf = em + ep

def create_sphere(x, y, z, radius):  # Hier stand vorher 'r', jetzt 'radius'
    """Erzeugt einen CGA-Kugel-Vektor."""
    s = x*e1 + y*e2 + z*e3
    s4 = 0.5 * ((x**2 + y**2 + z**2) - radius**2)
    return s + s4*n_inf + eo

# 1. Zwei Kugeln definieren, die sich schneiden
S1 = create_sphere(0, 0, 0, radius=3)      # Kugel im Ursprung
S2 = create_sphere(2, 0, 0, radius=3)      # Kugel verschoben auf X-Achse

# 2. Der Schnittkreis als Outer Product (Bivektor)
Circle_Bivector = S1 ^ S2

# 3. Parameter für die Visualisierung extrahieren
d = 2.0  # Abstand der Zentren (Zentrum S1 bei 0, S2 bei 2)
r1, r2 = 3.0, 3.0
x_kreis = (d**2 - r2**2 + r1**2) / (2 * d)
r_kreis = np.sqrt(max(0, r1**2 - x_kreis**2))

# --- Visualisierung ---
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

def plot_sphere(ax, x, y, z, r, col):
    u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:30j]
    xs = x + r * np.cos(u) * np.sin(v)
    ys = y + r * np.sin(u) * np.sin(v)
    zs = z + r * np.cos(v)
    ax.plot_surface(xs, ys, zs, color=col, alpha=0.2, linewidth=0)

# Kugeln zeichnen
plot_sphere(ax, 0, 0, 0, 3, 'cyan')
plot_sphere(ax, 2, 0, 0, 3, 'orange')

# Schnittkreis zeichnen
theta = np.linspace(0, 2*np.pi, 100)
yk = r_kreis * np.cos(theta)
zk = r_kreis * np.sin(theta)
xk = np.full_like(yk, x_kreis)
ax.plot(xk, yk, zk, color='red', linewidth=4, label='Schnittkreis (S1 ∧ S2)')

# Layout-Einstellungen
ax.set_title("CGA: Schnitt zweier Kugeln (Bivektor)")
ax.set_xlabel("E1 (X)")
ax.set_ylabel("E2 (Y)")
ax.set_zlabel("E3 (Z)")
ax.legend()

# Achsen einstellen für bessere Sicht
ax.set_xlim(-4, 6)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)

plt.show()