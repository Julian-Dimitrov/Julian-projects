import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

alpha_degrees = float(input())
v = float(input())
g = 9.8

alpha = np.radians(alpha_degrees)


def physics():
    global x_vals
    global y_vals

    x = (2 * pow(v, 2) * np.tan(alpha) + np.sqrt((2 * pow(v, 2) * np.tan(alpha))**2 + 4 * g * (pow(np.tan(alpha), 2) + 1))) \
                                                                                / (2 * g * (pow(np.tan(alpha), 2) + 1))
    print(x)

    t = x / (v * np.cos(alpha))
    print(t)

    time = np.linspace(0, t, 1000)

    x_vals = np.array([v * np.cos(alpha) * el for el in time])
    y_vals = np.array([v * np.sin(alpha)*el - (g * pow(el, 2))/2 for el in time])

    print(y_vals[-1])


def wall_target():
    global to_the_wall
    global wall_width
    global height
    global target_left
    global target_right

    hit = True

    height = 10
    wall_width = 2
    to_the_wall = 15

    target_width = 4
    to_the_target = 40

    target_left = to_the_target - target_width / 2
    target_right = to_the_target + target_width / 2

    a = wall_width + to_the_wall
    y_wall_close = -g * pow(a, 2) * (pow(np.tan(alpha), 2) + 1) + 2 * pow(v, 2) * np.tan(alpha) * a

    b = wall_width - to_the_wall
    y_wall_far = -g * pow(b, 2) * (pow(np.tan(alpha), 2) + 1) + 2 * pow(v, 2) * np.tan(alpha) * b

    if y_wall_close > height and y_wall_far > height:
        hit = False
        print("You passed the wall")

    else:
        print("You hit the wall")

    if target_left <= x_vals[-1] <= target_right:
        if hit is False:
            print("You have hit the target!!!")

        else:
            print("If the wall did not stop you you might have won")

    else:
        print("Target missed")


physics()
wall_target()

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals)
ax.plot([target_left, target_right], [0, 0])
ax.add_patch(Rectangle((to_the_wall, 0), wall_width, height))
ax.set_aspect(1)
plt.show()
