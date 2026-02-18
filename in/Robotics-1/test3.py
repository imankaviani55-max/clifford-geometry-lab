import numpy as np
import clifford as cf

# Definition der Algebra G(3,0,1)
# 3 Dimensionen quadratisch +1, 1 Dimension quadratisch 0
layout, blades = cf.Cl(3, 0, 1)

# Basisvektoren extrahieren (gamma_k)
g1 = blades['e1']
g2 = blades['e2']
g3 = blades['e3']
g4 = blades['e4'] # Das ist unser gamma_4 mit g4^2 = 0

# Der Einheits-Pseudoskalar (Gleichung 18.4)
I = g1 ^ g2 ^ g3 ^ g4

def analyze_g301():
    print("--- Analyse der 4D Geometrischen Algebra G(3,0,1) ---")
    
    # Überprüfung der Metrik
    print(f"g1^2: {g1*g1} (sollte 1.0 sein)")
    print(f"g2^2: {g2*g2} (sollte 1.0 sein)")
    print(f"g3^2: {g3*g3} (sollte 1.0 sein)")
    print(f"g4^2: {g4*g4} (sollte 0.0 sein)")
    
    # Überprüfung des Pseudoskalars
    print(f"\nPseudoskalar I: {I}")
    print(f"I^2: {I*I} (sollte 0.0 sein)")

def demonstrate_bivectors():
    """
    In G(3,0,1) gibt es 6 Bivektoren.
    3 davon sind 'euklidisch' (Rotationen), 
    3 sind 'ideal' (Translationen).
    """
    # Euklidische Bivektoren (Rotationsebene)
    b_rot = g1 ^ g2
    
    # 'Ideale' Bivektoren (verknüpft mit gamma_4)
    # Diese werden später für Translationen genutzt
    b_trans = g4 ^ g1
    
    print("\n--- Bivektoren in G(3,0,1) ---")
    print(f"Rotations-Bivektor (g1^g2): {b_rot}")
    print(f"Translations-Bivektor (g4^g1): {b_trans}")
    print(f"Quadrat des Translations-Bivektors: {b_trans*b_trans} (immer 0)")

if __name__ == "__main__":
    analyze_g301()
    demonstrate_bivectors()