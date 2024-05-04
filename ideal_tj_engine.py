import numpy as np
import matplotlib.pyplot as plt
k=1.4
cp=1004.5

Tt2=float(input('inlet entry temperature: '))
OPR=float(input('overall pressure ratio: '))


Tt3=Tt2*np.power(Tt2,(k-1)/k)
TET=2500
cv=cp/k

#The shape of an isochoric line in a T-s diagram is given by the following equation
#    T(s)=T0*exp((s-s0)/cv)
#From here one can find the change in entropy inside the combustion chamber as

s=np.abs(cv*np.log(TET/Tt3))

#Tt5 and Tt2 are connected by the isochoric line that closes the Brighton cycle

Tt5=Tt2*np.exp(s/cv)

s_discretized=np.linspace(0,s,100)

T1=Tt2*np.exp(s_discretized/cv)
T2=Tt3*np.exp(s_discretized/cv)
zer=[0,0]
sd=[s,s]

T_var_1=[Tt2,Tt3]
T_var_2=[Tt5,TET]


plt.plot(s_discretized,T1,s_discretized,T2,zer,T_var_1,sd,T_var_2)
plt.xlabel('s')
plt.ylabel('total temperature')
plt.grid(visible=bool)
plt.show()





