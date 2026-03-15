class Employee:
    def get_input(self):
  
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    pass


managers = []

print("Enter details of 10 Managers\n")

for i in range(10):
    print("\nManager", i+1)
    m = Manager()
    m.get_input()
    managers.append(m)

print("\n--- Manager Information ---")

for i in managers:
    i.display()
    class Book:
        def __init__(self, book_id, title, author):
            self.book_id = book_id
            self.title = title
            self.author = author
            self.available = True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully")

    def display_books(self):
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(book.book_id, book.title, book.author, status)

    def lend_book(self):
        book_id = int(input("Enter Book ID to lend: "))
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                print("Book lent successfully")
                return
        print("Book not available")

    def return_book(self):
        book_id = int(input("Enter Book ID to return: "))
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print("Book returned successfully")
                return
        print("Book not found")


library = Library()

while True:
    print("\nLibrary Menu")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        library.lend_book()

    elif choice == 4:
        library.return_book()

    elif choice == 5:
        break

    else:
        print("Invalid choice")