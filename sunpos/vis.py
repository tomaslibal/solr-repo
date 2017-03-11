import numpy as np
from mayavi import mlab
from tvtk.tools import visual
import numpy as np

fig = mlab.figure(1, bgcolor=(0, 0, 0), size=(350, 350))
visual.set_viewer(fig)
mlab.clf()

# The position of the atoms
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

sun = mlab.points3d(pos_x[1], pos_y[1], pos_z[1],
                   scale_factor=1,
                   resolution=20,
                   color=(1,1,1),
                   scale_mode='none')

plane_surf = np.zeros(25).reshape(5,5)
plane = mlab.surf(plane_surf)


arrow_up = visual.arrow(axis=(0,0,90))
vector_sun = visual.arrow(axis=((pos_x[1]),(pos_y[1]),(pos_z[1])),color=(1,0,0))

r1 = visual.ring(x=0, y=0, z=0, radius=3)
r1.axis=(0,0,90)

# mlab.view()
mlab.show()
