import numpy as np

# ----------------------------
# Hilfsfunktionen für Quaternions
# ----------------------------

def quaternion_from_axis_angle(axis, angle_rad):
    axis = axis / np.linalg.norm(axis)
    w = np.cos(angle_rad / 2)
    x, y, z = axis * np.sin(angle_rad / 2)
    return np.array([w, x, y, z])

def quaternion_conjugate(q):
    w, x, y, z = q
    return np.array([w, -x, -y, -z])

def quaternion_multiply(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1*w2 - x1*x2 - y1*y2 - z1*z2
    x = w1*x2 + x1*w2 + y1*z2 - z1*y2
    y = w1*y2 - x1*z2 + y1*w2 + z1*x2
    z = w1*z2 + x1*y2 - y1*x2 + z1*w2
    return np.array([w, x, y, z])

# ----------------------------
# Dual Quaternion Klasse
# ----------------------------

class DualQuaternion:
    def __init__(self, real, dual):
        self.real = real   # Quaternion für Rotation
        self.dual = dual   # Quaternion für Translation

    @staticmethod
    def from_translation_rotation(translation, axis, angle_rad):
        r = quaternion_from_axis_angle(axis, angle_rad)  # Rotations-Quaternion
        t = np.array([0, *translation])
        d = 0.5 * quaternion_multiply(t, r)             # Dualteil
        return DualQuaternion(r, d)

    def conjugate(self):
        return DualQuaternion(
            quaternion_conjugate(self.real),
            quaternion_conjugate(self.dual)
        )

    # Dual Quaternion Multiplikation
    def multiply(self, other):
        r_new = quaternion_multiply(self.real, other.real)
        d_new = quaternion_multiply(self.real, other.dual) + quaternion_multiply(self.dual, other.real)
        return DualQuaternion(r_new, d_new)

    # Vektor mit Dual Quaternion transformieren
    def transform_vector(self, v):
        v_q = np.array([0, *v])
        dq_v = quaternion_multiply(quaternion_multiply(self.real, v_q), quaternion_conjugate(self.real))
        translation = 2 * quaternion_multiply(self.dual, quaternion_conjugate(self.real))[1:]
        return dq_v[1:] + translation

# ----------------------------
# Beispiel
# ----------------------------

# Translation + Rotation
translation = np.array([1, 2, 3])
axis = np.array([0, 0, 1])
angle = np.pi / 4  # 45 Grad

dq = DualQuaternion.from_translation_rotation(translation, axis, angle)

vector = np.array([1, 0, 0])
transformed_vector = dq.transform_vector(vector)

print("Ursprünglicher Vektor:", vector)
print("Transformierter Vektor:", transformed_vector)
