from django.urls import path
from .views import WhisperListView, WhisperCreateView

urlpatterns = [
  path('', WhisperListView.as_view(), name='home'),
  path('new', WhisperCreateView.as_view(), name='new'),
]
