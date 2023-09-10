from django.urls import path
from .views import home_fun, prices


urlpatterns = [
    path('home/', home_fun, name='home'),
    path('get-price/', prices, name='prices'),
]
