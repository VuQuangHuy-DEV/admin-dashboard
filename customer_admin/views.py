from rest_framework import generics, status
from authentication.models import User
from ultis.api_helper import api_decorator
from ultis.helper import CustomPagination
from rest_framework.views import APIView
from rental.serializers import UserSerializer
from rest_framework import serializers
from django.utils import timezone
from django.db.models import Q


# Vehicle Hire
class UserFullSerializer(serializers.ModelSerializer):
    local_phone_number = serializers.CharField(read_only=True)
    class Meta:
        model = User
        exclude = ['phone_number']



class UserListAPIView(APIView):
    @api_decorator
    def get(self, request):
        users = User.objects.all().order_by('-created_at')
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(users, request)
        serializer = (UserFullSerializer(result_page, many=True, context={'request': request}, ))
        data = paginator.get_paginated_response(serializer.data).data
        return data, "Retrieve data successfully", status.HTTP_200_OK


class UserDetailView(APIView):
    @api_decorator
    def get(self, request, pk):
        queryset = User.objects.get(id=pk)
        serializer = UserFullSerializer(queryset, context={'request': request})
        return serializer.data, "Retrieve data successfully", status.HTTP_200_OK


class UserDeleteAPIView(APIView):
    @api_decorator
    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return None, "Delete successful", status.HTTP_204_NO_CONTENT


class UserUpdateAPIView(APIView):
    @api_decorator
    def post(self, request, pk):
        try:
            instance = User.objects.get(id=pk)
            instance.updated_at = timezone.now()
        except User.DoesNotExist:
            return {},'Object not found', status.HTTP_404_NOT_FOUND

        serializer = UserFullSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return {},'Update sucessfull ', status.HTTP_200_OK
        return {}, serializer.errors, status.HTTP_400_BAD_REQUEST





#Tìm kiếm chính xác qua phone_number
class UserDetailByPhoneView(APIView):
    @api_decorator
    def get(self, request, pk):
        queryset = User.objects.get(phone_number=pk)
        serializer = UserFullSerializer(queryset, context={'request': request})
        return serializer.data, "Retrieve data successfully", status.HTTP_200_OK


class UserDetailTwoCol(APIView):
    @api_decorator
    def get(self, request, pk):
        try:
            users = users = User.objects.filter(
                Q(phone_number__icontains=pk) | Q(full_name__icontains=pk)
            )
        except User.DoesNotExist:
            return {},'Users not found', status.HTTP_404_NOT_FOUND

        serializer = UserFullSerializer(users, many=True, context={'request': request})
        return serializer.data, 'Retrieve data successfully',status.HTTP_200_OK
