import numpy as np
import clifford as cf

# Setup der 4D Algebra G(3,0,1)
layout, blades = cf.Cl(3, 0, 1)
g1, g2, g3, g4 = blades['e1'], blades['e2'], blades['e3'], blades['e4']
I_4d = g1 ^ g2 ^ g3 ^ g4 

# Hilfs-Bivektoren für 3D-Strukturen innerhalb von 4D
s23, s31, s12 = g2^g3, g3^g1, g1^g2

def create_motor(angle, axis, t_vec):
    """Erzeugt einen Motor M = T*R"""
    # Rotor
    n = axis[0]*s23 + axis[1]*s31 + axis[2]*s12
    R = np.cos(angle/2) - n * np.sin(angle/2)
    # Translator
    t = t_vec[0]*g1 + t_vec[1]*g2 + t_vec[2]*g3
    T = 1 + 0.5 * (g4 * t)
    return T * R

# --- Implementierung der 4D-Repräsentationen ---

def get_4d_point(x_vec):
    """Gleichung 18.33: X = 1 + I*x (x als 3D-Bivektor)"""
    x_bivec = x_vec[0]*s23 + x_vec[1]*s31 + x_vec[2]*s12
    return 1 + (I_4d * x_bivec)

def get_4d_line(n_vec, m_vec):
    """Gleichung 18.34: L = n + I*m"""
    n = n_vec[0]*s23 + n_vec[1]*s31 + n_vec[2]*s12
    m = m_vec[0]*s23 + m_vec[1]*s31 + m_vec[2]*s12
    return n + (I_4d * m)

def get_4d_plane(normal_vec, d):
    """Gleichung 18.36: H = n + I*d"""
    n = normal_vec[0]*s23 + normal_vec[1]*s31 + normal_vec[2]*s12
    return n + (I_4d * d)

# --- Die Transformation ---

def run_linear_motion_test():
    # Motor: 90 Grad um Z-Achse, Translation um 2 Einheiten in X
    M = create_motor(np.pi/2, [0, 0, 1], [2, 0, 0])
    
    # Objekte definieren
    P = get_4d_point([1, 0, 0])     # Punkt bei x=1
    L = get_4d_line([0, 1, 0], [0, 0, 0]) # Linie: Y-Achse
    H = get_4d_plane([1, 0, 0], 3)  # Ebene: x=3 (Normalvektor e1, Distanz 3)
    
    # Gleichung 18.40, 18.41, 18.42: Alle nutzen M * O * ~M
    # In G(3,0,1) ist das Inverse eines Einheitsmotors gleich seinem Revers (~M)
    Mt = ~M 
    
    P_prime = M * P * Mt
    L_prime = M * L * Mt
    H_prime = M * H * Mt
    
    print("--- 18.5.2 Linearisierte 4D Transformationen ---")
    print(f"Punkt' (18.40):\n{P_prime}")
    print(f"\nLinie' (18.41):\n{L_prime}")
    print(f"\nEbene' (18.42):\n{H_prime}")

if __name__ == "__main__":
    run_linear_motion_test()