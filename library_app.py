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
                    books[isbn] = {'name': book_name, 'author': author_name, 'checked_out': checked_out}
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

def add_Book():
    isbn = input("please enter your ISBN:")
    bookname = input("please enter a book name:")
    author_name = input("please enter an author name:")
    checked_out = "F"                            #3. choice in the menu: Adding a new book to the file.
    books_for_read= open("books.txt","r")
    for line in books_for_read:
        book_data = line.strip()
        book_data = line.split(",")
        if isbn == book_data[0]:
            checking = 1
            break                          # checking = 1 is means that  there is a book with this isbn.
        else:
            checking = 0
    if checking == 0:           # I used "a" for add to string to my file. I was using "w" to adding -
            with open("books.txt","a") as file:     # something but it always deleting whole file to write. I found it after 1 hour...
                adding_a_book = isbn + "," + bookname +"," + author_name + "," + checked_out
                file.write(adding_a_book)
                print("Book added successfully.")

    elif checking == 1:
            print("Book already exists... Please check the ISBN number.")

def delete_line(txt,number):
    with open(txt,"r") as file:
        lines = file.readlines()
        del lines[number]

def delete_boosk():
    isbn_to_delete = input("Please enter ISBN of the book to delete:")
    with open("books.txt","r") as books_for_read:
        for line in books_for_read:
            book_data = line.strip()
            book_data = line.split(",")
            counter = 0
            if isbn_to_delete == book_data[0]:
                checking = 1
                if checking == 1:
                    if book_data[3] != "T\n":
                        del [isbn_to_delete]
                        print("Book deleted successfully!")
                    else:
                        print("You cannot delete a checked-out book. Please check the ISBN.")
                break
            else:
                checking = 0
                counter += 1
        if checking == 0:
            print("book not found")

def delete_book(books):
    isbn_to_delete = input("Enter ISBN of the book to delete: ")

    if isbn_to_delete in books:
        with open("books.txt", "r") as books_for_read:
            for line in books_for_read:
                book_data = line.strip()  # 5. choice in the menu: searchin book by the isbn.
                book_data = line.split(",")
            if book_data[3] != "F\n":
                del books[isbn_to_delete]
                print("Book deleted successfully!")
                save_data(books)
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
                break

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

list_all_checked_out_books()