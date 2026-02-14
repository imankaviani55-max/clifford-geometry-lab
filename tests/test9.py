# Installation falls nötig
# pip install clifford numpy

import clifford.g3 as g3
from clifford.g3 import blades

# Basisvektoren
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# --- Geometric Product zwischen zwei Bivektoren ---

B1 = e1 ^ e2             # bivector 1
B2 = (e1 + e2) ^ e3      # bivector 2

# Geometric Product
prod = B1 * B2

# Ausgabe
print("B1 =", B1)
print("B2 =", B2)
print("B1 * B2 =", prod)

# Inner und Outer Product optional anzeigen
inner = 0.5*(B1*B2 + B2*B1)
outer = 0.5*(B1*B2 - B2*B1)
print("Inner Product B1·B2 =", inner)
print("Outer Product B1^B2 =", outer)

# Erklärung:
# Geometric Product von (e1^e2) * ((e1+e2)^e3)
# = (e1^e2)*(e1^e3 + e2^e3)
# = e1e2e1e3 + e1e2e2e3
# = -e2e3 + e1e3
# = -(e2^e3) + (e1^e3)
