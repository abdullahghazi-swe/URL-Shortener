from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('details/<int:url_id>/', views.link_details, name='link_details')
]