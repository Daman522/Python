# n=6
# for i in range(n):
#     print("*" * i)

# n=6
# for i in range(n,-1,-1):
#     print("*" * i)

n=6
for i in range(1,n):
    print((n-i)*" " + (i * '*') )

# n=4
# for i in range(1,n):
#     print("*" * (i+2))

# n=8
# for i in range(1,n,2):
#     print((n-i)* " " + (i * "*"))

# n=4
# for i in range(n):
#     for j in range(0,n-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*" , end=" ")
#     print()

# n=4
# for i in range(1,n):
#     print(" "* (n-i)+ "* "*i)

n=5
for i in range(n):
    print( " " * (n-i)+(i* "* "))
for i in range(n,0,-1):
    print( " " * (n-i)+(i* "* "))
