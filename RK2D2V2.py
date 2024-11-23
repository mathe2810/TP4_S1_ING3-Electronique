import numpy as np
import matplotlib.pyplot as plt
import math

a = float(input("Valeur de coeff de frottement : "))
 
def fx_y(y,z):
    return z   
 
def fx_z(y,z):
    return -math.sin(y)-a*z
 
def rk2(h,y,z):
    return y+0.5*h*(fx_y(y,z)+fx_y(y+h*fx_y(y,z),z+h*fx_z(y,z))),z+0.5*h*(fx_z(y,z)+fx_z(y+h*fx_y(y,z),z+h*fx_z(y,z)))
 
 
h=0.01
y0=float(input('angle initial : '))
z0=float(input('vitesse initiale : '))
 
nb_points=1000
 
t=np.linspace(0,nb_points,nb_points)
y=np.linspace(0,0,nb_points)
z=np.linspace(0,0,nb_points)
 
y[0]=y0
z[0]=z0
 
 
for i in range(1,nb_points):
    y[i],z[i]=rk2(h,y[i-1],z[i-1])
 
plt.plot(t,y)
plt.show()