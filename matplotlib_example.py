
import matplotlib.pyplot as plt
import numpy as np


# Graphing 1st function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def func(x, f):  # the equation of the line to find the y values
    return (1 / (4 * f)) * x ** 2


x = np.linspace(-2, 2)
plt.figure()
plt.plot(x, func(x, 2), linewidth=2.0, color='r', label='F = 2')
plt.plot(x, func(x, 6), linewidth=6.0, color='b', label='F = 6')
plt.axis([-2, 2, 0, .5])
plt.title('Parabola plots with varying focal length')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='lower left')
plt.show()


# Graphing 2nd function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def func2(x):
    return 2*x**3 + 3*x**2 - 11*x - 6


x2 = x = np.linspace(-4, 4, num=25)
plt.figure()
plt.plot(x2, func2(x2), '*', linewidth=2.0, color='y')
plt.title('Plot of cubic polynomial ')
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()

# Graphing 3rd function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

plt.figure()
plt.subplot(211)
x3 = np.linspace(-2*np.pi, 2*np.pi)
plt.plot(x3, np.cos(x3), linewidth=2.0, color='r', label='y = cos(x)')
plt.legend(loc='lower right')
plt.grid(True)
plt.title('Plot of cos(x) and sin(x)')

x4 = np.linspace(-2*np.pi, 2*np.pi)
plt.subplot(212)
plt.plot(x4, np.sin(x4), linewidth=2.0, color='gray', label='y = sin(x)')
plt.xlabel("x")
plt.ylabel("y = sine(x")
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
