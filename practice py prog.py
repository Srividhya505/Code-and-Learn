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



#gcd or hcf
# a=int(input())
# b=int(input())
# while b:
#     a,b=b,a%b
# print("gcd=",a)


#reverse of a given number
# n=int(input())
# rev=0
# while(n!=0):
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)
#we used while loop because we dont know how many times we r going to iterate the loop.


#sum of digits
# n=int(input())
# sum=0
# while(n!=0):
#     r=n%10
#     sum=sum+r
#     n=n//10
# print(sum)


#count of digits
# n=int(input())
# count=0
# while(n!=0):
#     count=count+1
#     n=n//10
# print(count)


#palindrome of a number
# n=int(input())
# temp=n
# rev=0
# while(n!=0):
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if(temp==rev):
#     print("Palindrome")
# else:
#     print("Not a palindrome")



#armstrong number
# n=int(input())
# t=n
# dc=0
# while(n!=0):
#     n=n//10
#     dc=dc+1
# n=t
# s=0
# while(n!=0):
#     r=n%10
#     s=s+r**dc
#     n=n//10
# if(s==t):
#     print("Armstrong Number")
# else:
#     print("Not a Armstrong Number")


# #sum of prime numbers
# a=int(input())
# b=int(input())
# sum=0
# for i in range(a,b+1):
#     fc=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             fc=fc+1
#         if(fc==2):
#             sum=sum+1
#     print(sum)







