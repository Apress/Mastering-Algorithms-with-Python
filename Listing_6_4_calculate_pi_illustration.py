import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1234)

num_trials = 500
x = np.random.uniform(low=-1.0, high=1.0, size=num_trials)
y = np.random.uniform(low=-1.0, high=1.0, size=num_trials)

radius = 1.0
theta = np.linspace(0, 2 * np.pi, 1000)
x_circle = radius * np.cos(theta)
y_circle = radius * np.sin(theta)

inside_circle = x ** 2 + y ** 2 <= 1
x_inside, x_outside = x[inside_circle], x[~inside_circle]
y_inside, y_outside = y[inside_circle], y[~inside_circle]
plt.scatter(x_inside, y_inside, s=20, c='b', alpha=0.5)
plt.scatter(x_outside, y_outside, s=20, c='r', alpha=0.5)
plt.plot(x_circle, y_circle, 'k')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.gca().set_aspect('equal')
plt.tight_layout()
plt.show()



