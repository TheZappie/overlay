import math

import numpy as np
import shapely
from matplotlib import pyplot as plt
from shapely import affinity
from shapely.plotting import plot_polygon

from overlay import overlay

triangle = shapely.Polygon([(math.cos(math.radians(angle)), math.sin(math.radians(angle))) for angle in [0, 120, 240]])
triangles = [affinity.rotate(triangle, angle, origin=(0,0)) for angle in np.linspace(0, 120, 5, endpoint=False)]

triangles_overlain = overlay(triangles)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
for polygon in triangles:
    plot_polygon(polygon, color="w", add_points=False, ax=ax1)
for polygon in triangles_overlain:
    plot_polygon(polygon, color="w", add_points=False, ax=ax2)
ax1.set(facecolor="#242c34", xticks=[], yticks=[])
ax2.set(facecolor="#242c34", xticks=[], yticks=[])
ax1.set_title("Normal")
ax2.set_title("Overlain")
plt.savefig("Triangles.jpg")
plt.show()
