import numpy as np
import matplotlib.pyplot as plt
import sys

latitud1=(float(sys.argv[1])*np.pi)/180.0
longitud1=(float(sys.argv[2])*np.pi)/180.0

latitud2=(float(sys.argv[3])*np.pi)/180.0
longitud2=(float(sys.argv[4])*np.pi)/180.0



R =6371.0
deltalat =latitud2-latitud1
deltalong = longitud2-longitud1
distancia=2*R*np.arcsin(np.sqrt(((np.sin(deltalat/2.0))**2)+(np.cos(latitud1)*np.cos(latitud2)*(np.sin(deltalong/2.0))**2)))

print distancia
