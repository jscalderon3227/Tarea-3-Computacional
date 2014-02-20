import numpy as np
import matplotlib.pyplot as plt
import sys

n=sys.argv[1]

numero=int(n)

theta =np.random.random(numero)
deltax=np.cos(2*np.pi*theta)
deltay=np.sin(2*np.pi*theta)

x=np.zeros(numero)
y=np.zeros(numero)
distancia=np.zeros(numero)

for i in range(1,numero):
    x[i]=x[i-1]+deltax[i-1]
    y[i]=y[i-1]+deltay[i-1]

for i in range(numero):
    distancia[i]=np.sqrt((x[i]**2)+(y[i]**2))

numeropasos=numeropasos+np.ones(numero)

plt.pyplot.show(numeropasos,distancia)
