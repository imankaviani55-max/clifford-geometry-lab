import numpy as np
from clifford.g3c import layout, e1, e2, e3, eo, einf

def erstelle_punkt(v):
    """
    Erstellt einen CGA-Punkt: P = p + 0.5 * p^2 * einf + eo
    Hier ist p4 = 0.5*p^2 und p5 = 1
    """
    return v + 0.5 * (v**2).value[0] * einf + eo

def erstelle_kugel(zentrum_vec, radius):
    """
    Erstellt eine CGA-Kugel gemäß Abschnitt 3.6.5.3:
    s4 = 0.5 * (s^2 - r^2), s5 = 1
    Formel: S = s + 0.5 * (s^2 - r^2) * einf + eo
    """
    s_quadrat = (zentrum_vec**2).value[0]
    r_quadrat = radius**2
    return zentrum_vec + 0.5 * (s_quadrat - r_quadrat) * einf + eo

# --- Test-Szenario ---

# 1. Definieren der Kugel (S)
# Zentrum s bei (0,0,0), Radius r = 3
s_vec = 0*e1 + 0*e2 + 0*e3
r = 3
S = erstelle_kugel(s_vec, r)

# 2. Definieren von Test-Punkten (P)
punkte = {
    "Punkt A (Innen)": 1*e1 + 1*e2,      # Distanz^2 = 2 < 9
    "Punkt B (Auf Oberfläche)": 3*e1,    # Distanz^2 = 9
    "Punkt C (Außen)": 4*e1 + 3*e2       # Distanz^2 = 25 > 9
}

print(f"--- Analyse nach Abschnitt 3.6.5.3 (Kugel-Check) ---")
print(f"Kugel-Radius: {r}")
print("-" * 50)

for name, p_vec in punkte.items():
    P = erstelle_punkt(p_vec)
    
    # Skalarprodukt P · S (Gleichung 3.9 im Text)
    # Laut Text: P·S > 0 (Innen), P·S < 0 (Außen)
    ergebnis_ps = (P | S).value[0]
    
    status = ""
    if ergebnis_ps > 1e-10: # Toleranz für Fließkommazahlen
        status = "INNERHALB der Kugel (P·S > 0)"
    elif ergebnis_ps < -1e-10:
        status = "AUẞERHALB der Kugel (P·S < 0)"
    else:
        status = "AUF der Kugel (P·S = 0)"
        
    print(f"{name}:")
    print(f"  P·S = {ergebnis_ps:7.2f}  --> {status}")