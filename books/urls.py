from django.contrib import admin
from django.urls import path
from  .  import views

urlpatterns = [
    path('', views.book_list, name = "book_list"),
    path('add/',views.book_create, name = "book_create"),
    path('<int:pk>/edit/', views.book_update, name = "book_update"),
    path('<int:pk>/delete', views.book_delete, name = "book_delete"),
    path('<int:pk>/details', views.book_details, name = "book_details"),
    path('register/', views.registration_view, name ="register"),
    path('<int:pk>/review', views.add_review, name = 'add_review'),
]
