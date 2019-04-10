import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x=np.arange(0,10,0.01)
plt.plot(x,np.sin(x),label='curve')
plt.legend()
plt.xlabel('x axis')
 
plt.show()
