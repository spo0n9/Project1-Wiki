from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.title, name="title"),
    path("newpage", views.newpage, name='newpage'),
    path("random_page", views.random_page, name="random_page"),
    path("search", views.search, name="search"),
    path("createdpage", views.createdpage, name="createdpage"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("submitedit", views.submitedit, name="submitedit")
]
