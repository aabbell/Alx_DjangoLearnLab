from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book
from .models import Library

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {'book_list':books}
    return render (request, 'books/list_books.html' ,context)

class library_list(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name =  'library'