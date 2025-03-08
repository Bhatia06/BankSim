from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_account/', views.create_account, name='create_account'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('show_balance/', views.show_balance, name='show_balance'),
    path('view_transactions/', views.view_transactions, name='view_transactions'),
    path('credit/', views.credit, name='credit'),
    path('logout/', views.logout, name='logout'),
]