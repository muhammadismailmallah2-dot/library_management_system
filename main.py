from library_classes import Library

def main():
    library = Library()

    while True:
        print("""
==============================================
         LIBRARY MANAGEMENT SYSTEM
==============================================
1. Display All Books
2. Display Available Books
3. Display All Members
4. Search Books
5. Borrow a Book
6. Return a Book
7. View Member's Borrowed Books
8. View Overdue Books
9. Library Report
10. Add New Book
11. Register New Member
0. Exit
==============================================
""")

        choice = input("Enter your choice (0-11): ")

        if choice == "1":
            library.display_all_books()
        elif choice == "2":
            library.display_available_books()
        elif choice == "3":
            library.display_all_members()
        elif choice == "4":
            keyword = input("Enter book title or author: ")
            library.search_books(keyword)
        elif choice == "5":
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            library.borrow_book(member_id, book_id)
        elif choice == "6":
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            library.return_book(member_id, book_id)
        elif choice == "7":
            member_id = int(input("Enter member ID: "))
            library.view_member_borrowed_books(member_id)
        elif choice == "8":
            library.view_overdue_books()
        elif choice == "9":
            library.library_report()
        elif choice == "10":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(title, author)
        elif choice == "11":
            name = input("Enter member name: ")
            library.register_member(name)
        elif choice == "0":
            print("\nExiting... Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()