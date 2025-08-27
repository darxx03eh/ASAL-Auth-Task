from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.user_serializers import UserCreateSerializer, UserSerializer
from api.serializers.user_serializers import LogOutSerializer
from api.models.user import User

class UserRetrieveAPIView(APIView):
    serializer_class = UserSerializer
    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

class UserAPIView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        users = User.objects.all().order_by('pk')
        serializer = UserSerializer(users, many=True)
        return Response({
            'status': status.HTTP_200_OK,
            'meta': None,
            'success': True,
            'message': 'users retrieved successfully',
            'errors': None,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
class SignUpAPIView(APIView):
    serializer_class = UserCreateSerializer
    status_code = status.HTTP_201_CREATED
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'status_code': status.HTTP_201_CREATED,
            'meta': None,
            'success': True,
            'message': 'Current User Data',
            'errors': None,
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

class LogOutAPIView(APIView):
    serializer_class = LogOutSerializer
    status_code = status.HTTP_200_OK
    def post(self, request):
        serializer = LogOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status_code': status.HTTP_200_OK,
            'meta': None,
            'success': True,
            'message': 'Logout Successful',
            'errors': None,
            'data': serializer.data
        }, status=status.HTTP_200_OK)