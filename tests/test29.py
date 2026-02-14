import numpy as np

# Funktion, um ein Quaternion aus Achse und Winkel zu erstellen
def quaternion_from_axis_angle(axis, angle_rad):
    axis = axis / np.linalg.norm(axis)  # Einheitsvektor der Achse
    w = np.cos(angle_rad / 2)
    x, y, z = axis * np.sin(angle_rad / 2)
    return np.array([w, x, y, z])

# Funktion, um einen Quaternion zu konjugieren
def quaternion_conjugate(q):
    w, x, y, z = q
    return np.array([w, -x, -y, -z])

# Funktion, um einen Vektor mit einem Quaternion zu drehen
def rotate_vector(v, q):
    q_v = np.concatenate([[0], v])  # Vektor als reiner Quaternion
    q_conj = quaternion_conjugate(q)
    # Quaternion-Multiplikation: q * v * q_conj
    return quaternion_multiply(quaternion_multiply(q, q_v), q_conj)[1:]

# Quaternion-Multiplikation
def quaternion_multiply(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1*w2 - x1*x2 - y1*y2 - z1*z2
    x = w1*x2 + x1*w2 + y1*z2 - z1*y2
    y = w1*y2 - x1*z2 + y1*w2 + z1*x2
    z = w1*z2 + x1*y2 - y1*x2 + z1*w2
    return np.array([w, x, y, z])

# Beispiel
axis = np.array([0, 0, 1])  # Rotation um z-Achse
angle = np.pi / 4           # 45 Grad
q = quaternion_from_axis_angle(axis, angle)

vector = np.array([1, 0, 0])  # Vektor, der rotiert werden soll
rotated_vector = rotate_vector(vector, q)

print("Quaternion:", q)
print("Ursprünglicher Vektor:", vector)
print("Rotierter Vektor:", rotated_vector)
