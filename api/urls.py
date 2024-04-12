
from django.urls import path
from dashboard.views import invoice_report




urlpatterns = [
    path('invoice_report/', invoice_report.as_view(), name='invoice_report'),
    
]