from re import X
import numpy as np
from matplotlib import pyplot as plt

x=np.arange(1,11)
print(x)

# y=2*x
# print(y)

# plt.plot(x,y,color='g',linestyle=":",linewidth="2")
# print(plt.title('Line Plot'))
# print(plt.xlabel('x-label'))
# print(plt.ylabel('y-label'))
# print(plt.show())

y1=2*x
y2=3*x
# plt.plot(x,y1,color='g',linestyle=":",linewidth="2")
# plt.plot(x,y2,color='r',linestyle="-",linewidth="2")
# print(plt.title('Line Plot'))
# print(plt.xlabel('x-label'))
# print(plt.ylabel('y-label'))
# plt.grid(True)
# print(plt.show())

plt.subplot(1,2,1) #first index=rows,second index=column,third number=indicate the graph
plt.plot(x,y1,color='g',linestyle=":",linewidth="2")
print(plt.title('Line Plot'))
print(plt.xlabel('x-label'))
print(plt.ylabel('y-label'))
plt.subplot(1,2,2)
plt.plot(x,y2,color='r',linestyle="-",linewidth="2")
print(plt.title('Line Plot'))
print(plt.xlabel('x-label'))
print(plt.ylabel('y-label'))
plt.grid(True)
print(plt.show())
