import numpy as np
import clifford as cf

# Setup der 4D Algebra G(3,0,1)
layout, blades = cf.Cl(3, 0, 1)
g1, g2, g3, g4 = blades['e1'], blades['e2'], blades['e3'], blades['e4']
I = g1 ^ g2 ^ g3 ^ g4 

# Basis-Bivektoren (nach 18.5 / 18.33)
# Achtung: Clifford nutzt e12 statt e1^e2 für kompakte Darstellung
s23, s31, s12 = g2^g3, g3^g1, g1^g2  # Real
s14, s24, s34 = g1^g4, g2^g4, g3^g4  # Dual (Beachte Vorzeichen bei g4)

def create_4d_point(coords):
    """Gleichung 18.33: X = 1 + Ix"""
    # x ist ein 3D Bivektor
    x_bivec = coords[0]*s23 + coords[1]*s31 + coords[2]*s12
    return 1 + (I * x_bivec)

def create_4d_plane(normal_vec, d):
    """Gleichung 18.36: H = n + Id"""
    # n ist der 3D Bivektor der Orientierung
    n = normal_vec[0]*s23 + normal_vec[1]*s31 + normal_vec[2]*s12
    # Sicherstellen, dass n normiert ist (normale euklidische Norm)
    norm_n = np.sqrt(sum(np.square(normal_vec)))
    n_unit = n / norm_n
    
    return n_unit + (I * d)

def run_4d_geometry_demo():
    print("--- 18.4.2 Geometrie in der Motor-Algebra (Korrigiert) ---")
    
    # 1. Punkt bei x=2
    P = create_4d_point([2, 0, 0])
    print(f"Punkt P (erwartet 1 + 2*e14): \n{P}")
    
    # 2. Ebene H (Normalvektor Z, Abstand 5)
    H = create_4d_plane([0, 0, 1], 5)
    print(f"\nEbene H (erwartet e12 + 5*e1234): \n{H}")
    
    # 3. Motor (90 Grad Rotation um Y-Achse -> s31)
    theta = np.pi/2
    M = np.cos(theta/2) - s31 * np.sin(theta/2)
    
    # Transformation
    P_new = M * P * ~M
    H_new = M * H * ~M
    
    print("\n--- Nach 90 Grad Rotation um Y ---")
    print(f"P_neu: {P_new}")
    print(f"H_neu: {H_new}")

if __name__ == "__main__":
    run_4d_geometry_demo()