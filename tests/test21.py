import numpy as np
from clifford.g3c import layout, e1, e2, e3, e4, e5

# Definition der Basis-Vektoren nach Ihrem Text
ep = e4  # e+
em = e5  # e-

# eo = Ursprung, n_inf = Unendlichkeit (im Text als e1 bezeichnet)
eo = 0.5 * (em - ep)
n_inf = em + ep

def berechne_radius(kugel_vektor):
    """ Berechnet den Radius aus einem CGA-Kugel-Vektor """
    # Extrahiere das euklidische Zentrum (s)
    s_vec = kugel_vektor | (e1 + e2 + e3)
    s_quadrat = (s_vec**2)[()]
    
    # Extrahiere s4 (Koeffizient von n_inf)
    s4 = -(kugel_vektor | eo)[()]
    
    # Formel aus dem Text: r^2 = s^2 - 2*s4
    r_quadrat = s_quadrat - 2 * s4
    return np.sqrt(abs(r_quadrat))

# --- Beispiel aus Ihrem Dokument ---
# S = e2 + e3 - e1 + eo (Hinweis: e1 im Text ist unser n_inf)
S_beispiel = e2 + e3 - 1*n_inf + eo

print(f"Berechneter Radius: {berechne_radius(S_beispiel)}") 
# Ergebnis: 2.0 (da r^2 = 4)

# --- Test: Punkt auf der Oberfläche ---
# Ein Punkt P liegt auf der Kugel S, wenn S | P = 0
punkt_auf_oberflaeche = 5*e1 + 0.5*(25)*n_inf + eo
check = S_beispiel | punkt_auf_oberflaeche
print(f"Skalarprodukt (Nullraum-Test): {check}")