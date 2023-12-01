from django.urls import path
from shop import views 
from .views import SignUpView, CustomPasswordChangeView, ProfilePageView,ProfileUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='profile_view'),
    path('profile_edit/<int:pk>/', ProfileUpdateView.as_view(), name='profile_edit'),

]