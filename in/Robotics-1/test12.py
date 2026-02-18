import numpy as np
from clifford.g3 import layout

blades = layout.blades
e1, e2, e3 = blades['e1'], blades['e2'], blades['e3']
I = e1 ^ e2 ^ e3

def move_point_3d(x, R, t):
    """Gleichung 18.37: x' = R*x*~R + t"""
    return R * x * ~R + t

def move_line_3d(l, R, t):
    """
    Gleichung 18.38: Transformation einer Linie.
    l ist n + m (Richtung + Moment)
    """
    n = l(1) # Extrahiere Vektor-Teil (Richtung)
    m = l(2) # Extrahiere Bivektor-Teil (Moment)
    
    n_prime = R * n * ~R
    # Das neue Moment m' berechnet sich aus Rotation + Translationseinfluss
    m_prime = R * m * ~R + (t ^ n_prime)
    
    return n_prime + m_prime

def move_plane_3d(h, R, t):
    """
    Gleichung 18.39: Transformation einer Ebene.
    h ist n_bivec + I*d
    """
    n_bivec = h(2)
    d_val = float(h(3) / I)
    
    n_prime = R * n_bivec * ~R
    # Die neue Hesse-Distanz d' (Skalar)
    # d' = d + (t . n_prime_vector)
    # In GA: t ^ n_prime ist der Trivektor-Zusatz
    h_prime_trivector = (R * (I * d_val) * ~R) + (t ^ n_prime)
    
    return n_prime + h_prime_trivector

# --- Test ---
def run_3d_motion_demo():
    print("--- 18.5.1 Bewegung in G3,0,0 (Euklidisch) ---")
    
    # Setup: 90 Grad Rotation um Z, Translation um 1 in X
    theta = np.pi/2
    R = np.cos(theta/2) - (e1^e2) * np.sin(theta/2)
    t = 1.0 * e1
    
    # 1. Punkt bei (1,0,0)
    x = 1.0 * e1
    x_prime = move_point_3d(x, R, t)
    print(f"Punkt' (erwartet [1,1,0]):\n{x_prime}")
    
    # 2. Linie (Richtung e2, durch Ursprung)
    l = 1.0 * e2 + 0*(e1^e2)
    l_prime = move_line_3d(l, R, t)
    print(f"\nLinie' (Richtung + Moment):\n{l_prime}")
    
    # 3. Ebene (XZ-Ebene, d=0)
    h = (e3^e1) + 0*I
    h_prime = move_plane_3d(h, R, t)
    print(f"\nEbene' (Bivektor + Trivektor):\n{h_prime}")

if __name__ == "__main__":
    run_3d_motion_demo()