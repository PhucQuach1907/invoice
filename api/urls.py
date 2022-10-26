from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.api_overview, name='overview'),   
    path('invoices/', views.invoice_list, name='invoice_list'), 
    path('today/', views.get_latest_entries, name='latest_entry'), 
    path('invoice/<str:date>/', views.get_by_date),
    path('api/save_screenshot', SaveScreenshot.as_view(), name='save-screenshot')
]
