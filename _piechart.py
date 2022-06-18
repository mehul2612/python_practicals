from matplotlib import pyplot as plt
fruit=['Applle','Orange','Mango','Guava']
quantity=[67,64,100,29]
# plt.pie(quantity,labels=fruit,autopct='%0.1f%%')

plt.pie(quantity,labels=fruit,radius=2)
plt.pie([1],colors=['w'],radius=1)


print(plt.show())