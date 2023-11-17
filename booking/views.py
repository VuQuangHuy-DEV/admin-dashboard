from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination

from authentication.models import User
from core import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from general.models import Vehicle
from ultis.api_helper import api_decorator
from ultis.helper import CustomPagination
from .models import BookingPost
from .serializers import BookingListSerializer, CreateBookingSerializer,BookingDetailSerializer


class BookingListAPIView(APIView):
    @api_decorator
    def get(self, request):
        posts = BookingPost.objects.all().order_by('-created_at')
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = BookingListSerializer(result_page, many=True)
        data = paginator.get_paginated_response(serializer.data).data
        return data, "Retrieve data successfully", status.HTTP_200_OK


class BookingFilterListAPIView(APIView):
    @api_decorator
    def get(self, request, pk):
        vehicle = Vehicle.objects.get(id=pk)
        posts = BookingPost.objects.filter(vehicle=vehicle).order_by('-created_at')
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = BookingListSerializer(result_page, many=True)
        data = paginator.get_paginated_response(serializer.data).data
        return data, "Retrieve data successfully", status.HTTP_200_OK


class BookingByUserListAPIView(APIView):
    @api_decorator
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        posts = BookingPost.objects.filter(user=user).order_by('-created_at')
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = BookingListSerializer(result_page, many=True)
        data = paginator.get_paginated_response(serializer.data).data
        return data, "Retrieve data successfully", status.HTTP_200_OK



class CreateBookingAPIView(APIView):
    @api_decorator
    def post(self, request):
        vehicle_id = request.data.get('vehicle_id', None)
        user_id = request.data.get('user_id', None)
        user = User.objects.get(id=user_id)
        vehicle = Vehicle.objects.get(id=vehicle_id)
        serializer = CreateBookingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, vehicle=vehicle)
            data = serializer.data
            data.pop('user', None)
            return data, "Create booking post successfully", status.HTTP_201_CREATED



class BookingDetailAPIView(APIView):
    @api_decorator
    def get(self, request, pk):
        queryset = BookingPost.objects.get(id=pk)
        serializer = BookingDetailSerializer(queryset, context={'request': request})
        return serializer.data, "Retrieve data successfully", status.HTTP_200_OK