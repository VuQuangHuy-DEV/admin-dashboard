from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView

from authentication.models import User
from bidding.models import Proposal
from bidding.serializers import CreateProposalSerializer, ProposalListSerializer, ProposalDetailSerializer
from booking.models import BookingPost
from general.models import Vehicle
from point_management.models import TransactionHistory
from rental.models import Brand, Model
from ultis.api_helper import api_decorator
from ultis.helper import CustomPagination


class CreateProposalAPIView(APIView):
    @api_decorator
    def post(self, request):
        booking_post_id = request.data.get('booking_post_id', None)
        user_id = request.data.get('user_id', None)
        vehicle_id = request.data.get('vehicle_id', None)
        brand_id = request.data.get('brand_id', None)
        model_id = request.data.get('model_id', None)

        booking_post = BookingPost.objects.get(id=booking_post_id)
        user = User.objects.get(id=user_id)
        vehicle = Vehicle.objects.get(id=vehicle_id)
        brand = Brand.objects.get(id=brand_id)
        model = Model.objects.get(id=model_id)

        serializer = CreateProposalSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            # if len(Proposal.objects.filter(bookingPost=booking_post)) >= 5:
            #     raise ValidationError(f'Số lượt tham gia đấu giá không được lớn hơn 5')
            #
            # if Proposal.objects.filter(user=user).exists():
            #     raise ValidationError(f'Người dùng đã tham gia báo giá bài viết này')
            #
            # if user.points < 30:
            #     raise ValidationError(f'Tài khoản không đủ điểm để tham gia báo giá (số dư hiện tại: {user.points}đ)')
            #
            # if str(user.id) == str(booking_post.user.id):
            #     raise ValidationError(f'Người dùng không thể tham gia đấu giá bài viết họ đã tạo')

            serializer.save(user=user, vehicle=vehicle, brand=brand, model=model, booking_post=booking_post)

            user.points -= 30
            user.save()

            trans = TransactionHistory.objects.create(user=user, points_change=-30, description='Bidding')
            trans.save()

            data = serializer.data
            return data, "Create proposal successfully", status.HTTP_201_CREATED


class ProposalHistoryAPIView(APIView):
    @api_decorator
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        proposals = Proposal.objects.filter(user=user).order_by('-created_at')
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(proposals, request)
        serializer = ProposalListSerializer(result_page, many=True, context={'request': request})
        data = paginator.get_paginated_response(serializer.data).data

        return data, "Retrieve data successfully", status.HTTP_200_OK


class ProposalByBookingAPIView(APIView):
    @api_decorator
    def get(self, request, pk):
        booking_post = BookingPost.objects.get(id=pk)
        proposals = Proposal.objects.filter(booking_post=booking_post).order_by('-created_at')
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(proposals, request)
        serializer = ProposalListSerializer(result_page, many=True, context={'request': request})
        data = paginator.get_paginated_response(serializer.data).data

        return data, "Retrieve data successfully", status.HTTP_200_OK


class ProposalDetailAPIView(APIView):
    @api_decorator
    def get(self, request, pk):
        proposals = Proposal.objects.get(id=pk)
        serializer = ProposalDetailSerializer(proposals, context={'request': request})
        return serializer.data, "Retrieve data successfully", status.HTTP_200_OK


class ProposalApproveAPIView(APIView):
    @api_decorator
    def post(self, request):
        proposal_id = request.data.get('proposal_id', None)

        proposal = Proposal.objects.get(id=proposal_id)
        proposal.status = 'successful'
        proposal.booking_post.status = 'approved'
        proposal.booking_post.save()
        proposal.save()

        others_proposal = Proposal.objects.filter(booking_post=proposal.booking_post)
        for p in [x for x in others_proposal if x != proposal]:
            p.status = 'failed'
            p.save()

        return {}, "Approve proposal successfully", status.HTTP_200_OK


class ProposalRejectAPIView(APIView):
    @api_decorator
    def post(self, request):
        proposal_id = request.data.get('proposal_id', None)

        proposal = Proposal.objects.get(id=proposal_id)
        proposal.status = 'failed'
        proposal.save()

        return {}, "Reject proposal successfully", status.HTTP_200_OK
