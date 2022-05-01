from django.urls import path
# from rest_framework_simplejwt.views import MyTokenObtainPairView,TokenObtainPairView
from api.views import user_views as views
from api.views.user_views import MyTokenObtainPairView



urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/',views.registerUser,name='register'),
    path('profile/',views.getUserProfile,name='users-profile'),
    path('profile/update/',views.updateUserProfile,name='update-profile'),

    path('',views.getUsers,name='users'),
    path('<str:pk>/',views.getUserById,name='user'),

    path('update/<str:pk>/',views.updateUser,name='user-update'),
    path('delete/<str:pk>/',views.deleteUsers,name='user-delete'),
]
