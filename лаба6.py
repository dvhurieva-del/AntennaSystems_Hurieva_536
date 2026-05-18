import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv

# Вхідні дані (варіант 4)
lam = 0.035
D = 1.1
f = 0.45

# Основні параметри
k = 2 * np.pi / lam
R0 = D / 2
p = 2 * f
v = k * R0**2 / (2 * p)

# Масив кутів
theta = np.linspace(-np.pi/2, np.pi/2, 1000)

FH = []
FE = []

for t in theta:
    if abs(t) < 1e-8:
        t = 1e-8

    u = k * R0 * np.sin(t)

    den = (0.74 * jv(1, v) / v + 0.13)

    term1 = (
        0.74 * (v * jv(1, v) * jv(0, u) - u * jv(1, u) * jv(0, v))
        / (v**2 - u**2)
        + 0.26 * jv(1, u) / u
    )

    term2 = (
        0.25 * (
            u * jv(1, u) * jv(2, 1.5*v)
            - 1.5*v * jv(1, 1.5*v) * jv(2, u)
        ) / ((1.5*v)**2 - u**2)
    )

    fh = np.cos(t/2)**2 * (term1 - term2) / den
    fe = np.cos(t/2)**2 * (term1 + term2) / den

    FH.append(abs(fh))
    FE.append(abs(fe))

theta_deg = np.degrees(theta)

# Побудова графіків
plt.figure(figsize=(10, 5))
plt.plot(theta_deg, FH, label='H-plane')
plt.plot(theta_deg, FE, label='E-plane')
plt.axhline(0.707, linestyle='--')
plt.grid(True)
plt.legend()
plt.xlabel('Кут θ, град')
plt.ylabel('Нормована ДС')
plt.title('Діаграми спрямованості дзеркальної антени')
plt.show()