import numpy as np
import matplotlib.pyplot as plt
from clifford.g3c import layout, e1, e2, e3, e4, e5

# --- 1. CGA BASIS-KONFIGURATION ---
ep, em = e4, e5
# eo = Ursprung, n_inf = Unendlichkeit
eo = 0.5 * (em - ep)
n_inf = em + ep

def create_sphere(x, y, z, radius):
    """Erzeugt einen CGA-Kugel-Vektor aus Zentrum und Radius."""
    # Punkt s im euklidischen Raum
    s = x*e1 + y*e2 + z*e3
    # s4 nach der Formel aus deinem Dokument: 0.5 * (s^2 - r^2)
    s_sq = x**2 + y**2 + z**2
    s4 = 0.5 * (s_sq - radius**2)
    return s + s4*n_inf + eo

# --- 2. OBJEKTE ERSTELLEN ---
# Wir erstellen zwei Kugeln, die sich schneiden
# S1: Zentrum (0,0,0), Radius 3
S1 = create_sphere(0, 0, 0, radius=3)
# S2: Zentrum (2,0,0), Radius 3
S2 = create_sphere(2, 0, 0, radius=3)

# Der Schnittkreis als Bivektor (Outer Product)
Circle_Bivector = S1 ^ S2

# --- 3. KORREKTE AUSGABE DER KOMPONENTEN ---
print("="*50)
print("CGA SCHNITTKREIS FORMEL (BIVEKTOR):")
print(Circle_Bivector)
print("="*50)

print("\nRelevante Komponenten des Kreises:")
# Die Methode .blades() gibt ein Dictionary zurück
try:
    blades_dict = Circle_Bivector.blades()
    for name, mv in blades_dict.items():
        # Extrahiere den Skalarwert aus dem Multivektor
        coeff = float(mv) 
        if abs(coeff) > 0.0001:
            print(f"Blade {name:10} : {coeff:.4f}")
except Exception as e:
    print(f"Hinweis zur Ausgabe: {e}")
print("="*50)

# --- 4. GEOMETRISCHE EXTRAKTION FÜR DEN PLOT ---
# Mathematische Ableitung der Kreisposition im 3D-Raum:
d = 2.0  # Abstand der Zentren (0 bis 2 auf der X-Achse)
r1, r2 = 3.0, 3.0
# X-Position der Schnittebene:
x_kreis = (d**2 - r2**2 + r1**2) / (2 * d)
# Radius des Schnittkreises:
r_kreis = np.sqrt(max(0, r1**2 - x_kreis**2))

# --- 5. 3D-VISUALISIERUNG ---
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

def plot_sphere(ax, x, y, z, r, col, label):
    """Hilfsfunktion zum Zeichnen einer Kugel"""
    u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:30j]
    xs = x + r * np.cos(u) * np.sin(v)
    ys = y + r * np.sin(u) * np.sin(v)
    zs = z + r * np.cos(v)
    ax.plot_surface(xs, ys, zs, color=col, alpha=0.15, linewidth=0)
    ax.scatter(x, y, z, color=col, s=50, label=label)

# Kugeln zeichnen
plot_sphere(ax, 0, 0, 0, 3, 'blue', 'Kugel S1 (Ursprung)')
plot_sphere(ax, 2, 0, 0, 3, 'orange', 'Kugel S2 (Verschoben)')

# Schnittkreis zeichnen (liegt in der YZ-Ebene bei x_kreis)
theta = np.linspace(0, 2*np.pi, 100)
yk = r_kreis * np.cos(theta)
zk = r_kreis * np.sin(theta)
xk = np.full_like(yk, x_kreis)
ax.plot(xk, yk, zk, color='red', linewidth=4, label='Schnittkreis (S1 ^ S2)')

# Plot-Einstellungen
ax.set_title("CGA: Visualisierung des Schnittkreises zweier Kugeln")
ax.set_xlabel("E1 (X)")
ax.set_ylabel("E2 (Y)")
ax.set_zlabel("E3 (Z)")
ax.legend()

# Achsen fixieren für korrekte Proportionen
limit = 5
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit, limit)

plt.show()