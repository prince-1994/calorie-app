from django.urls import path
from .views import UserProfileView

urlpatterns = [
    path('profiles/', UserProfileView.as_view(), name='userprofile')
]