import numpy as np
from clifford.g3c import layout, e1, e2, e3, eo, einf

def erstelle_punkt(v):
    """Erzeugt einen CGA-Punkt: P = p + 0.5*p^2*einf + eo"""
    return v + 0.5 * (v**2).value[0] * einf + eo

def erstelle_kugel_ipns(zentrum_vec, radius):
    """Erstellt eine Kugel in IPNS-Darstellung: S = C - 0.5*r^2*einf"""
    C = erstelle_punkt(zentrum_vec)
    return C - 0.5 * (radius**2) * einf

# --- 1. Definition der Linie (l) ---
# Punkte a und b gemäß CLUScript
a_vec = 0*e1 - 0.5*e2 - 0.5*e3
b_vec = 0*e1 + 0.5*e2 + 0.5*e3

A = erstelle_punkt(a_vec)
B = erstelle_punkt(b_vec)

# Eine Linie in OPNS: L = A ^ B ^ einf
linie_opns = A ^ B ^ einf

# --- 2. Definition der Kugel (s) ---
# Zentrum (0, 1, 1), Radius r (im CLUScript als -0.1*e angedeutet, hier r=0.45)
zentrum_s = 0*e1 + 1*e2 + 1*e3
S_ipns = erstelle_kugel_ipns(zentrum_s, 0.45)

# --- 3. Berechnung des Schnitts (Meet) ---
# Um den Schnitt zu berechnen, nutzen wir das äußere Produkt 
# zwischen der IPNS-Kugel und der IPNS-Linie.
linie_ipns = linie_opns.dual()
punkt_paar = S_ipns ^ linie_ipns

# --- Analyse der Ergebnisse ---
print("--- Analyse nach Abschnitt 3.6.6.2 (Schnitt Linie-Kugel) ---")
print(f"Linie definiert durch A: {a_vec} und B: {b_vec}")
print(f"Kugel Zentrum: {zentrum_s}")
print("-" * 60)
print(f"Ergebnis (Point Pair MultiVector):\n{punkt_paar}")

# Prüfung der Dimension: 
# Ein Point Pair ist in IPNS ein 3-Blatt (Grade 3)
if 3 in punkt_paar.grades():
    print("\nStatus: Der Schnitt ergab ein Punkt-Paar (Trivektor).")
else:
    print("\nStatus: Kein Punkt-Paar gefunden (vielleicht kein Schnitt).")