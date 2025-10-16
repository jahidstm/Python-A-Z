class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

book = LibraryItem("Opekkha", "Humayun Ahmed", 1997)
mag = Magazine("Kishore Alo", "Anisul Islam", 2012, "April")

print(f"Book: {book.title} by {book.author} ({book.year})")
print(f"Magazine: {mag.title} - {mag.issue_number} issue ({mag.year})")
