import numpy as np
from clifford.g3c import layout, e1, e2, e3, eo, einf

def erstelle_punkt(v):
    """
    Erstellt einen CGA-Punkt gemäß der Definition im Text:
    P = p + 0.5 * p^2 * einf + eo
    """
    return v + 0.5 * (v**2).value[0] * einf + eo

# --- Definition der zwei Punkte ---
# Punkt p (z.B. bei x=3, y=4)
p_vec = 3*e1 + 4*e2
P = erstelle_punkt(p_vec)

# Punkt s (z.B. im Ursprung)
s_vec = 0*e1 + 0*e2
S = erstelle_punkt(s_vec)

# --- Berechnung nach Gleichung 3.9 ---
# P · S (Skalarprodukt in CGA)
skalarprodukt_ps = (P | S).value[0]

# --- Berechnung der euklidischen Distanz ---
# Gemäß Text: (s - p)^2 = -2 * (P · S)
distanz_quadrat_cga = -2 * skalarprodukt_ps

# Direkte euklidische Berechnung zum Vergleich:
diff_vec = s_vec - p_vec
distanz_quadrat_euklid = (diff_vec**2).value[0]

# --- Ausgabe der Ergebnisse ---
print("--- Analyse nach Abschnitt 3.6.5.1 ---")
print(f"Punkt P: {p_vec}")
print(f"Punkt S: {s_vec}")
print("-" * 40)
print(f"Skalarprodukt (P · S): {skalarprodukt_ps:.2f}")
print(f"Berechnetes Quadrat der Distanz (-2 * P·S): {distanz_quadrat_cga:.2f}")
print(f"Euklidisches Quadrat der Distanz (s-p)^2: {distanz_quadrat_euklid:.2f}")

# Validierung
if np.isclose(distanz_quadrat_cga, distanz_quadrat_euklid):
    print("\nErfolg: Die CGA-Formel stimmt mit der euklidischen Distanz überein!")

# Finaler Abstand
print(f"Der Abstand zwischen den Punkten ist: {np.sqrt(distanz_quadrat_cga):.2f}")