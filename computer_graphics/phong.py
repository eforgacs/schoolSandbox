import numpy as np

# i = i_a k_a + i_I (k_diff( N dot L ) + k_spec( R dot V )^n)))
# i = intensity
# k_a = ambient coefficient
# k_diff = diffuse coefficient
# k_spec = specular coefficient
# N = normal vector
# L = light vector
# V = view vector
# R = reflection vector
# n = shininess
# i_a = ambient light intensity
# i_I = light intensity


k_a = 0.7
k_diff = 0.9
k_spec = 0.6
n = 10

i_a = 0.1
i_I = 0.5


P1 = np.array([1, 1, 1])
P2 = np.array([0, 2, 1])
P3 = np.array([0, 0, 1])
N = np.cross(P2 - P1, P3 - P1)

L = [1, 1, 5]
V = [0, 0, 1]
# R = 2N(NL)-L
R = 2 * np.dot(N, L) * N - L
# R = [0, 0, 1]

i = i_a * k_a + i_I * (k_diff * (np.dot(N, L)) + k_spec * (np.dot(R, V)) ** n)

print(f"i: {i}")

# i = i_a * k_a + i_I * (k_diff * (N dot L) + k_spec * (R dot V)^n)

# i = 0.1 * 0.7 + 0.5 * (0.9 * (N dot L) + 0.6 * (R dot V)^10)

# i = 0.1 * 0.7 + 0.5 * (0.9 * (1) + 0.6 * (1)^10)

# i = 0.1 * 0.7 + 0.5 * (0.9 * 1 + 0.6 * 1)

# i = 0.1 * 0.7 + 0.5 * (0.9 + 0.6)

# i = 0.1 * 0.7 + 0.5 * 1.5

# i = 0.1 * 0.7 + 0.75

# i = 0.075 + 0.75

# i = 0.825



# i = i_a * k_a + i_I * (k_diff * (N dot L) + k_spec * (R dot V)^n)
#
# i = 0.1 * 0.7 + 0.5 * (0.9 * (N dot L) + 0.6 * (R dot V)^10)
#
# i = 0.1 * 0.7 + 0.5 * (0.9 * 10 + 0.6 * 35^10)
#
# i = 0.1 * 0.7 + 0.5 * (0.9 * 10 + 0.6 * 35^10)
#
# i = 458533360.87




# i = 0.1 * 0.1 + 0.5 * (0.5 * 0 + 0.5 * 0^10)

# i = 0.1 * 0.1 + 0.5 * (0.5 * 0 + 0.5 * 0)

# i = 0.1 * 0.1 + 0.5 * 0

# i = 0.1 * 0.1 + 0

# i = 0.01



# Is = ks * Is * (N*H)n

# Is = 0.5 * 0.5 * (N*H)^10

# Is = 0.5 * 0.5 * (0.5)^10

# Is = 0.5 * 0.5 * 0.0009765625
