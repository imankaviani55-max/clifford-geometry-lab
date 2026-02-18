import numpy as np
from clifford.g3 import layout

# In clifford.g3 sind die Basisvektoren standardmäßig e1, e2, e3
# Wir weisen sie den Namen aus deinem Buchkapitel (sigma) zu
blades = layout.blades
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# Das Einheits-Pseudoskalar I (Gleichung 18.1)
I = e1 ^ e2 ^ e3 

def run_demonstration_de():
    print("--- Ergebnisse der Geometrischen Algebra (G3,0,0) ---")
    
    # 1. Darstellung der Bivektor-Basis (Gleichung 18.1)
    print(f"Bivektor sigma12: {e1 ^ e2}")
    print(f"Bivektor sigma23: {e2 ^ e3}")
    print(f"Bivektor sigma31: {e3 ^ e1}")
    
    # 2. Überprüfung der Pseudoskalar-Eigenschaft (I^2 = -1)
    i_sq = I**2
    print(f"\nPseudoskalar I: {I}")
    print(f"Eigenschaft: I^2 = {i_sq}")
    
    # 3. Das äußere Produkt und das Volumenelement (lambda * I)
    # Beispielvektoren für die Robotik-Anwendung
    a = 2 * e1
    b = 3 * e2
    c = 1 * e3
    
    volumenelement = a ^ b ^ c
    print(f"\nÄußeres Produkt (a ^ b ^ c): {volumenelement}")
    
    # Extraktion von lambda
    lambd = float(volumenelement / I)
    print(f"Skalarer Wert (Volumen lambda): {lambd}")

if __name__ == "__main__":
    run_demonstration_de()