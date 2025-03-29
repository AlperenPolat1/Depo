def read_data_books():
    books = {}
    with open('books.txt', 'r') as file:
            for line in file:
                book_data = line.strip()
                book_data = line.split(",")
                if len(book_data) > 2:
                    isbn = book_data[0]
                    book_name = book_data[1]
                    author_name = book_data[2]
                    checked_out = book_data[3]
                    books[isbn] = {'name': book_name, 'author': author_name, 'checked_out': checked_out, "checked_out_by":None}
    return books
def read_students():
    students = {}
    with open('students.txt', 'r') as file:
        for line in file:
            student_data = line.strip().split()
            student_id = student_data[0]
            student_name = ' '.join(student_data[1:])
            students[student_id] = student_name
    return students

books_data = read_data_books()
students_data = read_students()

def save_data(books):
    with open('books.txt', 'w') as file:
        for isbn, book_info in books.items():
            file.write(f"{isbn},{book_info['name']},{book_info['author']},{book_info['checked_out']}")
    print("Data saved successfully!")

def list_all_books():
    with open("books.txt") as reading:            #1. choice in the menu: listing all books in the file.
        for line in reading:
            print(line)

def list_all_checked_out_books():
    with open("books.txt") as bookcheck:
        for line in bookcheck:                  #2. choice in the menu: listin all checked out books.
            bookcheck = line.strip()
            bookcheck = line.split(",")
            checked_out = bookcheck[3]
            if checked_out == "T\n":
                print(line)
def add_book(books):
    isbn = input("Enter ISBN of the new book: ")
    name = input("Enter name of the new book: ")
    author = input("Enter author of the new book: ")
    if isbn not in books_data:                 # 3. choice in the menu: Adding a new book to library.
        books[isbn] = {'name': name, 'author': author, 'checked_out': 'F\n', 'checked_out_by': None}
        print(f"Book {isbn} added successfully!")
        save_data(books_data)
    else:
        print("There is already a book with this ISBN.")

def delete_book(books):
    isbn_to_delete = input("Enter ISBN of the book to delete: ")

    if isbn_to_delete in books:              # 4. choice in the menu: Delete a book in the library.
        if books[isbn_to_delete]['checked_out'] == 'F\n':
            del books[isbn_to_delete]
            print("Book deleted successfully!")
            save_data(books_data)
        else:
            print("Cannot delete a checked-out book. Please check it in first.")
    else:
        print("Book not found.")

def search_by_isbn():
    isbn_to_search = input("Please enter ISBN of the book to search:")
    with open("books.txt", "r") as books_for_read:
        for line in books_for_read:
            book_data = line.strip()                         # 5. choice in the menu: searchin book by the isbn.
            book_data = line.split(",")
            if isbn_to_search == book_data[0]:
                print(book_data[0],",",book_data[1],",",book_data[2],",",book_data[3])
                break
        else:
            print("Book not found!")


def search_by_name():
    name_to_search = input("Please enter name of the book to search:")
    name_to_search = name_to_search.capitalize()
    with open("books.txt", "r") as books_for_read:
        checking = 0
        for line in books_for_read:             # 6. choice in the menu: searching books by their names.
            book_data = line.strip()
            book_data = line.split(",")
            books_names = book_data[1].split()
            if name_to_search in books_names:
                checking = 1
                print(book_data[0], ",", book_data[1], ",", book_data[2], ",", book_data[3])

    if checking == 0:
        print("Book not found.")

def save_students_with_books(students, books):
    with open('students_with_books.txt', 'w') as file:
        for student_id, student_name in students.items():
            checked_out_books = [isbn for isbn, book_info in books.items() if book_info['checked_out'] == 'T\n' and book_info['checked_out_by'] == student_id]
            if checked_out_books:
                file.write(f"Student : {student_id}  {student_name}\n")
                for isbn in checked_out_books:
                    file.write(f" - Checked Out Book: {isbn}, {books[isbn]['name']}, {books[isbn]['author']}, {books[isbn]['checked_out']}\n")


def update_students_with_books_file(student_id, books, students):
    save_students_with_books({student_id: students[student_id]}, books)

def check_out_book_to_student(books, students):
    isbn_to_check_out = input("Enter ISBN of the book to check out: ")
    student_id = input("Enter student ID: ")

    if isbn_to_check_out in books and student_id in students:              #7. choice in the menu: checking out a book to a student
        if books[isbn_to_check_out]['checked_out'] == 'F\n':
            books[isbn_to_check_out]['checked_out'] = 'T\n'
            books[isbn_to_check_out]['checked_out_by'] = student_id
            print(f"Book {isbn_to_check_out} checked out to student {student_id}.")
            update_students_with_books_file(student_id, books, students)
            save_data(books_data)
        else:
            print("Book is already checked out.")
    else:
        print("Invalid ISBN or student ID.")

def list_students_with_books(books, students):
    for student_id, student_name in students.items():
        checked_out_books = [isbn for isbn, book_info in books.items() if book_info['checked_out'] == 'T\n' and book_info['checked_out_by'] == student_id]
        print(f"Student : {student_id}  {student_name}")
        if checked_out_books:
            for isbn in checked_out_books:       #8. choice in the menu: Listing the students with their books
                print(f" - Checked Out Book: {isbn}, {books[isbn]['name']}, {books[isbn]['author']}, {books[isbn]['checked_out']}")
        else:
            print("There is no book checked out by student.")

        print()

def display_menu():
    print(" 1 for : List all the books in the library ")
    print(" 2 for : List all the books that are checked-out ")
    print(" 3 for : Add a new book ")
    print(" 4 for : Delete a book ")
    print(" 5 for : Search a book by ISBN number ")
    print(" 6 for : Search book by name ")
    print(" 7 for : Check out a book to a student ")
    print(" 8 for : List all the students with their checked-out books ")
    print(" 9 for : EXIT ")

while True:
    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        list_all_books()
    elif choice == "2":
        list_all_checked_out_books()
    elif choice == "3":
        add_book(books_data)
    elif choice == "4":
        delete_book(books_data)
    elif choice == "5":
        search_by_isbn()
    elif choice == "6":
        search_by_name()
    elif choice == "7":
        check_out_book_to_student(books_data, students_data)
    elif choice == "8":
        list_students_with_books(books_data, students_data)
    elif choice == "9":
        save_data(books_data)
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")