import numpy as np
import clifford as cf

layout, blades = cf.Cl(3, 0, 1)
g1, g2, g3, g4 = blades['e1'], blades['e2'], blades['e3'], blades['e4']

def solve_ik_2d(target_pos, l1, l2):
    """
    Berechnet die Gelenkwinkel für eine Zielposition (x, y).
    l1: Länge Arm 1, l2: Länge Arm 2
    """
    x, y = target_pos[0], target_pos[1]
    d_sq = x**2 + y**2
    d = np.sqrt(d_sq)
    
    # Überprüfung, ob das Ziel erreichbar ist
    if d > (l1 + l2) or d < abs(l1 - l2):
        raise ValueError("Ziel außerhalb des Arbeitsraums")

    # In der GA nutzen wir das Gesetz der Kosinusse, 
    # oft ausgedrückt durch das Skalarprodukt von Vektoren (Blades)
    # cos(theta2)
    cos_theta2 = (d_sq - l1**2 - l2**2) / (2 * l1 * l2)
    theta2 = np.arccos(np.clip(cos_theta2, -1.0, 1.0))
    
    # Winkel für Gelenk 1
    alpha = np.arctan2(y, x)
    beta = np.arccos((l1**2 + d_sq - l2**2) / (2 * l1 * d))
    theta1 = alpha - beta # 'Elbow down' Lösung
    
    return np.degrees(theta1), np.degrees(theta2)

# --- Test der IK ---
target = [1.5, 1.5]
l1, l2 = 2.0, 1.5

try:
    deg1, deg2 = solve_ik_2d(target, l1, l2)
    print(f"Ziel: {target}")
    print(f"Berechnete Winkel -> Gelenk 1: {deg1:.2f}°, Gelenk 2: {deg2:.2f}°")
    
    # Verifizierung mit Vorwärtskinematik (FK)
    # Wenn wir diese Winkel in die FK einsetzen, müssen wir beim Ziel ankommen.
except ValueError as e:
    print(e)