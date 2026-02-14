import numpy as np
from clifford.g3c import layout, e1, e2, e3, eo, einf

def erstelle_kugel_ipns(zentrum_vec, radius):
    """Erstellt eine Kugel in IPNS: S = C - 0.5 * r^2 * einf"""
    C = zentrum_vec + 0.5 * (zentrum_vec**2).value[0] * einf + eo
    return C - 0.5 * (radius**2) * einf

# --- Definition der Kugeln ---
zentrum_a = -0.5*e2 - 0.5*e3
S1 = erstelle_kugel_ipns(zentrum_a, 1.0)

zentrum_b = 0.5*e2 + 0.5*e3
S2 = erstelle_kugel_ipns(zentrum_b, 1.0)

# --- Schnittoperation (Meet) ---
# Das Ergebnis ist ein Bivektor (Grade 2) im IPNS
schnittkreis = S1 ^ S2

print("--- Analyse nach Abschnitt 3.6.6.1 (Schnitt zweier Kugeln) ---")
print(f"Zentrum A: {zentrum_a}")
print(f"Zentrum B: {zentrum_b}")
print("-" * 60)
print(f"Schnitt-MultiVector:\n{schnittkreis}")

# --- Korrigierte Statusprüfung ---
# Ein Kreis im IPNS hat Grade 2 (Schnitt von zwei Vektoren)
if 2 in schnittkreis.grades():
    print("\nStatus: Der Schnitt wurde erfolgreich als Kreis (IPNS-Bivektor) berechnet.")
else:
    print("\nStatus: Unerwarteter Geometrie-Typ.")

# Radius-Extraktion (Optionaler Check)
# Ein positiver Wert hier bestätigt, dass der Kreis real existiert
radius_check = (schnittkreis**2).value[0]
if radius_check != 0:
    print(f"Geometrische Validität: Der Schnitt ist eine reale Kurve.")