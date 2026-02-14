import numpy as np
from clifford.g3c import layout, e1, e2, e3, eo, einf

def erstelle_punkt(v):
    """Erzeugt einen CGA-Punkt (IPNS)"""
    return v + 0.5 * (v**2).value[0] * einf + eo

# --- 1. Definition der Linie (l) - Die grüne Linie ---
a_vec = 0*e1 - 0.5*e2 - 0.5*e3
b_vec = 0*e1 + 2*e2 + 2*e3
A, B = erstelle_punkt(a_vec), erstelle_punkt(b_vec)

# Linie in OPNS: l = a ^ b ^ n (wobei n = einf)
linie_l = A ^ B ^ einf

# --- 2. Definition der Ebene (p) - Der Spiegel ---
c_vec = 2*e1 + 1*e2 + 2*e3
d_vec = 1*e1 - 1*e2 + 1*e3
e_vec = -1.5*e1 - 2*e2 - 1*e3
C, D, E = erstelle_punkt(c_vec), erstelle_punkt(d_vec), erstelle_punkt(e_vec)

# Ebene in OPNS: p = c ^ d ^ e ^ n
ebene_p = C ^ D ^ E ^ einf

# --- 3. Spiegelung (Reflection) ---
# Formel gemäß Text: r = p * l * p
# Hinweis: In Geometric Algebra wird hier das geometrische Produkt verwendet.
# In 'clifford' ist das geometrische Produkt der Standard-Operator '*' oder '*' 

# Zuerst müssen wir die Ebene p in IPNS umwandeln (Vektor-Form), 
# da Spiegelungen an Versoren (IPNS) durchgeführt werden.
p_ipns = ebene_p.dual()

# Reflexion: r = p_ipns * l * p_ipns
reflektierte_linie = p_ipns * linie_l * p_ipns

# --- Analyse der Ergebnisse ---
print("--- Analyse nach Abschnitt 3.6.7 (Spiegelung/Reflection) ---")
print(f"Ursprüngliche Linie l (Grade {linie_l.grades()}): OPNS Trivektor")
print(f"Spiegelebene p (IPNS Vektor)")
print("-" * 60)
print(f"Reflektierte Linie r (MultiVector):\n{reflektierte_linie}")

# Validierung der Dimension
if reflektierte_linie.grades() == {3}:
    print("\nStatus: Die Reflexion war erfolgreich. Das Ergebnis ist wieder eine Linie (Grade 3).")