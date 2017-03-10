import numpy as np
from mayavi import mlab
from tvtk.tools import visual


fig = mlab.figure(1, bgcolor=(0, 0, 0), size=(350, 350))
visual.set_viewer(fig)
mlab.clf()

# The position of the atoms
pos_x = np.array([1, 0])
pos_y = np.array([1.5, 3.0])
pos_z = np.array([-1.5, 2.0])

planet = mlab.points3d(pos_x[0], pos_y[0], pos_z[0],
                  scale_factor=3,
                  resolution=20,
                  color=(1, 0, 0),
                  scale_mode='none')

sun = mlab.points3d(pos_x[1], pos_y[1], pos_z[1],
                   scale_factor=1,
                   resolution=20,
                   color=(1,1,1),
                   scale_mode='none')

a1 = visual.arrow()
r1 = visual.ring(x=0, y=0, z=0, radius=3)

# mlab.view()
mlab.show()
