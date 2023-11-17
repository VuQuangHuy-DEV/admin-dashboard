from django.core.exceptions import ValidationError
from rest_framework import serializers

from authentication.models import User
from core import settings


# Normal user
class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class VerifyOTPSerializer(serializers.Serializer):
    otp = serializers.CharField()


class VerifyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'full_name',
            'gender',
            'date_of_birth',
            'doc_id',
            'date_issued',
            'date_expired',
            'place_issued',
            'hometown',
            'permanent_address',
            'nationality',
            'front_id_image',
            'back_id_image',
        )

    def validate(self, data):
        self.validate_front_id_image(data['front_id_image'])
        self.validate_back_id_image(data['back_id_image'])
        return data

    def validate_front_id_image(self, value):
        if value:
            allowed_formats = ('image/jpeg', 'image/png')
            if value.content_type not in allowed_formats:
                raise ValidationError("Invalid image format. Only JPEG and PNG are accepted.")

            if value.size > 5 * 1024 * 1024:  # 5MB file size limit
                raise ValidationError("Image size is too large. The limit is 5MB.")

        return value

    def validate_back_id_image(self, value):
        if value:
            allowed_formats = ('image/jpeg', 'image/png')
            if value.content_type not in allowed_formats:
                raise ValidationError("Invalid image format. Only JPEG and PNG are accepted.")

            if value.size > 5 * 1024 * 1024:  # 5MB file size limit
                raise ValidationError("Image size is too large. The limit is 5MB.")

        return value


# Admin user
class CreateAdminUserSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.CharField()


class AdminUserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()


class UpdateAdminPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()
    renew_password = serializers.CharField()


class ResetAdminPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class GetUserInfoSerializer(serializers.ModelSerializer):
    local_phone_number = serializers.CharField()
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    class Meta:
        model = User
        exclude = ('password',
                   'is_superuser',
                   'front_id_image',
                   'back_id_image',
                   'groups',
                   'user_permissions',
                   'updated_at',
                   )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['phone_number'] = data['local_phone_number']
        data['full_name'] = data['full_name'] if len(data['full_name']) else data['phone_number']
        data.pop('local_phone_number', None)

        return data
