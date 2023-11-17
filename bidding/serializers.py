from rest_framework import serializers

from bidding.models import Proposal
from booking.serializers import BookingDetailSerializer, UserSerializer, BookingListSerializer, ProposalSerializer


class CreateProposalSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    vehicle = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    model = serializers.StringRelatedField()
    booking_post = serializers.StringRelatedField()

    class Meta:
        model = Proposal
        fields = '__all__'



class ProposalListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    vehicle = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    model = serializers.StringRelatedField()
    booking_post = BookingListSerializer()

    class Meta:
        model = Proposal
        fields = '__all__'


class ProposalDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    booking_post = BookingDetailSerializer()
    vehicle = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    model = serializers.StringRelatedField()


    class Meta:
        model = Proposal
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['full_name'] = ProposalSerializer(instance.proposal_set.all(), many=True).data
        return data
