from django.urls import path
from .views import BookingListAPIView, BookingFilterListAPIView, CreateBookingAPIView, BookingDetailAPIView, \
    BookingByUserListAPIView

urlpatterns = [
    path('posts/', BookingListAPIView.as_view()),
    path('posts/<uuid:pk>/', BookingFilterListAPIView.as_view()),
    path('post/create/', CreateBookingAPIView.as_view()),
    path("post/detail/<uuid:pk>/", BookingDetailAPIView.as_view()),
    path("post/user/<uuid:pk>/", BookingByUserListAPIView.as_view()),
]
