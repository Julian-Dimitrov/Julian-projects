import matplotlib.pyplot as plt
import numpy as np
from scipy import constants

height = 180
V_o = 8

time = np.sqrt((height * 2) / constants.g)

x_max = V_o * time

print(time)
print(x_max)

x_vals = np.linspace(0, x_max, 2000)
y_vals = np.array([(-(x / V_o)**2) * constants.g / 2 + height for x in x_vals])

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals)
ax.scatter(0, height)
plt.text(0, height, f"(0, {height:.2f})")
ax.scatter(x_max, 0)
plt.text(x_max, 0, f"({x_max:.2f}, 0)")
plt.title(f"Y = {height}, X_max = {x_max:.2f}, time = {time:.2f}")
plt.grid()
# plt.savefig(f"ball_from_cliff_01")
plt.show()
