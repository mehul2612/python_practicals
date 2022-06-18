from matplotlib import pyplot as plt
x=[10,20,30,40,50,60,70,80,90]
y=[8,1,7,2,0,3,7,3,2]
z=[7,2,5,6,9,1,4,5,3]
# plt.scatter(x,y,marker='*',c='g',s=100)
# plt.scatter(x,z,marker='.',c='r',s=100)
# print(plt.show())

plt.subplot(1,2,1)
plt.scatter(x,y,marker='*',c='g',s=100)
plt.subplot(1,2,2)
plt.scatter(x,z,marker='.',c='r',s=100)
print(plt.show())