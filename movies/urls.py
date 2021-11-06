from django.urls import path
from movies import views


urlpatterns = [
    path('', views.MoviesList.as_view()),
    path('<int:pk>/', views.MovieDetail.as_view()),
]