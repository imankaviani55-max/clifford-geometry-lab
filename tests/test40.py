import numpy as np
from clifford.g3c import layout, e1, e2, e3, eo, einf

def erstelle_punkt(v):
    """Erzeugt einen CGA-Punkt (IPNS)"""
    return v + 0.5 * (v**2).value[0] * einf + eo

# --- 1. Definition der Linie (l) - Die grüne Linie ---
a_vec = 0*e1 - 0.5*e2 - 0.5*e3
b_vec = 0*e1 + 2*e2 + 2*e3
A, B = erstelle_punkt(a_vec), erstelle_punkt(b_vec)

# Linie in OPNS: l = a ^ b ^ n
linie_l = A ^ B ^ einf

# --- 2. Definition der Ebene (p) - Die Projektionsfläche ---
c_vec = 2*e1 + 1*e2 + 2*e3
d_vec = 1*e1 - 1*e2 + 1*e3
e_vec = -1.5*e1 - 2*e2 - 1*e3
C, D, E = erstelle_punkt(c_vec), erstelle_punkt(d_vec), erstelle_punkt(e_vec)

# Ebene in OPNS: p = c ^ d ^ e ^ n
ebene_p_opns = C ^ D ^ E ^ einf

# --- 3. Projektion ---
# Formel gemäß Text: r = (p . l) / p
# In CGA führen wir Projektionen meist mit der IPNS-Darstellung der Ebene durch.

p_ipns = ebene_p_opns.dual()

# Berechnung der Projektion: r = (p_ipns | l) * p_ipns.inv()
# (Hinweis: Für einen Einheitsvektor p ist p.inv() = p)
projektion_r = (p_ipns | linie_l) * p_ipns.inv()

# --- Analyse der Ergebnisse ---
print("--- Analyse nach Abschnitt 3.6.8 (Projektion) ---")
print(f"Ursprüngliche Linie l (Grade 3 in OPNS)")
print(f"Projektionsebene p (Grade 1 in IPNS)")
print("-" * 60)
print(f"Projizierte Linie r (MultiVector):\n{projektion_r}")



# Überprüfung der Dimension
if projektion_r.grades() == {3}:
    print("\nStatus: Die Projektion war erfolgreich. Das Ergebnis ist eine Linie (Grade 3).")