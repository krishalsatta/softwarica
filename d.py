# a="programming"
# for i in range(0,11):
#     print(i,"=", a[i])
# else:
#    print("python")

# for i in range(10,0,-1):
#     print("2 * ", i ,"=",i*2) 
# a="python"
# for i in range(5,-1,-1):
#     print(a[i],end="")
#user sanga compare garne ani 3 choti vanda badi wrong input deyo vane logged out vanera message

# a=[1,2,3]
# for i in reversed(a):
#     print("[",i,"]",end="")
# o_l=[1,2,3]
# r_l=[]
# for i in reversed(o_l):
#     r_l.append(i)
# print(r_l)

# a=[5,4,8,9,10,12]
# sum=16
# for i in a:
#      sum=sum*i
# print(sum)
# a=int(input("enter a number"))
# if a>1:
#     for i in range(2,a):
#         if a%i==0:
#             print("it is not prime")
#             break
#     else:
#         print("it is prime")
# username=input("enter username:")
# password=input("enter password:")
# for i in range(0,3):
#     print("enter your credentials")
#     username1=input("enter your username:")
#     password1=input("enter your password:")
#     if username==username1 and password==password1:
#         print("you are sucessfully logged")
#         break
#     else:
#         if (username!=username1 or password!=password1):
#             print("invalid credentials")
# else:
#     print("3 attemp finished")
# i=1
# while i<=10:
#     if i==5:
#         break
#     print(i)
#     i=i+1
# else:
#     print("hello")

# def add(y):
#     x=10
#     return x+y
# sum=add(20)
# print(sum)



# def add(x,y):
#     c=x*y
#     return c
# sum=add(20,30)
# print(sum)

# with no argument and no return value
# def a():
#     x=10
#     y=100
#     d=y/x
#     print(d)
# a()    

# def greatest(a,b,c):
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=int(input("enter a number"))
#     if a>b:
#         if a>c:
#             return a
#         else:
#             return c
#     elif b>a:
#         if b>c:
#             return b
#         else:
#             return c
# x=greatest("a","b","c")
# print(f"greatest number is {x}" )

# def disp():
#     def show():
#         print("show function")
#     print("disp function")
#     show()
# disp()
# def add():
#     print("Add")
# print("python")
# add()
# print("hello")

# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         nonlocal z
#         z=z+1
#         print(x)
#         print("inside the function y ",y)
#     inner()
#     print("z:",z)
# outer()

# x=10
# def outer():
#     x=4
#     def inner():
#         x=8   
#     inner()
#     print(x)
# outer()



# def outer():
#     x="local"
#     def inner():
#         nonlocal x
#         x="nonlocal"
#         print("inner: ",x)
#     inner()
#     print("outer:",x)
# outer()n3

# li=[5,7,22,97,54,62,77,23,73,64]
# square_list=list(map(lambda x:x**2,li))
# print(square_list)


# a=[1,2,3]
# b=[4,5,6]
# abc=list(map(lambda x, y:x+y,a,b))
# print(abc)
for i in range(4):
    print(i,end="")