# pandas stands for Panel Data used for manipulation of data  and data analysis
from numpy import half
import pandas as pd
# Single-dimensional data=Series Object
# Multi-dimensional data=Data Frame
s1=pd.Series([1,2,3,4])
print(s1)
print(type(s1))
s2=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s2)
s3=pd.Series({'a':10,'b':20,'c':30})
print(s3)
s4=pd.Series({'a':10,'b':20,'c':30},index=['b','c','d','a'])
print(s4)
s5=pd.Series([1,2,3,4,5,6,7,8,9])
print(s5[4])
print(s5[:4])
print(s5[-3:])
print(s5+5)
print(s4+s3)
print(s1/10)
s6=pd.DataFrame({'Name':['Bob','Sam','Anne'],'Marks':[76,25,92]})
print(s6)
print(s6.head())
print(s6.tail())
print(s6.describe())
# file=('C:\Users\mehul chauhan\OneDrive\Desktop\GreatLearning\Conditional formatitng.xlsx')
iris=pd.read_excel('C:\\Users\\mehul chauhan\\OneDrive\\Desktop\\GreatLearning\\Conditional formatitng.xlsx')
print(iris)
print(iris.head())
print(iris.tail())
print(iris.describe())
print(iris.shape)
print(iris.iloc[0:3,0:2])
print(iris.loc[0:3,('Salesperson','Jan')])
print(iris.drop('Jan',axis=1))
print(iris.drop([1,2,3],axis=0))
print(iris.mean())
print(iris.median())
print(iris.min())
print(iris.max())
def half(x):
    return x*0.5

print(iris[['Jan']].apply(half))
print(iris[['Jan']].value_counts())
print(iris.sort_values(by='Feb'))