# path=[2,7,9,34,99]
# a=99

# for i in path:
#     print(i)
#     if i==99:
#         print('hh')

# path="DDUUDDUUUUD"
# count=0
# step=0
# for i in path:
#     prev=step
#     if i=='D':
#         step=step-1
#     else:
#         step=step+1

#     if prev<0 and step==0:
#         count=count+1
# print(count,'CCCC')

# grade = [29, 40, 73, 67]
# for i in range(len(grade)):
#     if grade[i] > 38:
#         r = grade[i] % 5
#         if r >= 3:
#             q = 5-r
#             grade[i] = grade[i]+q
# print(grade)
candels=[1 ,2 ,3, 4, 5, 4, 3, 2, 1, 3, 4]
m=0
x={}
small=candels[0]
for i in candels:
    if i in x.keys():
        x[i]+=1
        if x[i]>m:
            m=x[i]
    else:
        x[i]=1
    
print(x,m)
smallest_index = None
for key in x.keys():
    if x[key] == m:
        if not smallest_index:
            smallest_index = key
        elif key < smallest_index:
            smallest_index = key
        


print(smallest_index)
# name = "John Appleseed   "
# print(name.rstrip("d"))

# invoice_heading = "Heading*****"
# print(invoice_heading.rstrip("*"))