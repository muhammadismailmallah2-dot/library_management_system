# =====================================================
#  LIBRARY MANAGEMENT SYSTEM
#  Developed by: Ismail
#  Date: October 2025
# =====================================================

import datetime

# Book class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"[{self.book_id}] {self.title} by {self.author} — {status}")


# Member class
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def display_info(self):
        print(f"[{self.member_id}] {self.name} — Borrowed: {len(self.borrowed_books)} book(s)")


# BorrowRecord class
class BorrowRecord:
    def __init__(self, member, book):
        self.member = member
        self.book = book
        self.borrow_date = datetime.date.today()
        self.due_date = self.borrow_date + datetime.timedelta(days=14)
        self.return_date = None

    def is_overdue(self):
        return self.return_date is None and datetime.date.today() > self.due_date


# Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrow_records = []
        self.load_sample_data()

    def load_sample_data(self):
        self.books = [
            Book(1, "Shah Jo Risalo", "Shah Abdul Latif Bhittai"),
            Book(2, "Sachal Sarmast", "Sachal Sarmast"),
            Book(3, "History of Sindh", "Mirza Qaleech Baig"),
            Book(4, "Love of Punhun", "Shaikh Ayaz"),
            Book(5, "Umar Marvi", "Shah Abdul Latif Bhittai"),
            Book(6, "Moomal Rano", "Shah Abdul Latif Bhittai"),
        ]
        self.members = [
            Member(1, "Ismail"),
            Member(2, "Hyder"),
        ]

    def display_all_books(self):
        print("\nAll Books:")
        for book in self.books:
            book.display_info()

    def display_available_books(self):
        print("\nAvailable Books:")
        available_books = [b for b in self.books if b.available]
        if available_books:
            for book in available_books:
                book.display_info()
        else:
            print("No books available right now.")

    def display_all_members(self):
        print("\nAll Members:")
        for member in self.members:
            member.display_info()

    def search_books(self, keyword):
        print(f"\nSearch Results for '{keyword}':")
        results = [b for b in self.books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]
        if results:
            for book in results:
                book.display_info()
        else:
            print("No matching books found.")

    def borrow_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not member or not book:
            print("Invalid member or book ID.")
            return

        if not book.available:
            print("Book already borrowed.")
            return

        record = BorrowRecord(member, book)
        self.borrow_records.append(record)
        member.borrowed_books.append(book)
        book.available = False
        print(f"\n{member.name} successfully borrowed '{book.title}'.")

    def return_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not member or not book:
            print("Invalid member or book ID.")
            return

        record = next((r for r in self.borrow_records if r.member == member and r.book == book and not r.return_date), None)
        if record:
            record.return_date = datetime.date.today()
            book.available = True
            member.borrowed_books.remove(book)
            print(f"\n'{book.title}' returned successfully by {member.name}.")
        else:
            print("No active borrow record found.")

    def view_member_borrowed_books(self, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            print("Invalid member ID.")
            return

        print(f"\n{member.name}'s Borrowed Books:")
        if member.borrowed_books:
            for book in member.borrowed_books:
                print(f"- {book.title}")
        else:
            print("No borrowed books.")

    def view_overdue_books(self):
        print("\nOverdue Books:")
        overdue_records = [r for r in self.borrow_records if r.is_overdue()]
        if overdue_records:
            for r in overdue_records:
                print(f"{r.book.title} — Borrowed by {r.member.name} — Due: {r.due_date}")
        else:
            print("No overdue books.")

    def library_report(self):
        total_books = len(self.books)
        available_books = sum(1 for b in self.books if b.available)
        total_members = len(self.members)
        active_members = sum(1 for m in self.members if m.borrowed_books)
        borrowed_books = sum(1 for b in self.books if not b.available)
        overdue_books = sum(1 for r in self.borrow_records if r.is_overdue())

        print(f"""
================= LIBRARY REPORT =================
Total Books: {total_books}
Available Books: {available_books}
Total Members: {total_members}
Active Members: {active_members}
Currently Borrowed: {borrowed_books}
Overdue Books: {overdue_books}
==================================================
""")

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        print(f"\nBook '{title}' added successfully.")

    def register_member(self, name):
        member_id = len(self.members) + 1
        new_member = Member(member_id, name)
        self.members.append(new_member)
        print(f"\nMember '{name}' registered successfully.")