from matplotlib import pyplot as plt
import pandas as pd
# data=[2,7,7,5,5,6,7,7,8,3,5,6,9,7,6,5,6]
# plt.hist(data,color='r',)
# print(plt.show())

iris=pd.read_excel('C:\\Users\\mehul chauhan\\OneDrive\\Desktop\\GreatLearning\\Conditional formatitng.xlsx')
print(iris.head())
plt.subplot(1,6,1)
plt.hist(iris['Jan'],bins=30,color="red")
plt.subplot(1,6,2)
plt.hist(iris['Feb'],bins=30,color="yellow")
plt.subplot(1,6,3)
plt.hist(iris['Mar'],bins=30,color="green")
plt.subplot(1,6,4)
plt.hist(iris['Apr'],bins=30,color="blue")
plt.subplot(1,6,5)
plt.hist(iris['May'],bins=30,color="black")
plt.subplot(1,6,6)
plt.hist(iris['Jun'],bins=30,color="brown")
print(plt.show())
