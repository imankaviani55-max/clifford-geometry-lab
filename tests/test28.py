import numpy as np
import matplotlib.pyplot as plt
from clifford.g3c import layout, e1, e2, e3, e4, e5

# --- 1. MATHEMATISCHE BASIS-KONFIGURATION ---
# e4**2 = 1, e5**2 = -1 (Minkowski-Metrik für den konformen Raum)
ep, em = e4, e5

# eo: Ursprung (Origin) -> eo = 0.5 * (e- - e+)
eo = 0.5 * (em - ep)

# n_inf: Unendlichkeit (Infinity) -> n_inf = e- + e+
n_inf = em + ep

def erstelle_punkt(x, y, z):
    """
    Ein Punkt X wird in CGA als Vektor dargestellt:
    X = p + 0.5*p²*n_inf + eo
    wobei p = x*e1 + y*e2 + z*e3
    """
    p = x*e1 + y*e2 + z*e3
    p_quadrat = x**2 + y**2 + z**2
    # Formel 3.7 aus deinem Dokument:
    return p + 0.5 * p_quadrat * n_inf + eo

# --- 2. DIE VIER PUNKTE DEFINIEREN (Laut DualSphereN3.clu) ---
A = erstelle_punkt(-0.5, 0, 1)
B = erstelle_punkt(1, -0.5, 2)
C = erstelle_punkt(0, 1.5, 3)
D = erstelle_punkt(0, 2, 2)

# --- 3. BERECHNUNG DER KUGEL (OPNS) ---
# Im Outer Product Null Space (OPNS) wird eine Kugel durch das 
# äußere Produkt von 4 Punkten definiert:
# Sphere_OPNS = A ∧ B ∧ C ∧ D (Ein Quadvektor / Grade 4)
sphere_opns = A ^ B ^ C ^ D

print("="*60)
print("MATHEMATISCHE FORMEL DER KUGEL (QUADVEKTOR):")
print(sphere_opns)
print("="*60)

# --- 4. DUALITÄT: UMRECHNUNG IN DIE VEKTORFORM (IPNS) ---
# Um Radius und Zentrum zu berechnen, wandeln wir den Quadvektor 
# mittels Dual-Operator (*) in einen Vektor (Grade 1) um:
# Sphere_IPNS = *(Sphere_OPNS)
sphere_ipns = sphere_opns.dual()

def get_sphere_params(S):
    """
    Extrahiert Zentrum (s) und Radius (r) aus dem IPNS-Vektor S.
    Normalisierung: S_norm = S / -(S · n_inf)
    """
    # Normalisierung des Vektors, damit der Koeffizient von eo gleich 1 ist
    normalization = -(S | n_inf)[()]
    S_norm = S / normalization
    
    # Zentrum s = s1*e1 + s2*e2 + s3*e3
    center = [(S_norm | e1)[()], (S_norm | e2)[()], (S_norm | e3)[()]]
    
    # Radius r² = s² - 2*s4 (wobei s4 der Koeffizient von n_inf ist)
    s_sq = sum(c**2 for c in center)
    s4 = -(S_norm | eo)[()]
    radius = np.sqrt(abs(s_sq - 2 * s4))
    
    return center, radius

center, radius = get_sphere_params(sphere_ipns)

# --- 5. VISUALISIERUNG ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Zeichnen der 4 Originalpunkte (A, B, C, D)
points = np.array([[-0.5, 0, 1], [1, -0.5, 2], [0, 1.5, 3], [0, 2, 2]])
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'blue', 'green', 'black']

for i in range(len(points)):
    ax.scatter(points[i,0], points[i,1], points[i,2], color=colors[i], s=100, label=f'Punkt {labels[i]}')

# Zeichnen der berechneten Kugeloberfläche
u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:30j]
xs = center[0] + radius * np.cos(u) * np.sin(v)
ys = center[1] + radius * np.sin(u) * np.sin(v)
zs = center[2] + radius * np.cos(v)
ax.plot_surface(xs, ys, zs, color='yellow', alpha=0.2, linewidth=0)

ax.set_title(f"OPNS Kugel: A ∧ B ∧ C ∧ D\nRadius: {radius:.2f}")
ax.legend()
plt.show()