from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse
from django.db.models import F
from rest_framework import status

from .models import Movies
from .serializers import MovieSerializer, MovieListSerializer

# Create your views here.

class MoviesList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Movies.objects.all()
    serializer_class = MovieListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MovieDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, pk):
        movie = self.get_object()
        
        serializer = MovieSerializer(movie, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.update(movie, request.data)
            return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(data="wrong parameters", status=status.HTTP_400_BAD_REQUEST)