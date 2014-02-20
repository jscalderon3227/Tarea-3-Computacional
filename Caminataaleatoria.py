import numpy as np
import mathplotlib.pyplot as plt
import sys

n=sys.argv[1]

numero=int(n)

theta = random.random(numero)
deltax=cos(2*pi*theta)
deltay=sin(2*pi*theta)

x=zeros(numero)
y=zeros(numero)
distancia=zeros(numero)

for i in range(1,numero):
    x[i]=x[i-1]+deltax[i-1]
    y[i]=y[i-1]+deltay[i-1]

for i in range(numero):
    distancia[i]=sqrt((x[i]**2)+(y[i]**2))

numeropasos=numeropasos+ones(numero)

plot(numeropasos,distancia)
