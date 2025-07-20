from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {'book_list':books}
    return render (request, 'relationship_app/list_books.html' ,context)

class library_list(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books_list'] = library.get_books_list()
        return context