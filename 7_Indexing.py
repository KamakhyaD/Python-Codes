# val='rama'
# print(val[0])

# val="rama is going"
# print(val.title())

# val="rama is going"
# a= val.split()
# for x in a:
#     print(x[0].upper() + x[1::])


# Slicing

# val="rama is going"
# print(val[1:12:2])


# val="rama is going"
# # print(val[::1])
# print(val[::-1])


# val = str(input("Enter the word: \n"))
# reverse=val[::-1]
# if val== reverse:
#     print( "Its a pallindrome")
# else:
#     print("its not a pallindrome")



# String Formatting:

# name=input(" Enter your name :\n")
# age= int(input(f"Enter {name} age"))


# Define a function to print emojis using their hexadecimal values
def print_emoji(hex_value):
    emoji = chr(int(hex_value, 16))
    print(emoji)

# Example usage
print_emoji('1F600')  # Grinning face
print_emoji('1F602')  # Face with tears of joy
print_emoji('1F609')  # Winking face
print_emoji('1F60D')  # Smiling face with heart-eyes
print_emoji('1F618')  # Face blowing a kiss