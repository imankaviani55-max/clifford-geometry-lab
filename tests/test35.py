import numpy as np
from clifford.g3c import layout, e1, e2, e3, eo, einf

def erstelle_punkt(v):
    """
    Erzeugt einen Punkt im CGA-Raum (Conformal Geometric Algebra).
    Entspricht der homogenen Darstellung eines euklidischen Vektors.
    """
    return v + 0.5 * (v**2).value[0] * einf + eo

# --- Definition der Punkte (gemäß CLUScript PointInsideCircleN3.clu) ---
# Vektoren für die Ecken des Dreiecks A, B und C
A = erstelle_punkt(-0.5*e1 + 0*e2 + 1*e3)
B = erstelle_punkt(1*e1 - 0.5*e2 + 2*e3)
C = erstelle_punkt(0*e1 + 1.5*e2 + 3*e3)

# Testpunkt X (Der Punkt, dessen Position geprüft werden soll)
X = erstelle_punkt(0*e1 + 4*e2 + 4*e3)

# --- Konstruktion des Umkreises (Circumcircle) ---
# Das äußere Produkt (Wedge ^) von 3 Punkten ergibt einen Kreis in OPNS-Darstellung.
kreis_opns = A ^ B ^ C

# Um das Skalarprodukt für Distanztests zu nutzen, transformieren wir 
# den Kreis in die IPNS-Darstellung (Dualisierung).
# Entspricht dem '*' Operator in CLUCalc.
kreis_ipns = kreis_opns.dual()

# --- Konstruktion der Kugel (Sphere) ---
# Ein Kreis in CGA kann als Schnittmenge einer Kugel und einer Ebene betrachtet werden.
# Wir nutzen das Dual des Dreiecks-Spatprodukts für den Umkugel-Test.
umkugel_ipns = (A ^ B ^ C).dual()

# --- Berechnung und Auswertung (Statusprüfung) ---
# Das Skalarprodukt (Inner Product '|') bestimmt die Lage des Punktes X zur Kugel.
ergebnis = (X | umkugel_ipns).value[0]

print("--- Analyse nach Abschnitt 3.6.5.4 (Umkreis-Check) ---")
print(f"Ergebnis des Skalarprodukts (X | Kugel): {ergebnis:.4f}")

# --- Interpretation der Ergebnisse gemäß der Konvention aus 3.6.5.3 ---
# P · S > 0 : Punkt liegt innerhalb
# P · S < 0 : Punkt liegt außerhalb
# P · S = 0 : Punkt liegt exakt auf dem Kreis

print("-" * 50)
if ergebnis > 1e-10:
    print("Status: Der Punkt X liegt INNERHALB des Umkreises.")
elif ergebnis < -1e-10:
    print("Status: Der Punkt X liegt AUẞERHALB des Umkreises.")
else:
    print("Status: Der Punkt X liegt exakt AUF dem Umkreis.")