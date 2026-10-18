from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('go/<str:chars>', views.visitShort, name='redirecturl'),
    path('unshortner/', views.unshort, name='unshortner'),
    path('edit/<int:id>', views.edit_url, name='edit'),
    path('status/<int:id>', views.change_status, name='status'),
    path('delete/<int:id>', views.delete_link, name='delete')
]