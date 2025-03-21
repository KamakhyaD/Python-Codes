# Methods and Functions:


# class maths:
#     def square(self):
#         a=10
#         print(a**2)

# m1=maths()
# m1.square()



# def square():
#     a=10
#     print(a**2)
# square()


# Single Level Inheritance:
# class Alpha:
#     def fun(self):
#         print('Alpha class fun()')

# class Beta(Alpha):
#     pass

# b =  Beta()
# b.fun()


# class Alpha:
#     def fun(self):
#         print('Alpha class fun()')

# print(dir(Alpha))


# Multi Level Inheritance:

# class Alpha:
#     def fun1(self):
#         print("inside alpha fun1()")

# class Beta(Alpha):
#     def fun2(self):
#         print("inside beta fun(2)")

# class Gamma(Beta):
#     pass

# g=Gamma()
# g.fun1()
# g.fun2()


# Multiple inheritance:

# class Alpha:
#     def fun1(self):
#         print("Alpha class fun1()")

# class Beta:
#     def fun2(self):
#         print("Beta class fun2()")

# class Gamma(Alpha,Beta):
#     pass

# g= Gamma()
# g.fun1()
# g.fun2()


# Super:

# class Customer:
#     def __init__(self,name,ph,email):
#         self.name=name
#         self.ph=ph
#         self.email=email

# class PlatinumCustomer(Customer):
#     def __init__(self,name,ph,email,plat_id):
#         super().__init__(name,ph,email)
#         self.plat_id=plat_id


# def display(self):
#     print(self.__dict__)

# p=PlatinumCustomer('KD',1234567890,'ken.kamakhya3@gmail.com',123)
# display(p)


class Customer:
    def __init__(self,name,ph,address):
        self.name=name
        self.ph=ph
        self.address=address
    
    def place_order(self,dish):
        cost=0
        del_chg=50
        if dish=='Pizza':
            cost=500+del_chg
        else:
            cost=200+del_chg
        return cost
    
class PlatinumCustomer(Customer):
        def __init__(self,name,ph,address,plat_id):
            super().__init__(name,ph,address)
            self.plat_id=plat_id
        def place_order(self, dish):
            del_chg=50
            return
            (super().place_order(dish)-del_chg)*0.95

p=PlatinumCustomer('KD',1234567890,'Ken',123)
print(p.place_order('Pizza'))




    