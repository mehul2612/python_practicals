def hello():
    print("hello world")

hello()

def add_10(x):
    return x+10

print(add_10(9))

def odd_even(a):
    if(a%2==0):
        print("Number is even")
    else:
        print("Number is odd")

print(odd_even(5))
print(odd_even(10))

c1=lambda c:c*c*c
print(c1(7))

# Lambda with filter
l1=[1,2,3,4,56,7,8,9,10,45]
l2=list(filter(lambda d:int(d%2==0),l1))
print(l2)

# Lambda with map
list1=[1,2,3,4,5,6,7,8]
list2=list(map(lambda w:w*2,list1))
print(list2)

# Lambda with reduce
from functools import reduce
sum=reduce(lambda x1,y1:x1+y1,list1)
print(sum)
