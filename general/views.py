from rest_framework import status
from rest_framework.views import APIView
from ultis.api_helper import api_decorator
from ultis.helper import get_full_image_url
from .models import Cities, Vehicle
from .serializers import CitySerializer


class CityAPIView(APIView):
    @api_decorator
    def get(self, request):
        cities = Cities.objects.all()
        serializer = CitySerializer(cities, many=True)
        data = serializer.data

        main_group = []
        sub_group = []

        for item in data:
            if item['division_type'] == 'trung ương':
                item['image_url'] = get_full_image_url(request, item["image_url"])
                main_group.append(item)
            else:
                item.pop('image_url', None)
                sub_group.append(item)

        result = {
            'main_group': sorted(main_group, key=lambda x: x['position']),
            'sub_group': sorted(sub_group, key=lambda x: x['name'])
        }

        return result, "Retrieve data successfully", status.HTTP_200_OK


class VehicleAPIView(APIView):
    @api_decorator
    def get(self, request):
        vehicle = Vehicle.objects.all()
        serializer = CitySerializer(vehicle, many=True)
        data = serializer.data
        for x in data:
            x['image_url'] = get_full_image_url(request, x["image_url"])

        data = sorted(data, key=lambda x: x['position'])

        return data, "Retrieve data successfully", status.HTTP_200_OK
