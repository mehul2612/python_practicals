# numpy=Numerical  Python ,used for performing numericals operations
import numpy as np
n1=np.array([10,20,30,40])
print(n1)
n2=np.array([[10,20,30],[40,30,20]])
print(n2)
print(type(n2))
n3=np.zeros((1,2))
print(n3)
n4=np.zeros((5,5))
print(n4)
n5=np.full((2,2),10)
print(n5)
n6=np.arange(10,50,5)
print(n6)
n7=np.random.randint(1,100,5)
print(n7)
n8=np.array([[1,2,3],[4,5,6]])
print(n8.shape)
n8.shape=(3,2)
print(n8)
n9=np.array([1,2,3])
n10=np.array([3,2,1])
# Vertcal merging of 2 arrays
print(np.vstack((n9,n10)))
#Horizantal merging of 2 arrays
print(np.hstack((n9,n10)))
#Column merging of 2 arrays
print(np.column_stack((n9,n10)))
print(np.intersect1d(n1,n2))
print(np.setdiff1d(n1,n2))
print(np.setdiff1d(n2,n1))
print(np.sum([n9,n10]))
print(np.sum([n9,n10],axis=0))
print(np.sum([n9,n10],axis=1))
n9=n9-1
print(n9)
n10=n10+1
print(n10)
n9=n9*2
print(n9)
n10=n10/2
print(n10)
print(np.mean(n2))
print(np.median(n2))
print(np.std(n2))
print(np.save('my_numpy',n1))
new1=np.load('my_numpy.npy')
print(new1)






