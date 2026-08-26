def fun(x):
    for i in range(x):
        yield i
x=fun(30)
print(x)
print(next(x))
print(next(x))
print(next(x))




def fun2():
    yield 10
    yield 20
    yield 30
f=fun2()
print(f)
print(next(f))
print(next(f))
print(next(f))



def infinite():
    x=0
    while True:
        yield x
        x+=1
l=infinite()
k=infinite()
print(next(l))
print(next(l))
print("for loop")
for i in l:
    if i>10:
        break
    print(i)
for i in k:
    if i>5:
        break
    print(i)



def even(l):
    for i in l:
        if(i%2==0):
            yield i
k = even([1,2,3,3,7,8,9,4,5,6])
print(next(k))
print(next(k))
for i in k:
    print(i)