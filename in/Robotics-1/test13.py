import numpy as np
import clifford as cf

# Setup der 4D Algebra G(3,0,1)
layout, blades = cf.Cl(3, 0, 1)
g1, g2, g3, g4 = blades['e1'], blades['e2'], blades['e3'], blades['e4']
I = g1 ^ g2 ^ g3 ^ g4 

# Basis-Bivektoren
s23, s31, s12 = g2^g3, g3^g1, g1^g2

def create_motor_4d(angle, axis_vec, translation_vec):
    """Erzeugt einen Motor M = T * R"""
    # 1. Rotor R (Rotation)
    theta = angle
    n = axis_vec[0]*s23 + axis_vec[1]*s31 + axis_vec[2]*s12
    R = np.cos(theta/2) - n * np.sin(theta/2)
    
    # 2. Translator T (Translation)
    # t_vec als Vektor, dann Multiplikation mit g4
    t = translation_vec[0]*g1 + translation_vec[1]*g2 + translation_vec[2]*g3
    T = 1 + 0.5 * (g4 * t)
    
    return T * R

def apply_motion(obj, M):
    """
    Universelle Bewegungsformel für Punkte, Linien und Ebenen.
    O' = M * O * ~M
    """
    return M * obj * ~M

# --- Demonstration der Linearität ---
def run_4d_unification_demo():
    print("--- 18.5.2 Unifizierte Bewegung in G3,0,1 ---")
    
    # Motor definieren: 90 Grad um Z, Translation um 1 in X
    M = create_motor_4d(np.pi/2, [0, 0, 1], [1, 0, 0])
    
    # 1. Ein Punkt (1,0,0) -> Eingebettet in 4D
    # X = 1 + I * x_bivec
    P = 1 + I * (1.0 * s23) 
    
    # 2. Eine Linie (Richtung Y, durch Ursprung)
    # L = n + I*m
    L = s31 + 0 # reine Richtung
    
    # 3. Eine Ebene (Normalvektor Z, d=0)
    # H = n + I*d
    H = s12 + 0
    
    # JETZT: Die 'magische' Transformation für alle Objekte
    P_moved = apply_motion(P, M)
    L_moved = apply_motion(L, M)
    H_moved = apply_motion(H, M)
    
    print(f"Punkt transformiert:\n{P_moved}")
    print(f"\nLinie transformiert:\n{L_moved}")
    print(f"\nEbene transformiert:\n{H_moved}")

if __name__ == "__main__":
    run_4d_unification_demo()