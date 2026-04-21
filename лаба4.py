import numpy as np
import matplotlib.pyplot as plt

lam = 0.035
l = 0.237
h = 0.12

k = 2 * np.pi / lam

theta = np.linspace(-90, 90, 2000)
theta_rad = np.radians(theta)

# Однострижнева
x1 = k * l * np.cos(theta_rad) / 2
x1[x1 == 0] = 1e-6
F1 = np.abs(np.sin(x1) / x1)

# Двохстрижнева
F2 = F1 * np.abs(np.cos(k * h * np.sin(theta_rad) / 2))

# Нормування
F1 = F1 / np.max(F1)
F2 = F2 / np.max(F2)

plt.plot(theta, F1, label="1 стрижень")
plt.plot(theta, F2, label="2 стрижні")
plt.axhline(0.707, linestyle='--')

plt.xlabel("θ (градуси)")
plt.ylabel("F(θ)")
plt.title("ДСА (варіант 4)")
plt.legend()
plt.grid()
plt.show()