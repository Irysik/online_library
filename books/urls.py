from django.urls import path
from books.views import homepage
from .views import search
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', homepage, name='homepage'),
    path('search/', search, name='search'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<str:fragment>/', views.book_fragment, name='book_fragment'),
    path('books/<int:book_id>/first-20-lines/', views.display_first_20_lines, name='first_20_lines'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
