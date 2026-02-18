import numpy as np
import clifford as cf

# Setup der Algebra G(3,0,1)
layout, blades = cf.Cl(3, 0, 1)
g1, g2, g3, g4 = blades['e1'], blades['e2'], blades['e3'], blades['e4']
I = g1 ^ g2 ^ g3 ^ g4  # Pseudoskalar

def create_pure_rotor(angle_rad, axis_vec):
    """Gleichung 18.6: Einfacher Rotor R"""
    axis_norm = axis_vec / np.linalg.norm(axis_vec)
    n = (axis_norm[0]*(g2^g3) + axis_norm[1]*(g3^g1) + axis_norm[2]*(g1^g2))
    return np.cos(angle_rad/2) - n * np.sin(angle_rad/2)

def translate_rotor_axis(R, tc_vec):
    """Gleichung 18.7: Verschiebt die Rotationsachse um tc (R_s = Tc R ~Tc)"""
    tc = tc_vec[0]*g1 + tc_vec[1]*g2 + tc_vec[2]*g3
    Tc = 1 + 0.5 * (g4 * tc)
    return Tc * R * ~Tc

def create_motor_dual_angle(angle, d, axis_vec, tc_vec):
    """Gleichung 18.12: Motor via dualem Winkel M = cos(theta/2 + I*d/2) + sin(...)l"""
    theta = angle
    # 1. Bestimme die Linienachse l (Richtung n und Moment m)
    axis_norm = axis_vec / np.linalg.norm(axis_vec)
    n = (axis_norm[0]*(g2^g3) + axis_norm[1]*(g3^g1) + axis_norm[2]*(g1^g2))
    
    tc = tc_vec[0]*g1 + tc_vec[1]*g2 + tc_vec[2]*g3
    # m = n ^ tc (Momententeil der Linie)
    # Beachte: Da tc ein Vektor und n ein Bivektor ist, nutzen wir das geometrische Produkt
    # Der Text nutzt l = n + Im
    m = n ^ tc 
    l = n + (I * m)
    
    # 2. Duale Terme (Taylor Expansion f(a + Ib) = f(a) + I f'(a) b)
    # Realteil: cos(theta/2), Dualteil: -sin(theta/2) * d/2
    term_cos = np.cos(theta/2) - (I * np.sin(theta/2) * (d/2))
    # Realteil: sin(theta/2), Dualteil: cos(theta/2) * d/2
    term_sin = np.sin(theta/2) + (I * np.cos(theta/2) * (d/2))
    
    M = term_cos + term_sin * l
    return M

def run_kinematics_demo():
    print("--- 18.3.2 Motoren und Schraubenbewegungen ---")
    
    angle = np.pi/2 # 90 Grad
    d = 1.0         # Verschiebung entlang der Achse (Pitch)
    axis = [0, 0, 1] # Z-Achse
    tc = [2, 0, 0]   # Achse ist um 2 Einheiten in X verschoben
    
    # Weg A: Über explizite Transformation der Achse
    R = create_pure_rotor(angle, axis)
    Rs = translate_rotor_axis(R, tc)
    
    # Weg B: Über die duale Winkel-Formel (Gleichung 18.12)
    M = create_motor_dual_angle(angle, d, axis, tc)
    
    print(f"Rotor an verschobener Achse (Rs):\n{Rs}")
    print(f"\nVollständiger Motor (M):\n{M}")
    
    # Test: Ein Motor bewegt einen Punkt sowohl rotatorisch als auch translatorisch
    # Punkt im Ursprung (in G3,0,1 oft als 1 + g4*x dargestellt)
    p = 1 + g4 * (1*g1) # Punkt bei (1,0,0)
    p_transformed = M * p * ~M
    print(f"\nTransformierter Punkt (Rohdaten):\n{p_transformed}")

if __name__ == "__main__":
    run_kinematics_demo()