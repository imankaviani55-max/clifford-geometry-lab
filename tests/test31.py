import numpy as np
from clifford.g3c import layout, e1, e2, e3, eo, einf

# --- Hilfsfunktionen für CGA-Objekte (Hilfsfunktionen) ---

def erstelle_punkt(p_vec):
    """
    Konvertiert einen euklidischen Vektor in einen Punkt im CGA-Raum.
    Formel: P = p + 0.5 * |p|^2 * einf + eo
    """
    # p_vec**2 در جبر هندسی همان محصول داخلی بردار در خودش است
    return p_vec + 0.5 * (p_vec**2).value[0] * einf + eo

def erstelle_kugel(zentrum_vec, radius):
    """
    Erstellt eine Kugel mit einem Zentrum und einem Radius.
    Formel: S = C - 0.5 * r^2 * einf
    """
    C = erstelle_punkt(zentrum_vec)
    return C - 0.5 * (radius**2) * einf

def erstelle_ebene(normalen_vec, abstand):
    """
    Erstellt eine Ebene mit einem Normalenvektor n und dem Abstand d.
    Formel: pi = n + d * einf
    """
    # اطمینان از واحد بودن بردار نرمال برای محاسبه دقیق فاصله
    n_hat = normalen_vec / np.sqrt(abs((normalen_vec**2).value[0]))
    return n_hat + abstand * einf

# --- Hauptprogramm ---

# 1. Definition der Punkte (Vektoren P und Q)
p_koord = 3*e1 + 4*e2  # Punkt P bei (3, 4, 0)
q_koord = 0*e1 + 0*e2  # Punkt Q im euklidischen Ursprung (0, 0, 0)

P = erstelle_punkt(p_koord)
Q = erstelle_punkt(q_koord)

print("--- CGA Distanz-Berechnungen ---")

# 2. Berechnung des euklidischen Abstands
# P . Q = -0.5 * d^2  => d = sqrt(-2 * (P|Q))
inner_pq = (P | Q).value[0] 
dist_sq = -2 * inner_pq
print(f"1. Euklidischer Abstand zwischen P und Q: {np.sqrt(abs(dist_sq)):.2f}")

# 3. Abstand zwischen Punkt und Ebene
# P | Ebene ergibt den vorzeichenbehafteten orthogonalen Abstand
n = e2  # Normale zeigt nach oben (Y-Achse)
ebene = erstelle_ebene(n, 2)  # Ebene verschoben um 2 Einheiten
abstand_p_ebene = (P | ebene).value[0]
print(f"2. Abstand zwischen Punkt P und Ebene: {abstand_p_ebene:.2f}")

# 4. Position eines Punktes relativ zur Kugel
# S: Zentrum im Ursprung, Radius 2. (Punkt P ist (3,4), also Distanz 5)
S = erstelle_kugel(q_koord, 2)
inner_ps = (P | S).value[0]



print(f"3. Skalarprodukt P . S: {inner_ps:.2f}")
if inner_ps < 0:
    print("   Ergebnis: Der Punkt liegt INNERHALB der Kugel.")
elif inner_ps > 0:
    print("   Ergebnis: Der Punkt liegt AUẞERHALB der Kugel.")
else:
    print("   Ergebnis: Der Punkt liegt AUF der Kugel.")