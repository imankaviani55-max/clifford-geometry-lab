import numpy as np
import clifford as cf

# Algebra Setup
layout, blades = cf.Cl(3, 0, 1)
g1, g2, g3, g4 = blades['e1'], blades['e2'], blades['e3'], blades['e4']
I = g1 ^ g2 ^ g3 ^ g4

def get_motor(angle_deg, d, axis_vec, pos_vec):
    """
    Erzeugt einen Motor für ein Gelenk nach Gleichung 18.12.
    angle_deg: Drehwinkel des Gelenks
    d: Verschiebung entlang der Achse (für Schubgelenke, sonst 0)
    axis_vec: Richtungsvektor der Gelenkachse (z.B. [0,0,1])
    pos_vec: Position des Gelenks im Raum (Stützvektor)
    """
    theta = np.radians(angle_deg)
    
    # n: Richtungs-Bivektor (Einheit)
    axis_norm = axis_vec / np.linalg.norm(axis_vec)
    n = (axis_norm[0]*(g2^g3) + axis_norm[1]*(g3^g1) + axis_norm[2]*(g1^g2))
    
    # tc: Positions-Vektor als Bivektor-Kombination für das Moment
    tc = pos_vec[0]*g1 + pos_vec[1]*g2 + pos_vec[2]*g3
    
    # m = n ^ tc (Momententeil der Gelenkachse)
    l = n + (I * (n ^ tc))
    
    # Dualer Winkel Terme
    term_cos = np.cos(theta/2) - (I * np.sin(theta/2) * (d/2))
    term_sin = np.sin(theta/2) + (I * np.cos(theta/2) * (d/2))
    
    return term_cos + term_sin * l

def solve_fk(angles):
    """
    Vorwärtskinematik für einen 2-Arm Roboter.
    Arm 1: Länge 2, rotiert um Ursprung.
    Arm 2: Länge 1.5, rotiert am Ende von Arm 1.
    """
    # Gelenk 1: Im Ursprung [0,0,0], Achse Z
    M1 = get_motor(angles[0], 0, [0, 0, 1], [0, 0, 0])
    
    # Gelenk 2: Position ist am Ende von Arm 1 (Länge 2 in X-Richtung)
    # WICHTIG: Die Position wird im lokalen System des vorigen Gelenks definiert
    M2 = get_motor(angles[1], 0, [0, 0, 1], [2, 0, 0])
    
    # Gesamt-Motor (Kinematische Kette)
    M_total = M1 * M2
    
    # Wir transformieren einen Testpunkt (den Greifer/Endeffektor)
    # Der Greifer sitzt am Ende von Arm 2 (1.5 Einheiten weiter in X)
    p_ee_local = 1 + g4 * (3.5 * g1) # 2.0 (Arm1) + 1.5 (Arm2)
    
    p_ee_global = M_total * p_ee_local * ~M_total
    
    return p_ee_global

def extract_coords(point_multivector):
    """Extrahiert x, y, z Koordinaten aus einem transformierten Punkt in G3,0,1"""
    # In G3,0,1 ist ein Punkt p = 1 + g4*(x*g1 + y*g2 + z*g3)
    # Wir isolieren den g4-Teil
    coords = point_multivector(1) # Grad 1 (Vektoren)
    # Da g4*g1 ein Bivektor ist, suchen wir die Koeffizienten von g4g1, g4g2, g4g3
    x = (point_multivector | (g1^g4))[0]
    y = (point_multivector | (g2^g4))[0]
    z = (point_multivector | (g3^g4))[0]
    return np.array([x, y, z])

# --- Testlauf ---
angles_test = [45, 45] # Gelenk 1: 45°, Gelenk 2: 45°
pos_final = solve_fk(angles_test)

print(f"Winkel: {angles_test}")
# Hinweis: Die Extraktion hängt von der Implementierung der Punkt-Einbettung ab
# Hier schauen wir uns einfach die Koeffizienten der 'idealen' Bivektoren an
print(f"Endeffektor Multivektor (Auszug):\n{pos_final}")