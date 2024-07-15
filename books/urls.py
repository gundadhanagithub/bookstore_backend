from django.urls import path
from books import views

urlpatterns = [
    path('', views.books_list),
    path('<int:pk>/', views.book_detais),
]