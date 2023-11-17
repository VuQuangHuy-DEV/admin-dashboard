from rest_framework import generics, status

from authentication.models import User
from ultis.api_helper import api_decorator
from ultis.helper import CustomPagination
from .models import (Vehicle, Brand, Model,
                     RentalPost)
from .serializers import RentalCreateSerializer, RentalListSerializer, VehicleBrandSerializer, \
    VehicleModelSerializer, RentalDetailSerializer

from rest_framework.views import APIView


class VehicleBrandAPIView(APIView):
    @api_decorator
    def get(self, request):
        brands = Brand.objects.all()
        serializer = VehicleBrandSerializer(brands, many=True)
        return serializer.data, "Retrieve data successfully", status.HTTP_200_OK


class VehicleModelAPIView(APIView):
    @api_decorator
    def get(self, request, pk):
        brand = Brand.objects.get(id=pk)
        models = Model.objects.filter(brand=brand)
        serializer = VehicleModelSerializer(models, many=True)
        return serializer.data, "Retrieve data successfully", status.HTTP_200_OK


# Vehicle Hire
class RentalListAPIView(APIView):
    @api_decorator
    def get(self, request):
        posts = RentalPost.objects.all().order_by('-created_at')

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = RentalListSerializer(result_page, many=True, context={'request': request})
        data = paginator.get_paginated_response(serializer.data).data

        return data, "Retrieve data successfully", status.HTTP_200_OK


class RentalFilterListAPIView(APIView):
    @api_decorator
    def get(self, request, pk):
        vehicle = Vehicle.objects.get(id=pk)
        posts = RentalPost.objects.filter(vehicle=vehicle).order_by('-created_at')

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = RentalListSerializer(result_page, many=True, context={'request': request})
        data = paginator.get_paginated_response(serializer.data).data

        return data, "Retrieve data successfully", status.HTTP_200_OK


class RentalRelativeListAPIView(APIView):
    @api_decorator
    def get(self, request, pk):
        current_post = RentalPost.objects.get(id=pk)
        posts = RentalPost.objects.filter(location=current_post.location).order_by('-created_at')

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = RentalListSerializer(result_page, many=True, context={'request': request})
        data = paginator.get_paginated_response(serializer.data).data

        return data, "Retrieve data successfully", status.HTTP_200_OK


class RentalListFromUserAPIView(APIView):
    @api_decorator
    def get(self, request, pk):
        user = User.objects.get(id = pk)
        posts = RentalPost.objects.filter(user=user).order_by('-created_at')

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = RentalListSerializer(result_page, many=True, context={'request': request})
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
