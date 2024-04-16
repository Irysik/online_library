from typing import Iterable
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Genre, Book
from .forms import SearchForm
from django.db.models import Q
from ebooklib import epub

from .utils import read_book_page


def search(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(name__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query))
    else:
        books = []
    return render(request, 'search_results.html', {'books': books, 'query': query})


def homepage(request):
    genres: Iterable[Genre] = Genre.objects.all()
    books: Iterable[Book] = Book.objects.all()

    return render(
        request=request,
        template_name='homepage.html',
        context={
            "genres": genres,
            "books": books
        }
    )


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def book_fragment(request, fragment):
    return render(request, 'book_fragment.html', {'fragment': fragment})


# def display_first_20_lines(request, book_id):
#     try:
#
#         book = Book.objects.get(pk=book_id)
#         book_path = book.file.path
#
#         with open(book_path, 'r', encoding='utf-8') as file:
#             first_20_lines = []
#             file.seek(0)
#             for _ in range(2000):
#                 line = file.readline()
#                 if not line:
#                     break
#                 first_20_lines.append(line)
#
#         return render(request, 'first_20_lines.html', {'book': book, 'first_20_lines': first_20_lines})
#
#     except Book.DoesNotExist:
#         return HttpResponse('Книга не знайдена', status=404)
#     except Exception as e:
#         return HttpResponse(f'Помилка: {e}', status=500)


def display_first_20_lines(request, book_id):
    book = Book.objects.get(pk=book_id)
    book_path = book.file.path

    page_size = 5000
    page = request.GET.get('page') or ""
    if not page.isdigit():
        page = 1
    page = int(page)
    if page < 1:
        page = 1

    start_symbol = (page - 1) * page_size

    characters, end_symbol = read_book_page(
        book_path=book_path,
        start_byte=start_symbol,
        page_size=page_size,
    )

    text = characters.replace("\n", "<br/>")

    return render(request, "first_20_lines.html", {
        "text": text,
        "page": page,
        "book": book,
    })
