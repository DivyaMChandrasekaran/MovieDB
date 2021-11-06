from django.urls import path
from users import views
from rest_framework_simplejwt import views as token_views

urlpatterns = [   
    path('register',views.UserRegister.as_view()),   
    path('detail/<int:pk>/',views.UserDetail.as_view()),    
    path('login', token_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]