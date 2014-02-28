import numpy as np
import matplotlib.pyplot as plt 
import cmath 
import sys
from pylab import *

iteraciones=int(sys.argv[1])

x=linspace(-2.0,2.0,1024)
y=linspace(-2.0,2.0,1024)

conjuntomandelbrot=zeros((1024,1024))
xcomplejo=np.zeros(iteraciones)
ycomplejo=np.zeros(iteraciones)

for m in range(1024):

   
     for n in range(1024):
            
         for l in range(iteraciones):
               
                
                if(l==0):
                    
                    xcomplejo[l]=0
                    ycomplejo[l]=0
                    normacuad=(xcomplejo[l]**2)+(ycomplejo[l]**2)
                    
                    if(normacuad<4):
                      conjuntomandelbrot[m][n]=l
                else:
                    
                   xcomplejo[l]=(xcomplejo[l-1]**2)-(ycomplejo[l-1]**2)+x[m]
                   ycomplejo[l]=(2.0*xcomplejo[l-1]*ycomplejo[l-1])+y[n]
                    
                   normacuad=(xcomplejo[l]**2)+(ycomplejo[l]**2)    
                    
                   if(normacuad<4):
                      conjuntomandelbrot[m][n]=l
                    
plt.imshow(conjuntomandelbrot)
plt.show()
