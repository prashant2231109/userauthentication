

from django.urls import path,include
from auth_api.views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
   
]