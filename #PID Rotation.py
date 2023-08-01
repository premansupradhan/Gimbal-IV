#PID Rotation
import matplotlib.pyplot as plt
import math
import numpy as np
sp=float(input("Enter Final Position (in degrees): "))
sp=sp*math.pi/180
ang=np.arange(0,2*math.pi,0.02)
fig=plt.figure()
ax=plt.axes(projection='polar')
kp,ki,kd=0.5,0.1,10

initial=0
cur=0
e1=sp
carr=[0,]
esum=0
e=0
l=10
for i in range(0,100000):
    
    #reference
    e=sp-cur
    esum+=e
    d=e-e1
    #Controller
    u=kp*e+ki*esum+kd*d
    e1=e
    #plant
    cur=initial+u*0.05/100
    carr.append(cur)
    initial=cur
print(carr)   
for cur in carr:
    ax.plot([0,cur],[0,l],linestyle='-',color='black')
    plt.pause(0.05)
    ax.clear()

plt.show()   