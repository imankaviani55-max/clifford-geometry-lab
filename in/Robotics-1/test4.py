import numpy as np
import clifford as cf

# Definition der Algebra G(3,0,1)
layout, blades = cf.Cl(3, 0, 1)

# Basis-Vektoren
g1, g2, g3, g4 = blades['e1'], blades['e2'], blades['e3'], blades['e4']

# Definition der Bivektor-Basis (Gleichung 18.5)
# Euklidische Bivektoren (Rotation)
B_rot = [g2^g3, g3^g1, g1^g2]
# Ideale Bivektoren (Translation / Verschiebung der Achse)
B_trans = [g4^g1, g4^g2, g4^g3]

# Pseudoskalar der 4D Algebra
I = g1 ^ g2 ^ g3 ^ g4

def create_motor(angle_rad, axis_vec, translation_vec):
    """
    Erzeugt einen Motor M = T * R.
    R: Rotor (Rotation um Achse)
    T: Translator (Verschiebung entlang translation_vec)
    """
    # 1. Rotor R (Rotationsteil)
    axis_norm = axis_vec / np.linalg.norm(axis_vec)
    # Bivektor der Rotationsebene (euklidisch)
    phi = (axis_norm[0]*(g2^g3) + axis_norm[1]*(g3^g1) + axis_norm[2]*(g1^g2))
    R = np.cos(angle_rad/2) - phi * np.sin(angle_rad/2)
    
    # 2. Translator T (Translationsteil)
    # Nutzt die Bivektoren mit g4 (Gleichung 18.5)
    t = translation_vec[0]*g1 + translation_vec[1]*g2 + translation_vec[2]*g3
    T = 1 + 0.5 * (g4 * t)
    
    # 3. Motor M = T * R
    M = T * R
    return M

def run_motor_demo():
    print("--- Motor-Algebra Demonstration (G3,0,1+) ---")
    
    # Beispiel: Rotation 90 Grad um Z-Achse UND Verschiebung um 2 Einheiten in X
    angle = np.pi/2
    axis = [0, 0, 1]
    dist = [2, 0, 0]
    
    M = create_motor(angle, axis, dist)
    
    print(f"Konstruierter Motor M:\n{M}")
    
    # Überprüfung der Motor-Eigenschaft: M * ~M = 1
    check = M * ~M
    print(f"\nÜberprüfung M * ~M (sollte 1 sein): {check}")
    
    # Demonstration der Dualität (Gleichung 18.5 Kontext)
    # Der Dual eines euklidischen Bivektors ist ein idealer Bivektor
    print(f"\nDualitätstest: dual(g2^g3) = { (g2^g3) * I }")

if __name__ == "__main__":
    run_motor_demo()