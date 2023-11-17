from rest_framework import generics, status
from authentication.models import User
from ultis.api_helper import api_decorator
from ultis.helper import CustomPagination
from rental.models import (Vehicle, Brand, Model,
                           RentalPost)
from rental.serializers import RentalCreateSerializer, RentalListSerializer, VehicleBrandSerializer, \
    VehicleModelSerializer, RentalDetailSerializer

from rest_framework.views import APIView
from rest_framework import serializers
from rental.serializers import UserSerializer


class RentalListAPIView(APIView):
    @api_decorator
    def get(self, request):
        posts = RentalPost.objects.all().order_by('-created_at')

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(posts, request)
        selected_fields = ['id', 'title', 'details', 'user']

        class CustomRentalListSerializer(serializers.ModelSerializer):
            user = serializers.CharField(source='user.full_name')

            class Meta:
                model = RentalPost
                fields = selected_fields

        serializer = (CustomRentalListSerializer(result_page, many=True, context={'request': request}, ))

        data = paginator.get_paginated_response(serializer.data).data

        return data, "Retrieve data successfully", status.HTTP_200_OK


class RentalCreateAPIView(APIView):
    @api_decorator
    def post(self, request):
        vehicle_id = request.data.get('vehicle_id', None)
        user_id = request.data.get('user_id', None)
        user = User.objects.get(id=user_id)
        vehicle = Vehicle.objects.get(id=vehicle_id)
        serializer = RentalCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, vehicle=vehicle)
            data = serializer.data
            return data, "Create rental post successfully", status.HTTP_201_CREATED


class RentalDetailAPIView(APIView):
    @api_decorator
    def get(self, request, pk):
        queryset = RentalPost.objects.get(id=pk)
        serializer = RentalDetailSerializer(queryset, context={'request': request})
        return serializer.data, "Retrieve data successfully", status.HTTP_200_OK

    @api_decorator
    def post(self, request, pk):
        queryset = RentalPost.objects.get(id=pk)
        serializer = RentalDetailSerializer(queryset, context={'request': request})
        return serializer.data, "You used post Method", status.HTTP_200_OK


class RentalDeleteAPIView(APIView):
    @api_decorator
    def delete(self, request, pk):
        rental_post = RentalPost.objects.get(id=pk)
        rental_post.delete()
        return None, "Delete successful", status.HTTP_204_NO_CONTENT
