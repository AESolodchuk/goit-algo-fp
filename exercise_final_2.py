import matplotlib.pyplot as plt
import numpy as np


def draw_branch(x, y, length, angle, depth):
    if depth == 0:
        return

    end_x = x + length * np.cos(np.deg2rad(angle))
    end_y = y + length * np.sin(np.deg2rad(angle))

    plt.plot([x, end_x], [y, end_y], color="black")

    draw_branch(end_x, end_y, length * 0.67, angle - 25, depth - 1)
    draw_branch(end_x, end_y, length * 0.67, angle + 25, depth - 1)


initial_length = 100
initial_angle = 90
start_x, start_y = 0, 0


plt.figure(figsize=(8, 8))
plt.axis("off")

depth = input(f"Вкажіть рівень рекурсії:")
draw_branch(
    start_x,
    start_y,
    initial_length,
    initial_angle,
    depth=8 if depth == "" else int(depth),
)

plt.show()
