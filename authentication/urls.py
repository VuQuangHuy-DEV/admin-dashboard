from django.urls import path

from authentication.views import LoginAPIView, VerifyOTPAPIView, VerifyUserView, CreateAdminUserAPIView, \
    AdminUserLoginAPIView, UpdateAdminPasswordAPIView, ResetAdminPasswordAPIView, GetUserInfoAPIView

urlpatterns = [
    # Normal user
    path("login/", LoginAPIView.as_view()),
    path("verify/otp/", VerifyOTPAPIView.as_view()),
    path('verify/user/<uuid:pk>/', VerifyUserView.as_view()),
    path('user/info', GetUserInfoAPIView.as_view()),

    # Admin user
    path("admin-user/create/", CreateAdminUserAPIView.as_view()),
    path("admin-user/login/", AdminUserLoginAPIView.as_view()),
    path("admin-user/update/password/", UpdateAdminPasswordAPIView.as_view()),
    path("admin-user/reset/password/", ResetAdminPasswordAPIView.as_view()),

    path("admin-user/reset/password/", ResetAdminPasswordAPIView.as_view()),

]
