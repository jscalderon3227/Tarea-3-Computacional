import numpy as np
import matplotlib.pyplot as plt
import sys

n=sys.argv[1]

numero=int(n)

numeropasossalir=np.zeros(numero)


for j in range(numero):

  x=0
  y=0
  distancia=0
  while distancia<100:

      theta =np.random.random(1)
      deltax=np.cos(2*np.pi*theta)
      deltay=np.sin(2*np.pi*theta)
      

      x=x+deltax[0]
      y=y+deltay[0]
      distancia=np.sqrt((x**2)+(y**2))
      numeropasossalir[j]+=1



plt.hist(numeropasossalir,bins=20)
plt.show()
