from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books', views.LibraryView.as_view()),
    path('borrow_book', views.BorrowBooksView.as_view()),
    path('return_book', views.ReturnBooksView.as_view())
]
