from django.conf import settings
from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('WorkType/', WorkTypeAPIView.as_view()),
    path('WorkType/<int:pk>/', WorkTypeDetail.as_view()),
    path('Const_projects/', Const_projectsAPIView.as_view()),
    path('Const_projects/<int:pk>/', Const_projectsDetail.as_view()),
    path('Const_services/', Const_servicesAPIView.as_view()),
    path('Const_services/<int:pk>/', Const_servicesDetail.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]