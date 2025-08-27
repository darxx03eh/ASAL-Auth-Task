from http import HTTPStatus
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from api.models.user import  User
from rest_framework import serializers
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email', 'password', 'phone_number'
        )
    def validate_phone_number(self, value: str):
        if value.startswith('+970') or value.startswith('972'):
            return value
        raise serializers.ValidationError('Phone number must be entered in the format: +97012345678')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'data': data,
        }

class UserRetrieve(BaseUserSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email', 'phone_number'
        )
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'status_code': HTTPStatus.OK,
            'meta': None,
            'success': True,
            'message': 'Current User Data',
            'errors': None,
            'data': data
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email', 'phone_number'
        )

class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate_refresh(self, value):
        try:
            self.token = RefreshToken(value)
        except:
            raise serializers.ValidationError("Invalid or expired token")
        return value
    def save(self, **kwargs):
        self.token.blacklist()