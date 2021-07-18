#n-linear equation solver
import numpy as np
from numpy import linalg
print("the number of equations MUST be equal to the number of variables")
i=0
j=0
n=int(input("number of equations="))

x=np.zeros((n,n,n))
y=np.zeros((n,1))
delta=[]

#---------------------data entry--------------------

while i != n:
    j=0
    while j != n:
        x[0,i,j]=float(input(print("a",i+1,j+1,"=")))
        j+=1
    i+=1

i=0
j=0
k=0

while i != n:
    j=0
    while j!=n:
        k=0
        while k !=n:
            x[k,i,j]=x[0,i,j]
            k+=1
        j+=1
    i+=1


i=0
while i !=n:
    y[i,0]=float(input(print("b",i+1,"=")))
    i+=1

#-------------------------------------------------------------------------------
#-------------modefying arrays & calculating determinants-----------------------
#-------------------------------------------------------------------------------

delta.append(round(linalg.det(x[1]),4))

k=0
while k !=n:
    x[k,:,k]=y[:,0]
    delta.append(round(linalg.det(x[k]),4))
    k+=1

    
#-------------calculating results---------------

i=0
while i+1 != len(delta):
    print("x",i+1,"=",round(delta[i+1]/delta[0],4))
    i+=1



    

    
    









