# class Node:
#    def __init__(self, x=12):
#       self.left = 0
#       self.right = 0
#       self.data = x
#    def PrintTree(self):
#       print(self.data,self.right,self.left)

# root = Node(8)
# root.PrintTree()



# def name(n):
#    if len(n)==0:
#     print (n)
#     return
#    print(n)
#    name(n[1:])
#    print (n)

# name('daman')

def num(a):
   if a ==10:
      print(a)
      return
   print(a)
   num(a+1)
 

num(1)
