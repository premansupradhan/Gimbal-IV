import matplotlib.pyplot as plt
import math
import numpy as np
sp=float(input("Enter Final Position (in degrees): "))
sp=sp*math.pi/180
ang=np.arange(0,2*math.pi,0.02)
fig=plt.figure()
ax=plt.axes(projection='polar')
kp,ki,kd=10,0.1,10
initial=0
cur=0
e1=sp
carr=[0,]
esum=0
e=0
l=10
for i in range(0,10000):

    #reference
    e=sp-cur
    #print(e)
    esum+=e
    d=e-e1
    #Controller
    u=kp*e+ki*esum+kd*d
    print(u)
    e1=e
    #plant
    cur=initial+u*2/1200
    carr.append(cur)
    initial=cur

for cur in carr:
    ax.plot([0,cur],[0,l],linestyle='-',color='black')
    plt.pause(0.05)
    ax.clear()

plt.show()