from django.urls import path
from shop import views 
from .views import SignUpView, CustomPasswordChangeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),

]