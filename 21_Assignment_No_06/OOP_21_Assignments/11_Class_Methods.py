# Book class
class Book:
    total_books = 0  # class variable to count books

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # increase book count by 1

# Call class method twice
Book.increment_book_count()
Book.increment_book_count()

print(Book.total_books)  # prints 2
