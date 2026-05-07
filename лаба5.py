import numpy as np
import matplotlib.pyplot as plt

# Вхідні дані
lam = 0.035       # довжина хвилі, м
N = 14             # кількість щілин
d = 0.02           # відстань між щілинами, м

# Хвильове число
k = 2 * np.pi / lam
kd = k * d

# Кути
theta_deg = np.linspace(-90, 90, 5000)
theta = np.radians(theta_deg)

# Уникнення ділення на нуль
psi = kd * np.sin(theta)
small = 1e-12

numerator = np.sin(N * psi / 2)
denominator = N * np.sin(psi / 2) + small

F = np.abs(numerator / denominator)
F = F / np.max(F)

# Пошук ширини головної пелюстки
half_power = 0.707
indices = np.where(F >= half_power)[0]
beamwidth = theta_deg[indices[-1]] - theta_deg[indices[0]]

# Пошук нулів
zero_indices = np.where(F < 0.001)[0]
zero_angles = theta_deg[zero_indices]

# Пошук бокових пелюсток
from scipy.signal import find_peaks

peaks, _ = find_peaks(F)
peak_values = F[peaks]
peak_angles = theta_deg[peaks]

# Видалення головної пелюстки
side_lobes = peak_values[peak_values < 0.99]
max_side_lobe = np.max(side_lobes)

print(f"Хвильове число k = {k:.2f} рад/м")
print(f"kd = {kd:.2f}")
print(f"Ширина головної пелюстки = {beamwidth:.2f} градусів")
print(f"Максимальний рівень бокової пелюстки = {max_side_lobe:.3f}")

# Графік у декартовій системі
plt.figure(figsize=(10, 6))
plt.plot(theta_deg, F)
plt.axhline(0.707, color='red', linestyle='--', label='Рівень 0.707')
plt.xlabel('Кут θ (градуси)')
plt.ylabel('Нормована ДС')
plt.title('Діаграма спрямованості ХвЩА')
plt.grid(True)
plt.legend()

# Полярний графік
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.plot(theta, F)
ax.set_title('Полярна діаграма спрямованості')

plt.show()