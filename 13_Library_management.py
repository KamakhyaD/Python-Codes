# Library Management:
def show_books():
    list1=['The Mind','Harry Potter','The Secret','The Power of now','The Alchemist']
    print("Books available:")
    for x in list1:
        print(x)
    return list1

class admin:
    def check_book(self, available_books, requested_book):
        if requested_book in available_books:
            print("Book available")
        else:
            print("Book not available")
        pass

    def lending_book(self, requested_book):
        print(f"Book lent: {requested_book}")
        pass

    def receive_book(self):
        print("Book received")
        pass

    def add_book(self):
        print("Book added")
        pass

    def remove_book(self):
        print("Book removed")
        pass

    def payment(self):
        print("Payment done")
        pass

class parent_book:
    def request_book(self):
        userinput = input("Enter the book you want to request: ")
        print(f"Book requested by you: {userinput}")
        return userinput

    def return_book(self):
        print("Book returned")
        pass

class student_book(parent_book):
    pass

class management_book(parent_book):
    def payment(self):
        print("Payment done")
        pass

# Main execution
p1 = parent_book()
requested_book = p1.request_book()
available_books = show_books()
a1 = admin()
a1.check_book(available_books, requested_book)
a1.lending_book(requested_book)