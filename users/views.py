from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .models import MovieUser

class UserRegister(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(mixins.UpdateModelMixin, generics.GenericAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = MovieUser.objects.all()
    serializer_class = UserSerializer

    def patch(self, request,pk):
        user = self.get_object()
        
        serializer = UserSerializer(user, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.update(user, request.data)
            return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(data="wrong parameters", status=status.HTTP_400_BAD_REQUEST)