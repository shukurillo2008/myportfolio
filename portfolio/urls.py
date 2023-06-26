from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('<int:id>', views.portfolio, name='portfolio_url') 
]