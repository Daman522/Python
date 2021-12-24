# def hello():
    
#     return 8
# if hello()==8:
#     print('equal')
# else:
#     print('no match')
# import antigravity

# l=[1,2,4]
# l.append([6,8])
# print(l)
# print(l[3][0])

# a=[34,5,7,8,9,0,1,4]
# g=int(len(a)/2)
# print(a[g])

# num = 3452
# count = 0

# while num != 0:
#     num//=10
#     count += 1

# print("Number of digits: " ,count)

# def factorial(x):
#      if x==1:
#          return 1
#      else:
#         print(x*factorial(x-1))
# x=3
# print(factorial(x))


def recursive_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
   
n_terms = 5
   
# check if the number of terms is valid
if n_terms <= 0:
   print("Invalid input ! Please input a positive value")
else:
   print("Fibonacci series:")
   for i in range(n_terms):
       print(recursive_fibonacci(i))