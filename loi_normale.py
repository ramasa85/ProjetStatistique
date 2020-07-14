#from scipy.integrate import quad

import scipy as sp
import matplotlib.pylab as plt
#import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

x_min = -3.0
x_max = 3.0

mean = 0
std = 1.0

x = np.linspace(x_min, x_max, 10000)
y = scipy.stats.norm.pdf(x,mean,std)

plt.plot(x,y, color='coral')

plt.grid()

plt.xlim(x_min,x_max)
plt.ylim(0,0.4)

plt.title('plot - tracer la fonction de densité', fontsize=10)

plt.xlabel('x')
plt.ylabel('loi normal - Normal - Distribution')

plt.savefig("normal_distribution.png")
plt.show()


