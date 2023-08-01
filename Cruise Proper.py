import matplotlib.pyplot as plt
import numpy as np
'''m=float(input("Enter the Mass of Car: "))
b=float(input("Enter Drag Coeff: "))
sp=int(input('enter setpoint: '))'''
t=0
'''kp=float(input('Enter P Gain: '))
ki=float(input('Enter I Gain: '))
kd=float(input('Enter D Gain: '))'''
m,b,sp=1000,5,100
kp,ki,kd=0.08,0.05,10
v=0
esum=0
e1=sp
v1=0
varr=[]
for t in range(0,4000):
    varr.append(v)
    #Reference
    e=sp-v
    esum+=e
    d=e-e1
    #Controller
    u=kp*e+ki*esum+kd*d
    e1=e
    #Plant
    v=(u+m*v1)/(m+b)
    v1=v
x=np.arange(0,4000)
y=np.array(varr)
plt.xlabel("Time")
plt.ylabel("Velocity of Car FINAL "+str(v))
plt.plot(x,y,color='red')
plt.show()