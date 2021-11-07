from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse
from rest_framework import status
from rest_framework.filters import OrderingFilter

from .models import MovieReview, Movies
from .serializers import MovieSerializer, MovieListSerializer

# Create your views here.

class MoviesList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Movies.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['up_votes', 'down_votes', 'release_date']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Movies.objects.all()
        fav_genre = self.request.query_params.get('genre')
        if fav_genre is not None:
            queryset = queryset.filter(genre=fav_genre)
        return queryset

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

