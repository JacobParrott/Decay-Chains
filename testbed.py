#testbed.py

# generate a plot of a circle
# using the parametric form
# x = r cos(theta), y = r sin(theta)
# where theta goes from 0 to 2 pi
# and r is the radius of the circle

import numpy as np
import matplotlib.pyplot as plt

# define the radius
r = 1.0

# define the angles theta goes from 0 to 2 pi
theta = np.linspace(0, 2*np.pi, 100)

# calculate the x and y coordinates
x = r*np.cos(theta)
y = r*np.sin(theta)

# plot the circle
plt.plot(x, y) 


#q: what is an isomer?



