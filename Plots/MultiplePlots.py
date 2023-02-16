import numpy as np
from matplotlib import pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)


t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

plt.subplot(211) #211->first digit>there are 2 graphs,2nd digit = no of graphs on a level,3rd digit = graph position on its layer(1st,2nd)
plt.plot(t1,f(t1),'bo',t2,f(t2))

plt.subplot(212)
plt.plot(t1,f(t1),'bo',t2,f(t2))

# plt.subplot(212)
# plt.plot(t2,np.cos(2*np.pi*t2))

# plt.subplot(212)
# plt.plot(t2,np.cos(2*np.pi*t2))

plt.show()