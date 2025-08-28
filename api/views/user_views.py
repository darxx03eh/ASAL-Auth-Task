from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers.user_serializers import UserCreateSerializer, UserSerializer
from api.serializers.user_serializers import LogOutSerializer
from api.models.user import User
# Token Based Auth
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
        return Response(serializer.data)
        # return Response({
        #     'status': status.HTTP_200_OK,
        #     'meta': None,
        #     'success': True,
        #     'message': 'users retrieved successfully',
        #     'errors': None,
        #     'data': serializer.data
        # }, status=status.HTTP_200_OK)
class SignUpAPIView(APIView):
    serializer_class = UserCreateSerializer
    status_code = status.HTTP_201_CREATED
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({
        #     'status_code': status.HTTP_201_CREATED,
        #     'meta': None,
        #     'success': True,
        #     'message': 'Current User Data',
        #     'errors': None,
        #     'data': serializer.data
        # }, status=status.HTTP_201_CREATED)

class LogOutAPIView(APIView):
    serializer_class = LogOutSerializer
    status_code = status.HTTP_200_OK
    def post(self, request):
        serializer = LogOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        # return Response({
        #     'status_code': status.HTTP_200_OK,
        #     'meta': None,
        #     'success': True,
        #     'message': 'Logout Successful',
        #     'errors': None,
        #     'data': serializer.data
        # }, status=status.HTTP_200_OK)

# Session Based Auth
class SessionLogInAPIView(APIView):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user);
            return Response(status=status.HTTP_200_OK)
            # return Response({
            #     'status_code': status.HTTP_200_OK,
            #     'meta': None,
            #     'success': True,
            #     'message': 'Login Successful',
            #     'errors': None,
            #     'data': None
            # })
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        # return Response({
        #     'status_code': status.HTTP_400_BAD_REQUEST,
        #     'meta': None,
        #     'success': False,
        #     'message': 'Login Failed',
        #     'errors': None,
        #     'data': None
        # })

class SessionLogOutAPIView(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
        # return Response({
        #     'status_code': status.HTTP_200_OK,
        #     'meta': None,
        #     'success': True,
        #     'message': 'Logout Successful',
        #     'errors': None,
        #     'data': None
        # })