import numpy as np
from clifford.g3c import layout, e1, e2, e3, eo, einf

def erstelle_punkt(v):
    """
    Erstellt einen CGA-Punkt: P = p + 0.5 * p^2 * einf + eo
    Hier ist p5 = 1 (Koeffizient von eo)
    """
    return v + 0.5 * (v**2).value[0] * einf + eo

def erstelle_ebene(n_vec, d):
    """
    Erstellt eine CGA-Ebene: S = n + d * einf
    Hier ist s5 = 0 (kein eo Anteil), wie im Text beschrieben.
    """
    # Normalenvektor n sollte normiert sein
    n_normiert = n_vec / np.sqrt(abs((n_vec**2).value[0]))
    return n_normiert + d * einf

# --- Definition von Punkt und Ebene ---

# Punkt P (z.B. x=5, y=3, z=0)
p_vec = 5*e1 + 3*e2
P = erstelle_punkt(p_vec)

# Ebene S: Normalenvektor n in x-Richtung (e1), Abstand d = 2 vom Ursprung
# Die Ebene ist also die Fläche x = 2
n = e1
d = 2
S = erstelle_ebene(n, d)

# --- Berechnung des Abstands ---
# Laut Text Gleichung 3.9: P · S = p · n - d
abstand_cga = (P | S).value[0]

# Direkte euklidische Berechnung zum Vergleich:
# Abstand = (5 * 1) - 2 = 3
abstand_euklid = (p_vec | n).value[0] - d

# --- Ausgabe der Ergebnisse ---
print("--- Analyse nach Abschnitt 3.6.5.2 ---")
print(f"Punkt P Koordinate: {p_vec}")
print(f"Ebene S: Normalenvektor = {n}, Abstand d = {d}")
print("-" * 45)
print(f"Skalarprodukt (P · S) in CGA: {abstand_cga:.2f}")
print(f"Euklidische Berechnung (p·n - d): {abstand_euklid:.2f}")

# Interpretation des Vorzeichens
if abstand_cga > 0:
    print("\nDer Punkt liegt auf der Seite, in die der Normalenvektor zeigt.")
elif abstand_cga < 0:
    print("\nDer Punkt liegt auf der gegenüberliegenden Seite der Ebene.")
else:
    print("\nDer Punkt liegt direkt auf der Ebene.")