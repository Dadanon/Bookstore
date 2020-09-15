# books/views.py
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    login_url = 'account_login'


class BookDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    extra_context = {
        'separator': '*' * 80,
    }
    login_url = 'account_login'
    permission_required = 'books.special_status'

# Create your views here.
