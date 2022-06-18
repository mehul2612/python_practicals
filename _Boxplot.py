from matplotlib import pyplot as plt
# it  gives us 25%,50%,75%,max,min of the data
one=[1,2,3,4,5,6,7,8,9]
two=[1,2,3,4,5,4,3,2,1]
three=[6,7,8,9,8,7,6,5,4]
data=list([one,two,three])
plt.boxplot(data)
print(plt.show())