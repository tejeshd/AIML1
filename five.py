lst1=[1,1,1,1]
lst2=[1,2,3,4]
lst3=[1,1,1,1]
a=list(map(lambda x,y,z: x+y+z , lst1,lst2,lst3))
print(a)
