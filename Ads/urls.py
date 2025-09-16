from django.urls import path
from .views import ads_view,delete_view

urlpatterns = [
    path('', ads_view, name='ads_list'),
    path('<slug:slug>/', ads_view),
    path('delete/<slug:slug>/', delete_view),
]
