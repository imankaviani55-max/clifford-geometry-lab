import clifford.g3 as g3
from clifford.g3 import blades
import matplotlib.pyplot as plt
import numpy as np

# =========================
# Basisvektoren
# =========================
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']
I  = e1 ^ e2 ^ e3

# =========================
# Ebenen (OPNS)
# =========================
uA = e2
vA = e1 + e3
A  = uA ^ vA

uB = e1
vB = e2 + e3/2
B  = uB ^ vB

# =========================
# Meet (Schnittgerade)
# =========================
# Meet of two planes is the intersection line.
# Calculated via duals: (Dual(A) ^ Dual(B)).undual()
mAB = ((A / I) ^ (B / I)) * I

# =========================
# GA → numpy
# =========================
def mv_to_xyz(v):
    return np.array([float(v | e1), float(v | e2), float(v | e3)])

# =========================
# Numerische Ebenennormale
# =========================
def plane_normal(u, v):
    u = mv_to_xyz(u)
    v = mv_to_xyz(v)
    n = np.cross(u, v)
    return n / np.linalg.norm(n)

nA = plane_normal(uA, vA)
nB = plane_normal(uB, vB)

# =========================
# Ebene plotten
# =========================
def plot_ebene(ax, n, size=1.5, alpha=0.25, farbe='cyan'):
    if abs(n[0]) < 0.9:
        v1 = np.array([1, 0, 0])
    else:
        v1 = np.array([0, 1, 0])

    v1 = v1 - np.dot(v1, n) * n
    v1 /= np.linalg.norm(v1)
    v2 = np.cross(n, v1)

    s = np.linspace(-size, size, 12)
    t = np.linspace(-size, size, 12)
    S, T = np.meshgrid(s, t)

    X = S*v1[0] + T*v2[0]
    Y = S*v1[1] + T*v2[1]
    Z = S*v1[2] + T*v2[2]

    ax.plot_surface(X, Y, Z, color=farbe, alpha=alpha)

# =========================
# Schnittgerade
# =========================
d = mv_to_xyz(mAB)
d = d / np.linalg.norm(d)
t = np.linspace(-2, 2, 200)

# =========================
# Plot
# =========================
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

plot_ebene(ax, nA, farbe='blue')
plot_ebene(ax, nB, farbe='green')

ax.plot(t*d[0], t*d[1], t*d[2],
        color='red', linewidth=3, label='A ∩ B')

ax.set_xlim([-2,2])
ax.set_ylim([-2,2])
ax.set_zlim([-2,2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Meet zweier Ebenen (Geometric Algebra)')
ax.legend()

plt.show()
