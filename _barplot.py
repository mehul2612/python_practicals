from matplotlib import pyplot as plt
# student={'Bob':87,'Matt':56,'Sam':27}
# names=list(student.keys())
# values=list(student.values())
# print(plt.bar(names,values))
# print(plt.title('Distribution of student marks'))
# print(plt.xlabel('Name of student'))
# print(plt.ylabel('Marks of students'))
# print(plt.show())

student={'Bob':87,'Matt':56,'Sam':27,'Anne':76}
names=list(student.keys())
values=list(student.values())
print(plt.barh(names,values,color='g'))
print(plt.title('Distribution of student marks'))
print(plt.xlabel('Name of student'))
print(plt.ylabel('Marks of students'))
plt.grid(True)
print(plt.show())
