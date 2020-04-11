import numpy as np


tabel=np.loadtxt('../data/aux6PointsGLR.txt', delimiter=' ')
np.savetxt('../data/aux6PointsGLR.txt',tabel[:409000])