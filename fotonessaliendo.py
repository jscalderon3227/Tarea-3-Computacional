import numpy as np
import matplotlib.pyplot as plt
import sys

n=sys.argv[1]

numero=int(n)

numeropasossalir=np.zeros(numero)

for j in range(numero):

  asim=np.random.random()
  angulo=np.random.random()
  radio=np.random.random()
  

  r=100.0*(radio**(1.0/3.0))
  asym=np.arccos((2.0*asim)-1.0)
  polar=2.0*np.pi*angulo

  x=r*np.sin(asym)*np.cos(polar)
  y=r*np.sin(asym)*np.sin(polar)
  z=r*np.cos(asym)
  
  

  distancia=r

  while distancia<100:

      theta =np.random.random(1)
      phi=np.random.random(1)
      deltax=np.cos(2.0*np.pi*theta)*np.sin(np.pi*phi)
      deltay=np.sin(2.0*np.pi*theta)*np.sin(np.pi*phi)
      deltaz=np.cos(np.pi*phi)
      

      x+=deltax[0]
      y+=deltay[0]
      z+=deltaz[0]

      distancia=np.sqrt((x**2)+(y**2)+(z**2))
      numeropasossalir[j]+=1



plt.hist(numeropasossalir,bins=50)
plt.savefig("n_fotones_uniforme.pdf")


plt.show()
