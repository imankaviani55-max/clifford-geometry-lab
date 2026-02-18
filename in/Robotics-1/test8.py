import numpy as np
import clifford as cf

# Algebra Setup
layout, blades = cf.Cl(3, 0, 1)
g1, g2, g3, g4 = blades['e1'], blades['e2'], blades['e3'], blades['e4']
I = g1 ^ g2 ^ g3 ^ g4

def motor_log(M):
    """
    Berechnet den Logarithmus eines Motors M.
    Verwendet .value[0] für den Skalarteil, um Warnings zu vermeiden.
    """
    # s ist der Skalarteil (Koeffizient von 1)
    s = M.value[0] 
    # b ist der Bivektor-Teil (Grad 2)
    b = M(2)
    
    theta_half = np.arccos(np.clip(s, -1.0, 1.0))
    
    if abs(theta_half) < 1e-6:
        return b 
    
    # L = (theta/2) * l
    L = b * (theta_half / np.sin(theta_half))
    return L

def analyze_motion(M):
    """Analysiert die Schraubenbewegung ohne fehlerhafte layout.v Aufrufe"""
    L = motor_log(M)
    
    print("--- Analyse der Schraubenbewegung (Logarithmus) ---")
    print(f"Bivektor der Bewegung (L):\n{L}")
    
    # Um den Rotationswinkel theta zu extrahieren:
    # Wir projizieren L auf die euklidischen Bivektoren (e12, e23, e31)
    # In G(3,0,1) haben diese Bivektoren ein positives Quadrat.
    # Der Translator-Teil (mit e4) hat das Quadrat 0.
    
    # Wir nutzen die Norm des euklidischen Teils:
    # L_sq ist (theta/2)^2 + duale Terme
    L_sq = (L|L).value[0]
    theta = 2 * np.sqrt(abs(L_sq))
    
    print(f"Extrahierter Gelenkwinkel: {np.degrees(theta):.2f}°")
    
    # Extraktion der Verschiebung d:
    # Das ist etwas komplexer, da d im dualen Teil steckt.
    # Ein einfacher Weg: d = 2 * (L-Teil mit g4)
    # Wir schauen uns die Koeffizienten an, die e4 enthalten
    d_part = sum([abs(L.value[i]) for i in range(len(L.value)) if 'e4' in layout.names[i]])
    if theta > 1e-6:
        print(f"Geschätzte Verschiebung (Pitch d): {d_part:.4f}")

# --- Beispiel ---
axis = [0, 0, 1]
theta_input = np.pi/3 # 60 Grad
# Erzeuge Motor: 60 Grad um Z-Achse
n = (g1^g2)
M = np.cos(theta_input/2) - n * np.sin(theta_input/2)

if __name__ == "__main__":
    analyze_motion(M)