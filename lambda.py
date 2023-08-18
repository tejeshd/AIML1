a= lambda x:x+5
print(a(5))

b=lambda a,c: a+c
print(b(2,3))

x=lambda p,q: p if(p>q) else q
print(x(5,7))

y=lambda a:a**2
print(y(3))

lst=[1,2,3,4,5]
a=list(map(lambda x:x*x,lst))
print(a)

fib=[1,2,3,4,5,8,12,13,19]
f=list(filter(lambda x:x%2==0,fib))
print(f)

from functools import reduce
lst=[1,2,3,4,5,6,7]
x=reduce(lambda x,y:x+y,lst)
print(x)
