from relationship_app.models import Author , Book , Librarian,Library


author = Author.objects.get(name = "abel")
books = Book.objects.filter(author=author)

library = Library.objects.get(name="Addis Ababa Library")
books = library.Book.all()

librarian = Librarian.objects.get(name="Addis")
