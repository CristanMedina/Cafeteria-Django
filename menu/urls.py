from django.urls import path
from .views import (
    MenuListView,
    MenuCreateView,
    MenuUpdateView,
    MenuDeleteView,
)

app_name = 'menu'

urlpatterns = [
    path('', MenuListView.as_view(), name='menu_list'),
    path('nuevo/', MenuCreateView.as_view(), name='menu_create'),
    path('<int:pk>/editar/', MenuUpdateView.as_view(), name='menu_edit'),
    path('<int:pk>/eliminar/', MenuDeleteView.as_view(), name='menu_delete'),
]
