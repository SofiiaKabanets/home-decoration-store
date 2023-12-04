
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<uuid:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<uuid:product_id>/', views.cart_remove, name='cart_remove'),
    path('detail/', views.cart_detail, name='cart_detail'),
    path('full_remove/<uuid:product_id>/',views.full_remove,name='full_remove'),
]
