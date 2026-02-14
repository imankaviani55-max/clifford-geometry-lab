# Installation falls nötig
# pip install clifford numpy

import clifford.g3 as g3
from clifford.g3 import blades
from clifford.g3 import layout

# Basisvektoren
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

# Pseudoscalar (Trivector)
I = e1 ^ e2 ^ e3

# --- Example 1: Inverse eines Vektors ---
v = 2*e1
v_inv = 1/v  # Inverse in clifford
print("Vektor v =", v)
print("Inverse von v =", v_inv)
# Prüfung: v * v_inv
print("v * v_inv =", v*v_inv)  # sollte 1 sein

# --- Example 2: Inverse des Pseudoskalar ---
I_inv = 1/I
print("Pseudoscalar I =", I)
print("Inverse von I =", I_inv)
# Prüfung: I * I_inv
print("I * I_inv =", I*I_inv)  # sollte 1 sein (negativ multipliziert, siehe Buch)
