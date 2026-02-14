# Installation falls nötig
# pip install clifford numpy

import clifford.g3 as g3
from clifford.g3 import blades
import numpy as np

# Basisvektoren
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# --- Inner Product von Vektoren ---

# Beispiel 1: Länge eines Vektors
B = e1 + e2
length = np.sqrt(float(B | B))  # B | B ist das Skalarprodukt in GA
print("Vector B =", B)
print("Länge von B =", length)

# Beispiel 2: Perpendicularität prüfen
norm = float(e1 | e2)  # e1 · e2
print("Inneres Produkt e1 · e2 =", norm)
if norm == 0:
    print("e1 und e2 sind senkrecht (perpendicular).")
else:
    print("e1 und e2 sind nicht senkrecht.")
