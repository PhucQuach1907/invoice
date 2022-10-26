from django.contrib import admin
from django.urls import path, include

from project import settings
from . views import ListSoldItems, GetLatestSoldItems, AddNewItem, get_by_date, AddNewExpense

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', AddNewItem.as_view(), name='home'),
    path('today/', GetLatestSoldItems.as_view(), name='today'),
    path('search/', get_by_date, name='search'),
    path('expense/', AddNewExpense.as_view(), name='expense'),
    # path('', views.home)
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)