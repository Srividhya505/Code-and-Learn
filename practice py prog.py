#prime number
# n=int(input())
# if(n<2):
#     print("not Prime Number")
# else:
#     for i in range(2,n):
#         if(n%i==0):
#             print("not prime")
#             break
#         else:
#             print("prime")


#factors of no
# n=int(input())
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i,end=" ")


#factorial of a number
# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     print(fact)


#factor count
# n=int(input())
# fc=0
# for i in range(1,n+1):
#     if(n%i==0):
#         fc=fc+1
#         print(fc)


#prime no using fc
# n=int(input())
# fc=0
# for i in range(1,n+1):
#     if(n%i==0):
#         fc=fc+1
# if(fc==2):
#     print("prime")


#fibonacci
# n=int(input())
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c


#Lcm of 2 no
# a=int(input())
# b=int(input())
# if a>b:
#     max=a
# else:
#     max=b
# while True:
#     if max%a==0 and max%b==0:
#         break
#     max+=1
# print("max=",max)


#gcd/hcf
# a=int(input())
# b=int(input())
# while b:
#     a,b=b,a%b
# print("gcd=",a)




