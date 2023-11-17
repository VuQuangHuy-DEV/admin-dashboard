from .views import (
    UserListAPIView,
    UserDetailView,
    UserDeleteAPIView,
    UserUpdateAPIView,
    UserDetailByPhoneView,
    UserDetailTwoCol)

from django.urls import path

urlpatterns = [

    path("users/", UserListAPIView.as_view()),
    path("user/detail/<str:pk>/", UserDetailView.as_view()),
    path("user/delete/<str:pk>/", UserDeleteAPIView.as_view()),
    path("user/update/<str:pk>/", UserUpdateAPIView.as_view()),
    path("user/findByPhone/<str:pk>/", UserDetailByPhoneView.as_view()),
    path("user/findByLikePhone/<str:pk>/", UserDetailTwoCol.as_view()),

]
