import numpy as np
import matplotlib.pyplot as plt
from clifford.g3c import layout, e1, e2, e3, e4, e5

# --- Basis-Konfiguration (CGA Setup) ---
ep, em = e4, e5
# eo = Ursprung (Origin), n_inf = Unendlichkeit (Infinity)
# Entspricht den zusätzlichen Basisvektoren im Text
eo = 0.5 * (em - ep)
n_inf = em + ep

def erstelle_punkt(x, y, z):
    """
    Erstellt einen Punkt-Vektor nach Gleichung 3.7:
    X = p + 0.5 * p^2 * n_inf + eo
    Ein Punkt ist eine Kugel mit Radius r = 0.
    """
    p = x*e1 + y*e2 + z*e3
    p_quadrat = x**2 + y**2 + z**2
    return p + 0.5 * p_quadrat * n_inf + eo

def erstelle_ebene(nx, ny, nz, d):
    """
    Erstellt einen Ebenen-Vektor nach Gleichung 3.8:
    Plane = n + d * n_inf
    n = Normalenvektor (n1, n2, n3), d = Abstand zum Ursprung.
    """
    # Normalenvektor normieren
    norm = np.sqrt(nx**2 + ny**2 + nz**2)
    n = (nx/norm)*e1 + (ny/norm)*e2 + (nz/norm)*e3
    return n + d * n_inf

# --- 1. Objekte gemäß Textbeispiel erstellen ---

# Punkt a im Ursprung (Origin)
punkt_a = erstelle_punkt(0, 0, 0)

# Punkt b bei (0, 1, 0)
punkt_b = erstelle_punkt(0, 1, 0)

# Ebene erstellen: Normalenvektor (0,1,0) und Abstand d=1
# Im Textbeispiel: Plane = e2 + n_inf
meine_ebene = erstelle_ebene(0, 1, 0, d=1)

print("-" * 40)
print(f"Punkt A (Ursprung): {punkt_a}")
print(f"Punkt B (0, 1, 0): {punkt_b}")
print(f"Ebene (Normal e2, d=1): {meine_ebene}")
print("-" * 40)

# --- 2. 3D-Visualisierung ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Punkte zeichnen
ax.scatter(0, 0, 0, color='red', s=100, label='Punkt a (Ursprung)')
ax.scatter(0, 1, 0, color='green', s=100, label='Punkt b (0,1,0)')

# Ebene zeichnen
# Da die Normale in Y-Richtung zeigt, liegt die Ebene parallel zur XZ-Fläche
x_bereich = np.linspace(-2, 2, 10)
z_bereich = np.linspace(-2, 2, 10)
X, Z = np.meshgrid(x_bereich, z_bereich)
Y = np.ones_like(X) * 1  # Abstand d = 1

ax.plot_surface(X, Y, Z, color='red', alpha=0.3)

# Normalenvektor zeichnen
ax.quiver(0, 0, 0, 0, 1, 0, color='blue', length=1, label='Normalenvektor (e2)')

# Plot-Einstellungen
ax.set_xlabel('E1 (X)')
ax.set_ylabel('E2 (Y)')
ax.set_zlabel('E3 (Z)')
ax.set_title("CGA Visualisierung: Punkte und Ebenen")
ax.set_xlim(-2, 2); ax.set_ylim(-1, 2); ax.set_zlim(-2, 2)
ax.legend()

plt.show()