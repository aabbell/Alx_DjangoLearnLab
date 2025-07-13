# Retrieving all books
from bookshelf.models import Book

books = Book.objects.all()
print(books.title, books.author, books.publication_year)