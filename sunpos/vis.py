import numpy as np
from mayavi import mlab
from tvtk.tools import visual
from math import sin, cos, radians, degrees
import numpy as np


fig = mlab.figure(1, bgcolor=(0, 0, 0), size=(350, 350))
visual.set_viewer(fig)
mlab.clf()

# The position of the atoms
azimuth=-3.35501983171
alpha=35.5
r=3
sun_x = r * cos(radians(azimuth))
sun_y = r * sin(radians(azimuth))
# solve angle side angle
beta = 90 - alpha
sun_z = (r/sin(radians(beta))) * sin(radians(alpha))

pos_x = np.array([0, 0])
pos_y = np.array([0, 3.0])
pos_z = np.array([0, 2.0])

"""
planet = mlab.points3d(pos_x[0], pos_y[0], pos_z[0],
                  scale_factor=3,
                  resolution=20,
                  color=(1, 0, 0),
                  scale_mode='none')
"""
yellow = (242./255., 230./255., 65./255.)
sun = mlab.points3d(sun_x, sun_y, sun_z,
                   scale_factor=1,
                   resolution=20,
                   color=yellow,
                   scale_mode='none')

plane_surf = np.zeros(25).reshape(5,5)
plane = mlab.surf(plane_surf)

mlab.title("Lat={0}deg N, Lon={1}deg W, {2}".format(51.5, 0.126236, '11:59'))
# mlab.text3d(1.5, 1.5, 0, "A={0}deg S".format(-3.35501983171))
mlab.text(1.5, 1.5, "A={0}deg S".format(-3.35501983171), z=0, width=0.14)
#mlab.text3d(-1.5,1.5, 0, "h={0}deg".format(35.2031937033))
mlab.text(-1.5,1.5, "h={0}deg".format(35.2031937033), z=0, width=0.14)
#mlab.text3d(0, 20, 0, "Lat={0}deg N, Lon={1}deg W".format(51.5, 0.126236))

# south 
mlab.text(r*cos(radians(0)), r*sin(radians(0)), "S", z=0, width=0.14)
# west
mlab.text(r*cos(radians(90)), r*sin(radians(90)), "W", z=0, width=0.14)
# north
mlab.text(r*cos(radians(180)), r*sin(radians(180)), "N", z=0, width=0.14)
# east
mlab.text(r*cos(radians(270)), r*sin(radians(270)), "E", z=0, width=0.14)

arrow_up = visual.arrow(axis=(0,0,90))
vector_sun = visual.arrow(axis=((sun_x),(sun_y),(sun_z)),color=yellow)

r1 = visual.ring(x=0, y=0, z=0, radius=3)
r1.axis=(0,0,90)

# mlab.view()
mlab.show()
