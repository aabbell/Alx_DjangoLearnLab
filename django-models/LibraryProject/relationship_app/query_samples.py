from relationship_app.models import Author , Book , Librarian,Library


def book_by_author(author_name):
    authors = Author.objects.get(name = author_name)
    return Book.objects.filter(author = author)


def book_list_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def Librarian_in_library(library_name):
    return Librarian.objects.get(library__name=library_name)