import numpy as np
from clifford.g3c import layout, e1, e2, e3, eo, einf

def erstelle_punkt(v):
    """Erzeugt einen CGA-Punkt: P = p + 0.5*p^2*einf + eo"""
    return v + 0.5 * (v**2).value[0] * einf + eo

# --- 1. Definition der Linie (l) ---
a_vec = 0*e1 - 0.5*e2 - 0.5*e3
b_vec = 0*e1 + 0.5*e2 + 0.5*e3
A, B = erstelle_punkt(a_vec), erstelle_punkt(b_vec)

# Linie in OPNS: L = A ^ B ^ einf
linie_opns = A ^ B ^ einf

# --- 2. Definition der Ebene (p) ---
c_vec = 2*e1 + 1*e2 + 2*e3
d_vec = 1*e1 - 1*e2 + 1*e3
e_vec = -1*e1 - 2*e2 - 1*e3
C, D, E = erstelle_punkt(c_vec), erstelle_punkt(d_vec), erstelle_punkt(e_vec)

# Ebene in OPNS: P = C ^ D ^ E ^ einf
ebene_opns = C ^ D ^ E ^ einf

# --- 3. Schnittberechnung (Meet-Operation) ---
# Um den Schnittpunkt r zu finden, nutzen wir das äußere Produkt 
# der dualen Darstellungen (IPNS).
# r = dual(P) ^ dual(L)
ebene_ipns = ebene_opns.dual()
linie_ipns = linie_opns.dual()

schnittpunkt_r = ebene_ipns ^ linie_ipns

# --- Analyse der Ergebnisse ---
print("--- Analyse nach Abschnitt 3.6.6.3 (Schnitt Linie-Ebene) ---")
print(f"Linie definiert durch A, B und einf")
print(f"Ebene definiert durch C, D, E und einf")
print("-" * 60)
print(f"Schnittpunkt R (MultiVector):\n{schnittpunkt_r}")

# Ein Punkt ist in IPNS ein 4-Blatt (Quadvector)
if 4 in schnittpunkt_r.grades():
    print("\nStatus: Der Schnitt ergab einen Punkt (Quadvector in IPNS).")
    
    # Normalisierung des Punktes (eo-Koeffizient auf 1 setzen)
    # Ein CGA-Punkt P ist korrekt skaliert, wenn P | einf = -1
    faktor = -(schnittpunkt_r | einf).value[0]
    if abs(faktor) > 1e-10:
        punkt_normiert = schnittpunkt_r / faktor
        print(f"Normierter Schnittpunkt:\n{punkt_normiert}")