from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import LibraryBook

# Список книг
class BookListView(ListView):
    model = LibraryBook
    template_name = 'library/book_list.html'
    context_object_name = 'books'

# Додавання книги
class BookCreateView(CreateView):
    model = LibraryBook
    template_name = 'library/book_form.html'
    fields = ['title', 'author', 'isbn', 'available']
    success_url = reverse_lazy('library:book_list')

# Редагування книги
class BookUpdateView(UpdateView):
    model = LibraryBook
    template_name = 'library/book_form.html'
    fields = ['title', 'author', 'isbn', 'available']
    success_url = reverse_lazy('library:book_list')

# Видалення книги
class BookDeleteView(DeleteView):
    model = LibraryBook
    template_name = 'library/book_delete.html'
    success_url = reverse_lazy('library:book_list')
