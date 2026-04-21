import numpy as np
import matplotlib.pyplot as plt

lam = 0.028
a = 0.13
b = 0.13

k = 2 * np.pi / lam

theta = np.linspace(-90, 90, 1000)
theta_rad = np.radians(theta)

# Уникнення ділення на 0
xE = k * a * np.sin(theta_rad) / 2
xH = k * b * np.sin(theta_rad) / 2

xE[xE == 0] = 1e-6
xH[xH == 0] = 1e-6

FE = np.abs(np.sin(xE) / xE)
FH = np.abs(np.sin(xH) / xH)

FE = FE / np.max(FE)
FH = FH / np.max(FH)

plt.plot(theta, FE, label="E")
plt.plot(theta, FH, label="H")
plt.axhline(0.707, linestyle='--')
plt.legend()
plt.grid()
plt.show()