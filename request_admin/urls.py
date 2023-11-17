from .views import RentalListAPIView, RentalCreateAPIView, RentalDetailAPIView,RentalDeleteAPIView

from django.urls import path

urlpatterns = [

    path("posts/", RentalListAPIView.as_view()),
    path("post/detail/<str:pk>/", RentalDetailAPIView.as_view()),
    path("post/create/", RentalCreateAPIView.as_view()),
    path("post/delete/<str:pk>", RentalDeleteAPIView.as_view()),

]
