import numpy as np
from clifford.g3 import layout

# Basis-Blades extrahieren
blades = layout.blades
e1, e2, e3 = blades['e1'], blades['e2'], blades['e3']
I = e1 ^ e2 ^ e3 # Pseudoskalar

def check_hamilton_relations():
    """Überprüft die Hamilton-Beziehungen (i^2 = j^2 = k2 = ijk = -1)"""
    # Definition nach Text: i=I*e1, j=-I*e2, k=I*e3
    i = I * e1
    j = -I * e2
    k = I * e3
    
    print("--- Hamilton Relationen (Gleichung 18.2 Kontext) ---")
    print(f"i^2: {i*i}")
    print(f"j^2: {j*j}")
    print(f"k^2: {k*k}")
    print(f"ijk: {i*j*k}")

def apply_rotation(vector, angle_deg, axis_vector):
    """
    Implementiert Gleichung 18.3: R = cos(theta/2) + n*sin(theta/2)
    Wendet die Rotation via RaR~ an.
    """
    theta = np.radians(angle_deg)
    
    # 1. Achse als Bivektor (Einheits-Bivektor n)
    # n muss ein Einheits-Bivektor sein, der die Rotationsebene beschreibt
    axis_norm = axis_vector / np.linalg.norm(axis_vector)
    # Der Bivektor n ist das Dual der Rotationsachse: n = I * axis
    n = I * (axis_norm[0]*e1 + axis_norm[1]*e2 + axis_norm[2]*e3)
    
    # 2. Rotor Konstruktion (Gleichung 18.3)
    R = np.cos(theta/2) + n * np.sin(theta/2)
    
    # 3. Rotation anwenden: b = R * a * ~R (Sandwich-Produkt)
    # ~R ist die Konjugation (Reverse)
    a_rotated = R * vector * ~R
    
    return R, a_rotated

def run_rotor_demo():
    # Beispiel: Drehe den Vektor e1 um 90 Grad um die e3-Achse
    # Das Ergebnis sollte e2 sein.
    v = e1
    angle = 90
    axis = [0, 0, 1] # Z-Achse
    
    rotor, v_new = apply_rotation(v, angle, axis)
    
    print("\n--- Rotor Demonstration ---")
    print(f"Ursprünglicher Vektor: {v}")
    print(f"Konstruierter Rotor R: {rotor}")
    print(f"Rotierter Vektor: {v_new}")

if __name__ == "__main__":
    check_hamilton_relations()
    run_rotor_demo()