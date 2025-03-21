# print('Secure Connection has been established')
# try:
#     p=int(input("Enter the Prinicpal amount: "))
#     t=int(input("Enter the time period: "))
#     r=10
#     si=(p*t*r)/100
#     print(f"Simple Interest: {si}")
# except ValueError:
#     print('Please enter a valid number')

# except ZeroDivisionError:
#     print('Please enter a valid time period')

# except Exception as e:
#     print('Something went wrong')
#     print(e)
    
# print('Secure Connection has been terminated')


# # Specific Errors:
# a=int(input('Enter a number: '))
# b=int(input('Enter a number: '))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print('Cannot divide by zero')
# except ValueError:
#     print('Please enter a valid number')
# except Exception as e:
#     print('Something went wrong')   



# def validate(mob):
#     if len(mob)==10:
#         return True
#     else:
#         raise ValueError('Please enter a valid mobile number')

# def main():
#     try:
#         mob=input('Enter your mobile number: ')
#         validate(mob)
#     except ValueError as e:
#         print(e)
# main()


# mob=input('Enter your mobile number: ')
# try:
#     if len(mob)==10:
#         print('Mobile number is valid')
#     else:
#         raise ValueError('Please enter a valid mobile number')
# except ValueError as e:
#     print(e)

# Name Error
# try:
#     a=10
#     print(b)
#     raise NameError

# except Exception as e:
#     print('Something went wrong')
#     print(e)


# def menu(item):
   
#         if item=='Pizza':
#             print('Pizza is available')
#         elif item=='Burger':
#             print('Burger is available')
#         elif item=='Pasta':
#             print('Pasta is available')
#         else:
#             raise NameError(item)
    

# def main():
#     l1=['Pizza','Burger','Pasta']
#     print("items available", l1)
#     try:
#         item=input('Enter the item: ')
#         menu(item)
#     except NameError as e:
#         print(e,"is not available")
#     finally:
#         print('Thank you for visiting')

# main()
# def fun(x):
#     try:
#         res=100/x
#         print("inside try block")
#         return res
#     except:
#         print("inside except block")
#     else:
#         print("inside else block")
#     finally:
#         print("inside finally block")

# def main():
#     x=int(input("Enter a number: "))
#     print(fun(x))
# main()

# print("Execution started normally")
# L1=[10,20,0,40,50]
# d={1:'c',2:'Java',3:'Python',4:'c++'}

# try:
#     r=int(input("Enter the index number from the list  "))
#     # key error
#     print(d[r]) 
#     num=int(input("Enter the number from the dictionary: "))
#     den=int(input("Enter the denominator: "))
#     print(L1[num]/L1[den])

# except:
#     print("Something went wrong")

# print("Execution completed normally")

# print("Execution started normally")
# L1=[10,20,0,40,50]
# d={1:'c',2:'Java',3:'Python',4:'c++'}

# try:
#     r=int(input("Enter the index number from the list  "))
#     # key error
#     print(d[r]) 
#     num=int(input("Enter the number from the dictionary: "))
#     # if we enter in string it will raise value error
#     den=int(input("Enter the denominator: "))
#     print(L1[num]/L1[den])

# except KeyError:
#     print("Key error occured")
# except ZeroDivisionError:
#     print("Zero division error")
# except IndexError:
#     print("Index error occured")
# except Exception as e:  
#     print("Something went wrong")
#     print(e)

# print("Execution completed normally")

def fun2():
    print("Inside fun2")
    num=int(input("Enter the numerator: "))
    den=int(input("Enter the denominator: "))
    try:
        if den==0:
            raise ZeroDivisionError
        else:
            print(num/den)

    except ZeroDivisionError:
        print("Denominator cannot be zero")
    print("Exiting fun2")

def fun1(): 
    print("Inside fun1")
    fun2()
    print("Exiting fun1")

def main ():
    print("Inside main")
    fun1()
    print("Exiting main")

main()