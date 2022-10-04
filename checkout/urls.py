from django.urls import path, include
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('orderstatus/', views.orderstatus, name='orderstatus'),
    path('search_orders/', views.search_orders, name='search_orders'),
    path('order_list/', views.search_order, name='order_list'),
    path('wh/', webhook, name='webhook'),
]