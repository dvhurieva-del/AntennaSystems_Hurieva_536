import numpy as np
import matplotlib.pyplot as plt

# Вхідні дані
f = 460e6
c = 3e8
N = 9

# Розрахунки
lam = c / f
k = 2 * np.pi / lam
d = 0.3 * lam

theta = np.linspace(-90, 90, 1000)
theta_rad = np.radians(theta)

psi = k * d * np.cos(theta_rad)

# Уникнення ділення на 0
psi[psi == 0] = 1e-6

F = np.abs(np.sin(N * psi / 2) / (N * np.sin(psi / 2)))

# Нормування
F = F / np.max(F)

# Побудова
plt.plot(theta, F)
plt.axhline(0.707, linestyle='--')
plt.title("Нормована ДС (варіант 4)")
plt.xlabel("θ (градуси)")
plt.ylabel("F(θ)")
plt.grid()
plt.show()