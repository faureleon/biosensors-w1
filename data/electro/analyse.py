from math import *
import numpy as np
import matplotlib.pyplot as plt

fichierlow = open("datalow.txt", 'r')
Import=fichierlow.readlines()
Listlow=Import[:31]


inte=[]
val=[]


for i in range (len(List)):
    Listlow[i]=Listlow[i].strip()
    inte.append(Listlow[i][:2])
    val.append(Listlow[i][3:])


plt.plot(inte,val)
plt.show()
