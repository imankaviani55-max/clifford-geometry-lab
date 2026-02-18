import numpy as np
from clifford.g3 import layout

# Sicherer Zugriff auf die Basisvektoren e1, e2, e3
blades = layout.blades
e1, e2, e3 = blades['e1'], blades['e2'], blades['e3']
I = e1 ^ e2 ^ e3 # Pseudoskalar (G3,0,0)

def create_point(coords):
    """Gleichung 18.30: Punkt als Vektor"""
    return coords[0]*e1 + coords[1]*e2 + coords[2]*e3

def create_line(pos_coords, dir_coords):
    """Gleichung 18.31: Linie als Vektor (n) + Bivektor (m)"""
    x = create_point(pos_coords)
    n = create_point(dir_coords)
    # Normierung des Richtungsvektors
    n_norm = n / np.sqrt(abs((n|n).value[0]))
    # m = x ^ n (Momenten-Bivektor)
    m = x ^ n_norm
    return n_norm + m

def create_plane(pos_coords, normal_coords):
    """Gleichung 18.32: Ebene als Bivektor (n) + Trivektor (Id)"""
    x = create_point(pos_coords)
    n_vec = create_point(normal_coords)
    # Normalenvektor normieren
    n_vec = n_vec / np.sqrt(abs((n_vec|n_vec).value[0]))
    
    # Der Bivektor n ist das Dual des Normalenvektors
    n_bivec = n_vec * I
    # Trivektor-Teil entspricht der Hesse-Distanz (x ^ n)
    dist_trivector = x ^ n_bivec
    return n_bivec + dist_trivector

def run_geometry_test():
    print("--- 18.4.1 Geometrische Objekte (stabilisiert) ---")
    
    # 1. Punkt bei (1, 2, 3)
    p = create_point([1, 2, 3])
    print(f"Punkt p:\n{p}")
    
    # 2. Linie: Geht durch (1,0,0) in Richtung Z (e3)
    # n = e3, x = e1 -> m = e1 ^ e3 = -e31
    line = create_line([1, 0, 0], [0, 0, 1])
    print(f"\nLinie l (Richtung n + Moment m):\n{line}")
    
    # 3. Ebene: Normalenvektor e2 (Y-Achse), Distanz 5 (geht durch [0,5,0])
    # Entspricht der XZ-Ebene bei y=5
    plane = create_plane([0, 5, 0], [0, 1, 0])
    print(f"\nEbene h (Bivektor n + Trivektor Id):\n{plane}")
    
    # Hesse-Distanz extrahieren
    # Da h = n + I*d, gilt d = h(3) / I
    d = (plane(3) / I).value[0]
    print(f"Extrahierte Hesse-Distanz d: {d:.2f}")

if __name__ == "__main__":
    run_geometry_test()