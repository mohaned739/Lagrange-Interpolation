import numpy as np
import matplotlib.pyplot as plt


def Lagrange(time,vel,t):

    vt=0
    size= len(time)
    index=0
    for i in range(size):
        #find the correct position
        ti=time[i]
        if t<ti:
            tj=time[i-1]
            if t>tj:
                #tnode = time[i-1] and t1 = time[i]
                L0 = (t-time[i])/(time[i-1] - time[i])
                L1 = (t - time[i-1]) / (time[i]-time[i-1])
                vt =(vel[i-1]* L0)+(vel[i]*L1)
                index=i
                break

    arr = np.array([index,t,vt])
    return arr


time = np.array([0, 10, 15, 20, 22.5, 30])
vel = np.array([0, 227.04, 362.78, 517.35, 602.97, 901.67])
while True:
    t= input("Enter the value you want to interpolate : ");
    t=int(t)
    arr= Lagrange(time,vel,t)
    index=int(arr[0])
    time=np.insert(time,index,t)
    vel=np.insert(vel,index,arr[2])
    print(time)
    print(vel)
    plt.plot(time,vel,"b")
    plt.show()
    cont=input("Do you want to enter another value? y/n : ")
    if cont == "n":
        break