import numpy as np
import clifford as cf

layout, blades = cf.Cl(3, 0, 1)
g1, g2, g3, g4 = blades['e1'], blades['e2'], blades['e3'], blades['e4']
I = g1 ^ g2 ^ g3 ^ g4

def get_conjugates(M):
    """
    Implementiert die Varianten aus Gleichung (18.28).
    M:  Originaler Motor (Ts * Rs)
    Mt: Reversierung (Reverse) ~M = (a0 - a) + I(b0 - b)
    M_bar: Duale Konjugation (Inversion des I-Teils)
    Mt_bar: Kombinierte Konjugation
    """
    # M_tilde (Reversierung des Grads)
    Mt = ~M
    
    # M_bar (Inversion des dualen Teils I -> -I)
    # In G(3,0,1) ist I = g1234. Wir negieren alle Terme, die g4 enthalten.
    val_bar = M.value.copy()
    for i, name in enumerate(layout.names):
        if 'e4' in name:
            val_bar[i] *= -1
    M_bar = layout.MultiVector(val_bar)
    
    # Mt_bar (~M_bar)
    Mt_bar = ~M_bar
    
    return Mt, M_bar, Mt_bar

def extract_components(M):
    """
    Implementiert Gleichung (18.29) zur Extraktion der 4 Komponenten.
    """
    Mt, M_bar, Mt_bar = get_conjugates(M)
    
    # a0: Realer Skalar
    a0 = 0.25 * (M + Mt + M_bar + Mt_bar)
    
    # Ib0: Dualer Skalar
    Ib0 = 0.25 * (M + Mt - M_bar - Mt_bar)
    
    # a: Realer Bivektor
    a = 0.25 * (M - Mt + M_bar - Mt_bar)
    
    # Ib: Dualer Bivektor
    Ib = 0.25 * (M - Mt - M_bar + Mt_bar)
    
    return a0, Ib0, a, Ib

# --- Demonstration ---
def run_properties_demo():
    print("--- 18.3.3 Eigenschaften von Motoren ---")
    
    # Erstelle einen Test-Motor (Rotation + Translation)
    theta = np.pi/3 # 60 Grad
    d = 0.8
    n = (g1^g2) # Rotationsebene
    l = n + I*(n ^ (1.5*g1)) # Verschobene Achse
    
    M = np.cos(theta/2) + np.sin(theta/2) * l
    
    # 1. Überprüfung der Norm (Gleichung 18.22)
    norm_sq = M * ~M
    print(f"Motor-Norm |M| (sollte 1 sein): {norm_sq.value[0]:.4f}")
    
    # 2. Extraktion der Komponenten (Gleichung 18.29)
    a0, Ib0, a, Ib = extract_components(M)
    
    print("\nExtrahierte Komponenten:")
    print(f"a0 (Real-Skalar):    {a0}")
    print(f"Ib0 (Dual-Skalar):   {Ib0}")
    print(f"a (Real-Bivektor):   {a}")
    print(f"Ib (Dual-Bivektor):  {Ib}")
    
    # 3. Kombination von Motoren (Gleichung 18.25)
    Ma = M
    Mb = M # Wir machen die gleiche Bewegung nochmal
    Mc = Ma * Mb
    print(f"\nVerketteter Motor (Ma*Mb) Skalarteil: {Mc.value[0]:.4f}")

if __name__ == "__main__":
    run_properties_demo()