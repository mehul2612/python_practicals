d1={'apple':50,'mango':100,'guava':200,'banana':500}
# print(d1)
print(type(d1))
print(d1.values())
print(d1.keys())
d1['orange']=70
d1['banana']=20
d2={'kivi':120,'grapes':80}
d1.update(d2)
d1.pop('banana')
print(d1)