from datetime import datetime

from django.contrib.auth import authenticate, login
from django_user_agents.utils import get_user_agent
from phonenumbers import parse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.services.sms_service import process_send_otp
from authentication.models import User, OTP
from authentication.serializers import LoginSerializer, VerifyUserSerializer, CreateAdminUserSerializer, \
    AdminUserLoginSerializer, UpdateAdminPasswordSerializer, ResetAdminPasswordSerializer, GetUserInfoSerializer
from core import settings
from ultis.helper import validate_email_address, get_validate_date, get_full_image_url, convert_phone_number, send_email
from ultis.api_helper import api_decorator


# Normal user
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    @api_decorator
    def post(self, request):

        phone_number = request.data.get('phone_number', None)

        # Trích xuất thông tin trình duyệt, thiết bị và hệ điều hành
        user_agent = get_user_agent(request)
        device = user_agent.device
        browser = user_agent.browser
        os = user_agent.os

        # Tạo nội dung email
        subject = "[XeOi] Cảnh báo đăng nhập hệ thống"
        content = (
            f'<table border="1">'
            f'<tr><td>Số điện thoại</td><td>{phone_number}</td></tr>'
            f'<tr><td>Thời điểm đăng nhập</td><td>{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</td></tr>'
            f'<tr><td>Trình duyệt</td><td>{browser}</td></tr>'
            f'<tr><td>Thiết bị</td><td>{device}</td></tr>'
            f'<tr><td>Hệ điều hành</td><td>{os}</td></tr>'
            f'</table>'
        )
        recipient_list = ['dinhtruongnguyen11@gmail.com', 'ngominhtrong53@gmail.com']

        # Gửi email
        if not settings.DEBUG:
            send_email(recipient_list, subject, content)

        try:
            phone_number = convert_phone_number(phone_number)
        except:
            raise ValueError("Invalid phone number format.")

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)
            user.points = 1000
            user.save()

        otp = OTP.objects.create(user=user)
        response = process_send_otp(user.phone_number, otp.code)
        otp.log = response
        otp.save()

        response_data = {
            "id": user.id,
            'phone_number': user.local_phone_number,
            'is_active': user.is_active,
            'is_verify': user.is_verify,
            'is_staff': user.is_staff,
            'created_at': user.created_at,

        }

        return response_data, "Verification code was sent", status.HTTP_200_OK


class VerifyOTPAPIView(APIView):
    permission_classes = (AllowAny,)

    @api_decorator
    def post(self, request):
        code = request.data.get('otp', 'None')

        # USE FOR CH PLAY TESTING
        if code == '000000':
            phone_number = parse('+84374047031', None)
            user = User.objects.get(phone_number=phone_number)

            response_data = {
                'phone_number': user.local_phone_number,
                'id': user.id,
                'is_active': user.is_active,
                'is_verify': user.is_verify,
                'is_staff': user.is_staff,
                'created_at': user.created_at,
                'token': user.token

            }
            return response_data, "OTP verified successfully", status.HTTP_200_OK

        try:
            otp = OTP.objects.get(code=code, active=True)
            otp.active = False
            otp.save()

            response_data = {
                'phone_number': otp.user.local_phone_number,
                'id': str(otp.user.id),
                'is_active': otp.user.is_active,
                'is_verify': otp.user.is_verify,
                'is_staff': otp.user.is_staff,
                'created_at': otp.user.created_at,
                'token': otp.user.token

            }

            return response_data, "OTP verified successfully", status.HTTP_200_OK
        except OTP.DoesNotExist:
            raise ValueError("Your OTP is not or no longer valid")


class VerifyUserView(APIView):
    @api_decorator
    def post(self, request, pk):
        if not User.objects.filter(id=pk).exists():
            raise ValueError("User doest not exist")

        user = User.objects.get(id=pk)
        user.is_verify = True
        user.save()
        serializer = VerifyUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.is_verify = True
            serializer.save()
            data = serializer.data

            if settings.DEBUG:
                front_id_image_url = get_full_image_url(request, user.front_id_image.url)
                back_id_image_url = get_full_image_url(request, user.back_id_image.url)
                data['front_id_image'] = front_id_image_url
                data['back_id_image'] = back_id_image_url

            return data, "Verify user successfully", status.HTTP_200_OK
        return Response({
            "status_code": status.HTTP_400_BAD_REQUEST,
            "message": "Invalid data format",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Admin user
class CreateAdminUserAPIView(APIView):
    # permission_classes = (IsAdminUser,)
    serializer_class = CreateAdminUserSerializer

    @api_decorator
    def post(self, request):

        phone_number = request.data.get('phone_number', None)
        full_name = request.data.get('full_name', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not validate_email_address(email):
            raise ValueError("Invalid email format.")

        try:
            phone_number = convert_phone_number(phone_number)
        except:
            raise ValueError("Invalid phone number format")

        if User.objects.filter(phone_number=phone_number).exists():
            raise ValueError("User already exists")

        user = User.objects.create_user(phone_number=phone_number)
        user.full_name = full_name
        user.email = email
        user.is_staff = True
        user.is_verify = True
        user.points = 1000

        if password:
            user.set_password(password)
            new_pwd = password
        else:
            new_pwd = user.new_password

        user.save()

        response_data = {
            "id": user.id,
            'full_name': user.full_name,
            'phone_number': user.local_phone_number,
            'email': email,
            'password': new_pwd,
            'is_active': user.is_active,
            'is_verify': user.is_verify,
            'is_staff': user.is_staff,
            'created_at': user.created_at,

        }
        return response_data, "Create new admin user successfully", status.HTTP_201_CREATED


class AdminUserLoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = AdminUserLoginSerializer

    @api_decorator
    def post(self, request):

        phone_number = request.data.get('phone_number', None)
        password = request.data.get('password', None)

        try:
            phone_number = convert_phone_number(phone_number)
        except:
            raise ValueError("Invalid phone number format")

        user = authenticate(request, phone_number=phone_number, password=password)

        if user is None:
            raise ValueError("Invalid phone number or password")

        if not user.is_staff:
            return Response({}, "Incorrect permissions to access", status=status.HTTP_401_UNAUTHORIZED)

        if user.last_login:
            login(request, user)

        response_data = {
            "id": user.id,
            'full_name': user.full_name,
            'phone_number': user.local_phone_number,
            'email': user.email,
            'is_active': user.is_active,
            'is_verify': user.is_verify,
            'last_login': get_validate_date(user.last_login),
            'is_staff': user.is_staff,
            'created_at': user.created_at,
            'token': user.token
        }
        return response_data, "Login successfully", status.HTTP_200_OK


class UpdateAdminPasswordAPIView(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UpdateAdminPasswordSerializer

    @api_decorator
    def post(self, request):

        phone_number = request.user.phone_number
        new_password = request.data.get('new_password', None)
        renew_password = request.data.get('renew_password', None)

        if new_password != renew_password:
            raise ValueError("The entered passwords do not match.")
        if not User.objects.filter(phone_number=phone_number).exists():
            raise ValueError("User doest not exists.")
        user = User.objects.get(phone_number=phone_number)
        user.set_password(new_password)
        user.save()

        login(request, user)
        return {}, "Update password successfully", status.HTTP_200_OK


class ResetAdminPasswordAPIView(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ResetAdminPasswordSerializer

    @api_decorator
    def post(self, request):
        phone_number = request.data.get('phone_number', None)
        try:
            phone_number = convert_phone_number(phone_number)
        except:
            raise ValueError("Invalid phone number format.")
        if not User.objects.filter(phone_number=phone_number).exists():
            raise ValueError("User doest not exists.")

        user = User.objects.get(phone_number=phone_number)

        if not user.is_staff:
            raise ValueError("This user is not an admin.")

        new_pwd = user.new_password

        response_data = {
            'phone_number': user.local_phone_number,
            'new_password': new_pwd,
        }
        return response_data, "Reset password successfully", status.HTTP_200_OK


class GetUserInfoAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @api_decorator
    def get(self, request):
        phone_number = request.user.phone_number
        user = User.objects.get(phone_number=phone_number)
        serializer = GetUserInfoSerializer(user, context={'request': request})
        return serializer.data, "Retrieve data successfully", status.HTTP_200_OK

