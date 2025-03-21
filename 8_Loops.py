# for x in '123456':
#     print(x)

# for x in range(4):
#     print(x)


# for x in range(1,10):
#     print(x)

# for x in range(2,22,2):
#     print(x)

# for x in range(1,10,2):
#     print(x)

# for x in range(1,10):
#     if x % 2 != 0:
#         print(x)

# for x in range(1,10):
#     if x % 2 == 0:
#         pass
#     else:
#         print(x)



#  END statment:

# for x in range (6):
#     print (x,end= " ")

# n= int(input("Enter a number: "))
# for row in range (n):
#     for col in range (row+1):
#         print(col,end=" ")
#     print()


# n= int(input("Enter a number: "))
# for row in range (n):
#     for col in range (n-row):
#         print("*",end=" ")
#     print()


# n= int(input("Enter a number: "))
# for row in range (n):
#     for col in range (row+1):
#        print("*",end=" ")
#     print()
# for row in range (n):
#     for col in range (n-row):
#         print("*",end=" ")
#     print()

# i=1
# while i<10:
#     print(i)
#     i=i+2

# for x in 'Rama':
#     if x == 'm':
#         break
#     else:
#         print(x)

# value="rama"
# print(value[2])

# val = 'rama'
# i=0
# while i<len(val):
#     if val[i] == 'm':
#         break  
#     else:
#         print(val[i])
#     i=i+1

# while True:
#     print("1. home ")
#     print("2. about ")
#     print("3. contact ")
#     print("4. exit ")
#     userinput = int(input("Enter a number: "))
#     if userinput == 1:
#         print("Welcome to home page")
#     elif userinput == 2:
#         print("Welcome to about page")
#     elif userinput == 3:
#         print("Welcome to contact page")
#     elif userinput == 4:
#         break
#     else:
#         print("Invalid input")

input= int(input("Enter a number: "))
for x in range (input):
   print(x*x)