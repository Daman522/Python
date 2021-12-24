# class Employee():

#     def __init__(self,first,last,pay,*args, **kwargs):
#         self.first=first
#         self.last=last
#         self.pay=pay
        

#     def fullname(self,*args):
#         for i in args:
#             print(i,self.first)

# e1=Employee(pay=8000,first='daman',last='kaur',)
# print(e1.fullname('daman','simran','john'))


class Employee():

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first+last+'@gmail.com'

    def fullname(self):
        a=7+3
        return a 

e1=Employee(last='preet',pay=90,first='daman')
e2=Employee('jon','sss',9000)
print(e1.pay)
print(e2.last)
print(e1.fullname())


from datetime import datetime

datetime.strptime("2017-02-02 19:02:03","%Y%m%d")