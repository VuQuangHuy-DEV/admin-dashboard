from datetime import datetime

from rest_framework import serializers
from authentication.models import User
from bidding.models import Proposal
from rental.serializers import UserSerializer
from ultis.api_helper import format_time_difference
from .models import BookingPost


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'

class BookingListSerializer(serializers.ModelSerializer):
    vehicle = serializers.StringRelatedField()
    user = UserSerializer()
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = BookingPost
        fields = ['id', 'title', 'details', 'status', 'start_date', 'end_date', 'departure', 'destination', 'price_min',
                  'price_max', 'num_of_people', 'allows_pet', 'vehicle', 'user','created_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['bidders'] = ProposalSerializer(instance.proposal_set.all(), many=True).data
        return data


class CreateBookingSerializer(serializers.ModelSerializer):
    vehicle = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = BookingPost
        fields = ['id',
                  'title',
                  'details',
                  'status',
                  'start_date',
                  'end_date',
                  'departure',
                  'destination',
                  'price_min',
                  'price_max',
                  'num_of_people',
                  'allows_pet',
                  'user',
                  'vehicle']
class UserSerializer(serializers.ModelSerializer):
    local_phone_number = serializers.CharField()

    class Meta:
        model = User
        fields = ['full_name', 'avatar', 'local_phone_number']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['phone_number'] = data['local_phone_number']
        data.pop('local_phone_number', None)

        return data


class BookingDetailSerializer(serializers.ModelSerializer):
    vehicle = serializers.StringRelatedField()
    user = UserSerializer()
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = BookingPost
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['time_ago'] = format_time_difference(datetime.strptime(data['created_at'], "%d/%m/%Y %H:%M:%S"),
                                                  datetime.now())
        data['bidders'] = ProposalSerializer(instance.proposal_set.all(), many=True).data
        return data
