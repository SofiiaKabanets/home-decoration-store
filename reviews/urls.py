from django.urls import path
from .views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewDeleteView


urlpatterns = [
    path('review/', ReviewListView.as_view(), name = 'review'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name = 'review_detail'),
    path('review/new/', ReviewCreateView.as_view(), name = 'review_new'),
    path('review/delete/', ReviewDeleteView.as_view(), name = 'review_delete'),
]
