from django.urls import path
from . import views

app_name = 'autocompleteapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_quotes, name='search_quotes'),
    path('results/', views.result_quotes, name='result_quotes')
]