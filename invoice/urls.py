from django.contrib import admin
from django.urls import path, include

from . views import ListSoldItems, GetLatestSoldItems, AddNewItem, get_by_date, AddNewExpense, GetAll


urlpatterns = [
    path('', AddNewItem.as_view(), name='home'),
    path('today/', GetLatestSoldItems.as_view(), name='today'),
    path('search/', get_by_date, name='search'),
    path('expense/', AddNewExpense.as_view(), name='expense'),
    path('get_all/', GetAll.as_view(), name='get all'),
]